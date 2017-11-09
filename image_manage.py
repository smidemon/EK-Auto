 # coding=utf-8
from crt_stk import EkOS
import sys,json,time
import ConfigParser
import unittest,random
sys.path.insert(0,"D:\PY_project\EkOS_Test")

config = ConfigParser.ConfigParser()
config.readfp(open("config.ini"))
ipaddr = config.get("main","ipaddr")
ec = EkOS()
class imageManage(unittest.TestCase):

    def test_active_plugin(self):
        plugin_list = {}
        url = "http://"+ipaddr+":30000/api/plugin"
        data = config.get('json','registry_plugin')
        plugin_list = data.split(',')
        for i in plugin_list:
            data = json.loads(i)
            response,code = ec.total(url=url,data=i,type="post")
            if 200<= code < 300:
                print response
            else:
                print "failed to active registry plugin"
            print "##################################"
            time.sleep(10)

    def get_reg_id(self):
        reg_list = dict()
        url = "http://"+ipaddr+":30000/service/registry/api/projects"
        param = "page=1&page_size=10&project_name=&is_public=0&type=8"
        response,code = ec.total(url=url,param=param,type="get")
        response = json.loads(response)
        for i in response:
            name = i["name"]
            id = i["project_id"]
            reg_list[name] = id
        return reg_list


    def test_add_pri_registry(self):
        url = "http://"+ipaddr+":30000/service/registry/api/projects"
        data = config.get('json','add_priregistry_json')
        # print data
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to add primary registry"
        else:
            print "failed to add primary registry"
        print "##################################"

    def test_add_pub_registry(self):
        url = "http://"+ipaddr+":30000/service/registry/api/projects"
        data = config.get('json','add_pubregistry_json')
        # print data
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to add public registry"
        else:
            print "failed to add public registry"
        print "##################################"

    # 删除所有除default和library以外的仓库
    def test_del_registry(self):
        reg_list = self.get_reg_id()
        names = reg_list.keys()
        for i in names:
            if i != "default" and i != "library":
                id = reg_list[i]
                url = "http://"+ipaddr+":30000/service/registry/api/projects/"+str(id)
                response,code = ec.total(url=url,type="delete")
                if code == 200:
                    print "success to del pub registry"
                else:
                    print "failed to del pub registry"
        print "##################################"

    # 删除私有镜像
    def test_del_pri_img(self):
        img_name = config.get("json","img_name")
        url = "http://"+ipaddr+":30000/service/registry/api/repositories/"+img_name+"/tags/"
        param = "tag=latest"
        response,code = ec.total(url=url,param=param,type="delete")
        if code == 200:
            print "success to del pri img"
        else:
            print "failed to del pri img"
        print "##################################"

    def test_get_img(self):
        img_list,code = ec.get_all_image()
        if  200 <= code < 300:
            print "success to get all image"
            print "一共"+str(len(img_list))+"个镜像"
            print img_list
        else:
            print "failed to get all image"
        print "##################################"

    def test_get_reg(self):
        reg_list,code = ec.get_all_reg()
        if  200 <= code < 300:
            print "success to get all registry"
            print "一共"+str(len(reg_list))+"个仓库"
            print reg_list
        else:
            print "failed to get all registry"
        print "##################################"

    def test_upload_img(self):
        url = "http://"+ipaddr+":30000/service/ci/upload"
        response,code = ec.total2()
        # if  200 <= code < 300:
        #     print "success to upload img"
        # else:
        #     print "failed to upload img"
        print response
        print "##################################"

    def test_edit_manager(self):
        flag = ec.get_reg_type()
        num = random.randrange(2)
        if num == 0:
            data = config.get("json","admin_id")
        else:
            data = config.get("json","edit_info")
        if flag:
            print num
            url = "http://"+ipaddr+":30000/service/auth/api/projects/7"
            response,code = ec.total(url=url,data=data,type="put")
            if 200<= code < 300:
                print "success to edit reg manager or info "
            else:
                print "failed to edit reg manager or info "
            print "##################################"
        else:
            print "此仓库不存在或不能修改管理员为admin"
            print "##################################"

if __name__ == '__main__':
    unittest.main()

