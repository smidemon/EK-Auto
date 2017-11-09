 # coding=utf-8
from crt_stk import EkOS
import sys,time
import ConfigParser
import unittest
sys.path.insert(0,"D:\PY_project\EkOS_Test")

config = ConfigParser.ConfigParser()
config.readfp(open("config.ini"))
ipaddr = config.get("main","ipaddr")
ec = EkOS()
class storage(unittest.TestCase):

    def test_active_plugin(self):
        url = "http://"+ipaddr+":30000/api/plugin"
        data = config.get('json','store_plugin')
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to active storage plugin"
        else:
            print "failed to active storage plugin"
        print "##################################"
        time.sleep(12)

    def test_add_nfs(self):
        url = "http://"+ipaddr+":30000/service/storage/api/storage"
        param = "pluginname=storage"
        data = config.get('json','add_nfs_json')
        # print data
        response,code = ec.total(url=url,param=param,data=data,type="post")
        if  200 <= code < 300:
            print "success to add nfs storage"
        else:
            print "failed to add nfs storage"
        print "##################################"

    def test_add_ceph(self):
        url = "http://"+ipaddr+":30000/service/storage/api/storage"
        param = "pluginname=storage"
        data = config.get('json','add_ceph_json')
        # print data
        response,code = ec.total(url=url,param=param,data=data,type="post")
        if  200 <= code < 300:
            print "success to add ceph storage"
        else:
            print "failed to add ceph storage"
        print "##################################"
        time.sleep(12)

    def test_add_nfsvm(self):
        url = "http://"+ipaddr+":30000/service/storage/api/storage/pvc"
        param = "pluginname=storage"
        data = config.get('json','add_nfsvm_json')
        # print data
        response,code = ec.total(url=url,param=param,data=data,type="post")
        if  200 <= code < 300:
            print "success to add nfs volumn"
        else:
            print "failed to add nfs volumn"
        print "##################################"

    def test_add_cephvm(self):
        url = "http://"+ipaddr+":30000/service/storage/api/storage/pvc"
        param = "pluginname=storage"
        data = config.get('json','add_cephvm_json')
        # print data
        response,code = ec.total(url=url,param=param,data=data,type="post")
        if  200 <= code < 300:
            print "success to add ceph volumn"
        else:
            print "failed to add ceph volumn"
        print "##################################"
        time.sleep(3)

    def test_ifdel_storage(self):
        code = ec.get_story_count()
        if  200 <= code < 300:
            print "Successfully know whether the storage can be deleted"
        else:
            print "failed know whether the storage can be deleted"
        print "##################################"

    def test_del_nfsvm(self):
        nfsvm_name = config.get("json","nfsvm_name")
        url = "http://"+ipaddr+":30000/service/storage/api/storage/pvc/"+nfsvm_name
        param = "pluginname=storage&namespace=default"
        response,code = ec.total(url=url,param=param,type="delete")
        if  200 <= code < 300:
            print "success to delete nfs volumn"
        else:
            print "failed to delete nfs volumn"
        print "##################################"

    def test_del_cephvm(self):
        cephvm_name = config.get("json","cephvm_name")
        url = "http://"+ipaddr+":30000/service/storage/api/storage/pvc/"+cephvm_name
        param = "pluginname=storage&namespace=default"
        response,code = ec.total(url=url,param=param,type="delete")
        if  200 <= code < 300:
            print "success to delete ceph volumn"
        else:
            print "failed to delete ceph volumn"
        print "##################################"
        time.sleep(3)

    def test_del_ceph(self):
        ceph_name = config.get("json","ceph_name")
        url = "http://"+ipaddr+":30000/service/storage/api/storage/"+ceph_name
        param = "pluginname=storage&namespace=default"
        response,code = ec.total(url=url,param=param,type="delete")
        if  200 <= code < 300:
            print "success to delete ceph storage"
        else:
            print "failed to delete ceph storage"
        print "##################################"

    def test_del_nfs(self):
        nfs_name = config.get("json","nfs_name")
        url = "http://"+ipaddr+":30000/service/storage/api/storage/"+nfs_name
        param = "pluginname=storage&namespace=default"
        response,code = ec.total(url=url,param=param,type="delete")
        if  200 <= code < 300:
            print "success to delete nfs storage"
        else:
            print "failed to delete nfs storage"
        print "##################################"
        time.sleep(3)

    def test_del_plugin(self):
        url = "http://"+ipaddr+":30000/api/plugin/del"
        data = config.get("json","store_plugin")
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to delete storage plugin"
        else:
            print "failed to delete storage plugin"
        print "##################################"

if __name__ == '__main__':
    unittest.main()

