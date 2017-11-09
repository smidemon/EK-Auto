 # coding=utf-8
import unittest
import sys,os,json,urllib2
from crt_stk import EkOS
sys.path.insert(0,"D:\PY_project\EkOS_Test")
from storage import storage
from image_manage import imageManage
from auth import cetfAuth
from tenant import tenant
from node_manage import node_manage
from network import network
from stack_manage import stack_manage
# ec = EkOS()
suite = unittest.TestSuite()
#存储管理
# suite.addTest(storage("test_active_plugin"))
# suite.addTest(storage("test_add_nfs"))
# suite.addTest(storage("test_add_ceph"))
# suite.addTest(storage("test_add_nfsvm"))
# suite.addTest(storage("test_add_cephvm"))
# suite.addTest(storage("test_ifdel_storage"))
# suite.addTest(storage("test_del_nfsvm"))
# suite.addTest(storage("test_del_cephvm"))
# suite.addTest(storage("test_del_ceph"))
# suite.addTest(storage("test_del_nfs"))
# suite.addTest(storage("test_del_plugin"))

#认证授权
# suite.addTest(cetfAuth("test_add_user"))
# suite.addTest(cetfAuth("test_get_users"))
# suite.addTest(cetfAuth("test_add_groups"))
# suite.addTest(cetfAuth("test_get_groups"))
# suite.addTest(cetfAuth("test_get_groups1"))
# suite.addTest(cetfAuth("test_start_SMTP"))
# suite.addTest(cetfAuth("test_stop_SMTP"))
# suite.addTest(cetfAuth("test_ping_smtp"))
# suite.addTest(cetfAuth("test_config_smtp"))
# suite.addTest(cetfAuth("test_start_LDAP"))
# suite.addTest(cetfAuth("test_stop_LDAP"))
# suite.addTest(cetfAuth("test_ping_ldap_WinAD"))
# suite.addTest(cetfAuth("test_config_ldap_WinAD"))
# suite.addTest(cetfAuth("test_ping_ldap_openLD"))
# suite.addTest(cetfAuth("test_config_ldap_openLD"))
# suite.addTest(cetfAuth("test_del_user"))

#镜像管理
# suite.addTest(imageManage("test_active_plugin"))
# suite.addTest(imageManage("test_add_pri_registry"))
# suite.addTest(imageManage("test_add_pub_registry"))
# suite.addTest(imageManage("test_del_registry"))
# suite.addTest(imageManage("test_del_pri_img"))
# suite.addTest(imageManage("test_get_img"))
# suite.addTest(imageManage("test_get_reg"))
# suite.addTest(imageManage("test_upload_img"))
# suite.addTest(imageManage("test_edit_manager"))

#多租户
# suite.addTest(tenant("test_active_plugin"))
# suite.addTest(tenant("test_add_tenant"))
# suite.addTest(tenant("test_admin_off"))
# suite.addTest(tenant("test_admin_on"))
# suite.addTest(tenant("test_edit_quota"))
# suite.addTest(tenant("test_set_default_quota"))

#主机
# suite.addTest(node_manage("test_active_plugin"))
# suite.addTest(node_manage("test_add_node"))
# suite.addTest(node_manage("test_get_node"))
# suite.addTest(node_manage("test_node_disable"))
# suite.addTest(node_manage("test_node_enable"))
# suite.addTest(node_manage("test_tenant_assign"))
# suite.addTest(node_manage("test_release_node"))

#应用管理
# suite.addTest(stack_manage("test_active_plugin"))
# suite.addTest(stack_manage("test_add_stack"))
# suite.addTest(stack_manage("test_del_stack"))
# suite.addTest(stack_manage("test_add_svc"))
# suite.addTest(stack_manage("test_update_port"))
# suite.addTest(stack_manage("test_scale_num"))
# suite.addTest(stack_manage("test_svc_autoscale"))
# suite.addTest(stack_manage("test_close_autoscale"))
# suite.addTest(stack_manage("test_rollingupdate"))
suite.addTest(stack_manage("test_rollback"))
# suite.addTest(stack_manage("test_del_svc"))
# suite.addTest(stack_manage("test_create_balance"))
# suite.addTest(stack_manage("test_add_rule"))
# suite.addTest(stack_manage("test_del_rule"))
# suite.addTest(stack_manage("test_del_balance"))

#网络管理
# suite.addTest(network("test_active_plugin"))
# suite.addTest(network("test_add_ippool"))

# print suite
if __name__ == '__main__':
    unittest.main(defaultTest='suite')

