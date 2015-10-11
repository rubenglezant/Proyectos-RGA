package es.rga.pokemon;

import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.JTextArea;
import javax.swing.SwingUtilities;
import javax.swing.table.DefaultTableModel;
import javax.swing.UIManager;
import javax.swing.UnsupportedLookAndFeelException;

import es.rga.pokemon.runner.Runner;

public class Pokemon extends JFrame implements ActionListener

{
	JButton miBoton = new JButton("Button");
	JCheckBox miCheckBox = new JCheckBox("Check");
	JTextArea miAreaDeTexto = new JTextArea("My text");

	JPanel panelSuperior = new JPanel();
	JPanel panelInferior = new JPanel();
	JPanel panelTodo = new JPanel();

	JTable tbl = new JTable();
	DefaultTableModel dtm = new DefaultTableModel(0, 0);
	JScrollPane panel = new JScrollPane(tbl);

	public Pokemon() {
		String header[] = new String[] { "IP", "VALOR" };
		dtm.setColumnIdentifiers(header);
		tbl.setModel(dtm);

		panelSuperior.setLayout(new FlowLayout());
		panelSuperior.add(miCheckBox);
		panelSuperior.add(miBoton);

		panelInferior.setLayout(new FlowLayout());
		panelInferior.add(miAreaDeTexto);

		panelTodo.setLayout(new BorderLayout());
		panelTodo.add(panelSuperior, BorderLayout.NORTH);
		panelTodo.add(panel, BorderLayout.CENTER);
		panelTodo.add(panelInferior, BorderLayout.SOUTH);

		getContentPane().add(panelTodo, BorderLayout.CENTER);

		miBoton.addActionListener(this);
		miCheckBox.addActionListener(this);


		setDefaultCloseOperation(DISPOSE_ON_CLOSE);
	}

	public static void main(String[] args) {
		Pokemon myApplication = new Pokemon();

		// Especifica donde aparecerá en la ventana:
		myApplication.setLocation(200, 100);
		myApplication.setSize(600, 600);

		// Muéstralo!
		myApplication.setVisible(true);
	}

	public void actionPerformed(ActionEvent e) {
		if (e.getSource() == miBoton) {
			miAreaDeTexto.setText("A button click");
			this.presionaBoton();
		} else if (e.getSource() == miCheckBox)
			miAreaDeTexto.setText("The checkbox state changed to "
					+ miCheckBox.isSelected());
		else
			miAreaDeTexto.setText("E ...?");
	}

	public void presionaBoton() {
		// add row dynamically into the table
		new Runner("C:\\RUBEN\\workspaceTest\\Pokemon\\bin\\IPs-MAV.txt",
				"C:\\RUBEN\\workspaceTest\\Pokemon\\bin\\CMDs-MAV.txt", dtm).start();
	}
}