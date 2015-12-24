import sys, httplib

HOST = sys.argv[1]
PORT = 8080
API_URL = '/mav-core-war/ws/mavCommManager'

def do_request(xml_location):
        """HTTP XML Post requeste"""
        request = open(xml_location,"r").read()
        webservice = httplib.HTTP(HOST,PORT)
        webservice.putrequest("POST", API_URL)
        webservice.putheader("Host", HOST)
        webservice.putheader("User-Agent","Python post")
        webservice.putheader("Content-type", "text/xml; charset=\"UTF-8\"")
        webservice.putheader("Content-length", "%d" % len(request))
        webservice.endheaders()
        webservice.send(request)
        statuscode, statusmessage, header = webservice.getreply()
        result = webservice.getfile().read()
        print statuscode, statusmessage, header
        print result

do_request(sys.argv[2])

