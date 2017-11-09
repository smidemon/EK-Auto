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
class cetfAuth(unittest.TestCase):

    def test_add_user(self):
        url = "http://"+ipaddr+":30000/service/auth/api/users"
        data = config.get("json","add_user")
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to add user"
        else:
            print "failed to add user"
        print "##################################"

    def test_get_users(self):
        user_list,code = ec.get_all_user()
        if  200 <= code < 300:
            print "success to get all user"
            print "一共"+str(len(user_list))+"个用户"
            print user_list
        else:
            print "failed to get all user"
        print "##################################"

    def test_add_groups(self):
        url = "http://"+ipaddr+":30000/service/auth/api/groups"
        data = config.get("json","add_groups")
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to add group"
        else:
            print "failed to add group"
        print response
        print "##################################"

    def test_get_groups(self):
        group_list,code = ec.get_all_group()
        if  200 <= code < 300:
            print "success to get all group"
            print "管理模式下一共"+str(len(group_list))+"个群组"
            print group_list
        else:
            print "failed to get all group"
        print "##################################"

    def test_get_groups1(self):
        group_list,code = ec.get_all_group(False)
        if  200 <= code < 300:
            print "success to get all group"
            print "租户模式下一共"+str(len(group_list))+"个群组"
            print group_list
        else:
            print "failed to get all group"
        print "##################################"

    def test_start_SMTP(self):
        url = "http://"+ipaddr+":30000/service/auth/api/configurations"
        data = config.get("json","start_smtp")
        response,code = ec.total(url=url,data=data,type="put")
        if  200 <= code < 300:
            print "success to start smtp"
        else:
            print "failed to start smtp"
        print "##################################"

    def test_stop_SMTP(self):
        url = "http://"+ipaddr+":30000/service/auth/api/configurations"
        data = config.get("json","stop_smtp")
        response,code = ec.total(url=url,data=data,type="put")
        if  200 <= code < 300:
            print "success to stop smtp"
        else:
            print "failed to stop smtp"
        print "##################################"

    def test_ping_smtp(self):
        url = "http://"+ipaddr+":30000/service/auth/api/email/ping"
        data = config.get("json","ping_smtp")
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to ping smtp"
        else:
            print "failed to ping smtp"
        print "##################################"

    def test_config_smtp(self):
        url = "http://"+ipaddr+":30000/service/auth/api/configurations"
        data = config.get("json","config_smtp")
        response,code = ec.total(url=url,data=data,type="put")
        if  200 <= code < 300:
            print "success to config smtp"
        else:
            print "failed to config smtp"
        print "##################################"

    def test_start_LDAP(self):
        url = "http://"+ipaddr+":30000/service/auth/api/configurations"
        data = config.get("json","start_ldap")
        response,code = ec.total(url=url,data=data,type="put")
        if  200 <= code < 300:
            print "success to start smtp"
        else:
            print "failed to start smtp"
        print "##################################"

    def test_stop_LDAP(self):
        url = "http://"+ipaddr+":30000/service/auth/api/configurations"
        data = config.get("json","stop_ldap")
        response,code = ec.total(url=url,data=data,type="put")
        if  200 <= code < 300:
            print "success to stop smtp"
        else:
            print "failed to stop smtp"
        print "##################################"

    def test_ping_ldap_WinAD(self):
        url = "http://"+ipaddr+":30000/service/auth/api/ldap/ping"
        data = config.get("json","ping_ldap_winAD")
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to ping ldap_windowsAD"
        else:
            print "failed to ping ldap_windowsAD"
        print "##################################"

    def test_config_ldap_WinAD(self):
        url = "http://"+ipaddr+":30000/service/auth/api/configurations"
        data = config.get("json","config_ldap_winAD")
        response,code = ec.total(url=url,data=data,type="put")
        if  200 <= code < 300:
            print "success to config ldap_windowsAD"
        else:
            print "failed to config ldap_windowsAD"
        print "##################################"

    def test_ping_ldap_openLD(self):
        url = "http://"+ipaddr+":30000/service/auth/api/ldap/ping"
        data = config.get("json","ping_ldap_openLD")
        response,code = ec.total(url=url,data=data,type="post")
        if  200 <= code < 300:
            print "success to ping ldap_openLD"
        else:
            print "failed to ping ldap_openLD"
        print "##################################"

    def test_config_ldap_openLD(self):
        url = "http://"+ipaddr+":30000/service/auth/api/configurations"
        data = config.get("json","config_ldap_openLD")
        response,code = ec.total(url=url,data=data,type="put")
        if  200 <= code < 300:
            print "success to config ldap_openLD"
        else:
            print "failed to config ldap_openLD"
        print "##################################"

    def test_del_user(self):
        url = "http://"+ipaddr+":30000/service/auth/api/users/10003"
        param = "namespace=default"
        response,code = ec.total(url=url,param=param,type="delete")
        if  200 <= code < 300:
            print "success to delete user bbbb"
        else:
            print "failed to delete user bbbb"
        print "##################################"



if __name__ == '__main__':
    unittest.main()

