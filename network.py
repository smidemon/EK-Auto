 # coding=utf-8
from crt_stk import EkOS
import sys,json,time
import ConfigParser
import unittest
sys.path.insert(0,"D:\PY_project\EkOS_Test")

config = ConfigParser.ConfigParser()
config.readfp(open("config.ini"))
ipaddr = config.get("main","ipaddr")
ec = EkOS()
class network(unittest.TestCase):

    def test_active_plugin(self):
        url = "http://"+ipaddr+":30000/api/plugin"
        data = config.get('json','network_plugin')
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to active network plugin"
        else:
            print "failed to active network plugin"
        print "##################################"

    def test_add_ippool(self):
        url = "http://"+ipaddr+":30000/service/network/api/ip_pool/add"
        data = config.get('json','network_data')
        print data
        # headers = config.get("json","network_head")
        response,code = ec.total2(url=url,data=data,type="POST")
        if  200 <= code < 300:
            print "success to add ippool"
        else:
            print "failed to add ippool"
        print "##################################"



if __name__ == '__main__':
    unittest.main()

