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
class tenant(unittest.TestCase):

    def test_active_plugin(self):
        url = "http://"+ipaddr+":30000/api/plugin"
        data = config.get('json','tenant_plugin')
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to active tenant plugin"
        else:
            print "failed to active tenant plugin"
        print "##################################"
        time.sleep(10)

    def test_admin_off(self):
        url = "http://"+ipaddr+":30000/profile/"
        param = "admin=off&current=default"
        response,code = ec.total(url=url,param=param,type="get")
        if  200 <= code < 300:
            print "success to Switch to tenant mode"
        else:
            print "failed to Switch to tenant mode"
        print "##################################"

    def test_admin_on(self):
        url = "http://"+ipaddr+":30000/profile/"
        param = "admin=on&current=default"
        response,code = ec.total(url=url,param=param,type="get")
        if  200 <= code < 300:
            print "success to Switch to manage mode"
        else:
            print "failed to Switch to manage mode"
        print "##################################"

    def test_add_tenant(self):
        url = "http://"+ipaddr+":30000/service/tenant/api/tenant"
        data = config.get("json","add_tenant")
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to add tenant"
        else:
            print "failed to add tenant"
        print "##################################"

    def test_edit_quota(self):
        url = "http://"+ipaddr+":30000/service/tenant/api/quota"
        data = config.get("json","edit_quota")
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to edit quota"
        else:
            print "failed to edit quota"
        print "##################################"

    def test_set_default_quota(self):
        url = "http://"+ipaddr+":30000/service/tenant/api/quota/default"
        data = config.get("json","set_default_quota")
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to set default quota"
        else:
            print "failed to set default quota"
        print "##################################"

    def test_del_tenant(self):
        pass




if __name__ == '__main__':
    unittest.main()

