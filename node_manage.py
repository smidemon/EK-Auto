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
class node_manage(unittest.TestCase):

    def test_active_plugin(self):
        url = "http://"+ipaddr+":30000/api/plugin"
        data = config.get('json','node_plugin')
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to active node plugin"
        else:
            print "failed to active node plugin"
        print "##################################"
        time.sleep(10)

    def test_add_node(self):
        url = "http://"+ipaddr+":30000/service/node/api/node/install"
        data = config.get("json","add_node")
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to add node"
        else:
            print "failed to add node"
        print "##################################"

    def test_del_node(self):
        node = "node4"
        url = "http://192.168.10.152:30000/service/node/api/node/"+node
        response,code = ec.total(url=url,type="delete")
        if  200 <= code < 300:
            print "success to delete node"
        else:
            print "failed to delete node"
        print "##################################"

    def test_get_node(self):
        node_list,code = ec.get_all_node()
        if  200 <= code < 300:
            print "success to get all node"
            print "一共"+str(len(node_list))+"个主机"
            print node_list
        else:
            print "failed to get all node"
        print "##################################"

    def test_node_disable(self):
        node = "node5"
        url = "http://"+ipaddr+":30000/service/node/api/node/"+node+"/schedule/disable"
        response,code = ec.total(url=url,type="post")
        if  200 <= code < 300:
            print "success to close node label"
        else:
            print "failed to close node label"
        print "##################################"

    def test_node_enable(self):
        node = "node5"
        url = "http://"+ipaddr+":30000/service/node/api/node/"+node+"/schedule/enable"
        response,code = ec.total(url=url,type="post")
        if  200 <= code < 300:
            print "success to close node label"
        else:
            print "failed to close node label"
        print "##################################"

    def test_tenant_assign(self):
        node = "node3"
        url = "http://"+ipaddr+":30000/service/node/api/node/private/"+node
        param = "namespace=default"
        response,code = ec.total(url=url,param=param,type="put")
        if  200 <= code < 300:
            print "success to assign node to default"
        else:
            print "failed to assign node to default"
        print "##################################"

    def test_release_node(self):
        node = "node3"
        url = "http://"+ipaddr+":30000/service/node/api/node/private/apply"
        param = "namespace=default&allotNode="+node
        response,code = ec.total(url=url,param=param,type="delete")
        if  200 <= code < 300:
            print "success to release node from default"
        else:
            print "failed to release node from default"
        print "##################################"

if __name__ == '__main__':
    unittest.main()

