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
class stack_manage(unittest.TestCase):

    def test_active_plugin(self):
        url = "http://"+ipaddr+":30000/api/plugin"
        data = config.get('json','stack_plugin')
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to active stack plugin"
        else:
            print "failed to active stack plugin"
        print "##################################"
        time.sleep(13)

    def test_add_stack(self):
        url = "http://"+ipaddr+":30000/service/stack/api/stack"
        data = config.get("json","add_stack")
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to add stack"
        else:
            print "failed to add stack"
        print "##################################"
        time.sleep(3)

    def test_del_stack(self):
        url = "http://"+ipaddr+":30000/service/stack/api/stack/delete"
        data = config.get("json","del_stack")
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to del stack"
        else:
            print "failed to del stack"
        print "##################################"

    def test_add_svc(self):
        url = "http://"+ipaddr+":30000/service/stack/api/app"
        data = config.get("json","add_svc")
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to add svc"
        else:
            print "failed to add svc"
        print "##################################"
        time.sleep(5)

    def test_update_port(self):
        url = "http://"+ipaddr+":30000/service/stack/api/app/service"
        data = config.get("json","update_port")
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to update port"
        else:
            print "failed to update port"
        print "##################################"

    def test_scale_num(self):
        url = "http://"+ipaddr+":30000/service/stack/api/app/scale"
        data = config.get("json","svc_scale")
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to scale svc"
        else:
            print "failed to scale svc"
        print "##################################"
        time.sleep(5)

    def test_svc_autoscale(self):
        url = "http://"+ipaddr+":30000/service/stack/api/app/autoscale"
        data = config.get("json","svc_autoscale")
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to config autoscale"
        else:
            print "failed to config autoscale"
        print "##################################"

    def test_close_autoscale(self):
        url = "http://"+ipaddr+":30000/service/stack/api/app/autoscale"
        data = config.get("json","close_autoscale")
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to close autoscale"
        else:
            print "failed to close autoscale"
        print "##################################"

    def test_del_svc(self):
        url = "http://"+ipaddr+":30000/service/stack/api/app/del"
        data = config.get("json","del_svc")
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to del svc"
        else:
            print "failed to del svc"
        print "##################################"

    def test_rollingupdate(self):
        url = "http://"+ipaddr+":30000/service/stack/api/app/rollupdate"
        data = config.get("json","rollupdate")
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to rollupdate"
        else:
            print "failed to rollupdate"
        print "##################################"
        time.sleep(5)

    def test_rollback(self):
        url = "http://"+ipaddr+":30000/service/stack/api/app/rollback"
        data = config.get("json","rollback")
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to rollback"
        else:
            print "failed to rollback"
        print "##################################"
        time.sleep(5)

    def test_create_balance(self):
        url = "http://"+ipaddr+":30000/service/stack/api/balance"
        data = config.get("json","add_balance")
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to add balance"
        else:
            print "failed to add balance"
        print "##################################"
        time.sleep(5)

    def test_del_balance(self):
        url = "http://"+ipaddr+":30000/service/stack/api/balance/del"
        data = config.get("json","add_balance")
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to del balance"
        else:
            print "failed to del balance"
        print "##################################"

    def test_add_rule(self):
        url = "http://"+ipaddr+":30000/service/stack/api/balance/add/httprule"
        data = config.get("json","add_httprule")
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to add httprule"
        else:
            print "failed to add httprule"
        print "##################################"

    def test_del_rule(self):
        url = "http://"+ipaddr+":30000/service/stack/api/balance//del/httprule"
        data = config.get("json","del_httprule")
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to del httprule"
        else:
            print "failed to del httprule"
        print "##################################"

if __name__ == '__main__':
    unittest.main()

