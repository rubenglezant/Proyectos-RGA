package es.rga.pokemon.runner;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Properties;
import java.util.StringTokenizer;

import javax.swing.table.DefaultTableModel;

import com.jcraft.jsch.ChannelExec;
import com.jcraft.jsch.JSch;
import com.jcraft.jsch.Session;

public class Runner extends Thread {

	ArrayList<String> hosts;
	String cmds;
	ArrayList<String> nombreCmds;
	DefaultTableModel dtm;

	public Runner(String IPs, String cmds, DefaultTableModel dtm) {
		this.hosts = new ArrayList<String>();
		this.nombreCmds = new ArrayList<String>();
		nombreCmds.add("IP");
		this.dtm = dtm;
		
		this.leerHost(IPs);
		this.leerCmds(cmds);
	}

	public void run() {
		//String header[] = new String[] { "IP", "VALOR", "VALOR" };
		Object header[] = nombreCmds.toArray();
		dtm.setColumnIdentifiers(header);
		dtm.addRow(header);
		ArrayList<String> out = new ArrayList<String>();
		for (int i = 0; i < hosts.size(); i++) {
			String ip = hosts.get(i);
			try {
				out = this.execSSH(ip, cmds);
			} catch (Exception e) {
				e.printStackTrace();
			}
			dtm.addRow(out.toArray());
		}

	}

	public void leerHost(String file) {
		File archivo = null;
		FileReader fr = null;
		BufferedReader br = null;

		try {
			// Apertura del fichero y creacion de BufferedReader para poder
			// hacer una lectura comoda (disponer del metodo readLine()).
			archivo = new File(file);
			fr = new FileReader(archivo);
			br = new BufferedReader(fr);

			// Lectura del fichero
			String linea;
			while ((linea = br.readLine()) != null)
				hosts.add(linea);
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			try {
				if (null != fr) {
					fr.close();
				}
			} catch (Exception e2) {
				e2.printStackTrace();
			}
		}
	}

	public void leerCmds(String file) {
		File archivo = null;
		FileReader fr = null;
		BufferedReader br = null;

		try {
			archivo = new File(file);
			fr = new FileReader(archivo);
			br = new BufferedReader(fr);
			String linea;
			cmds ="";
			while ((linea = br.readLine()) != null) {
				StringTokenizer st = new StringTokenizer(linea, ":");
				nombreCmds.add(st.nextToken());
				cmds+=(st.nextToken()+"\n");
			}
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			try {
				if (null != fr) {
					fr.close();
				}
			} catch (Exception e2) {
				e2.printStackTrace();
			}
		}
	}
	
	private ArrayList<String> execSSH(String ip, String cmds) throws Exception {
		ArrayList<String> out = new ArrayList<String>();
		JSch jsch=new JSch();
		 Session session=jsch.getSession("root", ip, 22);
		   session.setPassword("ctm");
		   Properties config = new Properties();
		   config.put("StrictHostKeyChecking", "no");
		   session.setConfig(config);
		   session.connect();

		   ChannelExec channel=(ChannelExec) session.openChannel("exec");
		   BufferedReader in=new BufferedReader(new InputStreamReader(channel.getInputStream()));
		   channel.setCommand(cmds);
		   channel.connect();

		   String msg=null;
		   out.add(ip);
		   while((msg=in.readLine())!=null){
		    out.add(msg);
		   }

		   channel.disconnect();
		   session.disconnect();
		   return out;
	}

}
