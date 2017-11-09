#coding=utf-8
import requests,json,time
import cookielib,re,ConfigParser
import urllib2,urllib,sys
sys.path.insert(0,"D:\PY_project\EkOS_Test")

config = ConfigParser.ConfigParser()
config.readfp(open("config.ini"))
ipaddr = config.get("main","ipaddr")
class EkOS:
    #登陆并获取cookie
    def __init__(self):
        self.all_cookie = ""
        url = "http://"+ipaddr+":30000/login"
        data = urllib.urlencode({'username':'admin','password':'admin12345'})
        mycookie = cookielib.CookieJar()#生成cookie对象
        handler = urllib2.HTTPCookieProcessor(mycookie) #利用urllib2库中的HTTPCookieProcessor来声明一个处理cookie的处理器
        self.opener = urllib2.build_opener(handler) #利用handler来构造opener，opener的用法和urlopen()类似
        response = self.opener.open(url,data)#opener返回的一个应答对象response
        # print response.read()
        for index,cookie in enumerate(mycookie):
            tmp = cookie.name + "=" + cookie.value + "; "
            self.all_cookie += tmp
        # return opener
        # print self.all_cookie

    #数据处理模块，根据提供的url、param、data发送请求，并返回响应
    #自动化测试所用方法--没有转换数据格式
    def total(self,url,param=None,data=None,type=None):
        # global response
        # opener = self.login()
        type = type.upper()
        # print type
        headers = {'Content-Type':'application/json'}
        datas = data
        if param != None:
            newurl = url + "?" + param
            print newurl
        else:
            newurl = url
        try:
            '''
            if type == "post":
                request = urllib2.Request(url=newurl,headers=headers,data=datas)
                response = self.opener.open(request)

            elif type == "put":
                request = urllib2.Request(url=newurl,headers=headers,data=datas)
                request.get_method = lambda: 'PUT'
                response = self.opener.open(request)

            elif type == "delete":
                request = urllib2.Request(url=newurl,headers=headers,data=datas)
                request.get_method = lambda: 'DELETE'
                response = self.opener.open(request)

            else:
                response = self.opener.open(url=newurl,headers=headers,data=datas)
            '''
            request = urllib2.Request(url=newurl,headers=headers,data=datas)
            request.get_method = lambda : type
            response = self.opener.open(request)
            return response.read(),response.code
        except Exception as e:
            print e

    def total1(self,url,param=None,data=None,type=None):
        # global response
        # opener = self.login()
        type = type.upper()
        headers = {'Content-Type':'application/json'}
        # datas = urllib.urlencode(data)
        datas = json.dumps(data)
        if param != None:
            newurl = url + "?" + param
        else:
            newurl = url
        try:
            '''
            if type == "post":
                request = urllib2.Request(url=newurl,headers=headers,data=datas)
                response = self.opener.open(request)
            elif type == "put":
                request = urllib2.Request(newurl)
                request.get_method = lambda: 'PUT'
                response = self.opener.open(request)
            elif type == "delete":
                request = urllib2.Request(newurl)
                request.get_method = lambda: 'DELETE'
                response = self.opener.open(request)
            else:
                response = self.opener.open(newurl)
            '''

            request = urllib2.Request(url=newurl,headers=headers,data=datas)
            request.get_method = lambda : type
            response = self.opener.open(request)
            return response.read(),response.code
        except Exception as e:
            print e

    def total2(self,url=None,data=None,type=None):
        # url = "http://192.168.22.3:30000/service/network/api/ip_pool/add"
        # data = data.strip('"')
        # print data
        data = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"lable\"\r\n\r\nnet\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ips\"\r\n\r\n172.168.0.1/24\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'cache-control': "no-cache",
            'postman-token': "aa5851e0-3dce-9be2-d5ee-1f68b8d970e2",
            'Cookie':self.all_cookie
              }
        try:
            # response = requests.post(url=url, data=data, headers=headers)
            # return response.text
            request = urllib2.Request(url=url,headers=headers,data=data)
            request.get_method = lambda : type
            response = self.opener.open(request)
            return response.read(),response.code
        except Exception as e:
            print e

    #获取所有的日志
    def logging(self,ip,app_name,svc_name,time,query_name):
        # opener = login()
        apps = app_name
        svc = svc_name
        query = query_name
        url = "http://"+ipaddr+":30000/service/logging/api/logs?" \
              "namespace=default&index=filebeat-*-"+str(time)+ \
              "&page=1&size=100&application="+str(apps) \
        + "&service=" + str (svc) + "&pod=&containerID=&query=" + str(query)
        # "http://192.168.22.3:30000/service/logging/api/logs?namespace=default&index=filebeat-6.0.0-beta1-2017.08.31&page=1&size=100&application=test3&service=app-1&pod=&containerID=&query="
        # response = get_cookie(ip,url)
        # global opener
        # response = opener.open(url)  #获取新地址的内容（现在只针对get请求，post请求暂未作处理）
        response,code = self.total1(url=url,type="get")
        #opener.open()
        print response
        return response#将响应内容以文本的形式返回

    #正则表达式，匹配满足条件的所有日志
    def regulation(response):
        pattern = re.compile(u'_source.*?log":"(.*?)",',re.IGNORECASE)
        #变量pattern实现存储所有满足条件的记录；re.IGNORECASE忽略大小写；中间部分则是匹配规则，截取名为log中的内容
        #re.compile  正则表达式的匹配函数
        return pattern   #返回结果集

    def plugin_active(self):
        url = "http://"+ipaddr+":30000/api/plugin"
        # ,{"name":"stack"},{"name":"network"},{"name":"network"},{"name":"network"},{"name":"network"}
        data = [{"name":"ci"},{"name":"tenant"},{"name":"logging"},{"name":"stack"},{"name":"appstore"},{"name":"node"},{"name":"storage"},{"name":"registry"},{"name":"monitor"},{"name":"network"}]
        for i in data:
            try:
                print i
                response = self.total1(url=url,data=i,type="post")
                print response
            except:
                print "failed to active"

    #申请主机
    def apply_host(self):
        url = "http://"+ipaddr+":30000/service/node/api/node/private/apply"
        param = "namespace=default"
        response = self.total1(url=url,param=param,type="put")
        print response

    #创建应用栈
    def create_stack(self,stc_name):
        url = "http://"+ipaddr+":30000/service/stack/api/stack"
        data = {"name":stc_name,"ippool":"","namespace":"default"}
        response = self.total1(url=url,data=data,type="post")
        print response

    #创建服务
    def create_svc(self,app_name,stc_name):
        url = "http://"+ipaddr+":30000/service/stack/api/app"
        data = {"name":app_name,"namespace":"default","stack":stc_name,"stateful":"none","replicas":1,"cpu":125,"memory":64,"diskSize":20000,"collectLog":True,"scheduler":None,"containers":[{"name":"cccc","image":"registry.ekos.local/library/hello:latest","command":"","stdin":False,"tty":False,"envs":[],"healthCheck":None,"cfgFileMounts":[],"secretMounts":[],"hostMounts":[],"volumes":[],"cpuPercent":100,"memPercent":100}],"service":{"ports":[]},"desc":""}
        response = self.total1(url=url,data=data,type="post")
        # print response.code
        print response

    #获取所有服务
    def get_all_app(self):
        stack_list = []
        app_list = []
        url = "http://"+ipaddr+":30000/service/stack/api/stack"
        param = "namespace=default&page=1&itemsPerPage=1000000"
        response,code = self.total1(url=url,param=param,type="get")
        response = json.loads(response)
        obj = response["stacks"]
        if len(obj) > 0:
            for i in range(len(obj)):
                stack_list.append(obj[i])
            for i in stack_list:
                if len(i["apps"]) > 0:
                    for j in range(len(i["apps"])):
                        app_list.append(i["apps"][j]["name"])
                else:
                    continue
        else:
            print "no any stack"
        return app_list


    def delete_stack(self,name):
        url = "http://"+ipaddr+":30000/service/stack/api/stack/delete"
        data = {"name":name,"namespace":"default"}
        response = self.total1(url=url,data=data,type="post")
        print response


    def delete_svc(self,app_name):
        url = "http://"+ipaddr+":30000/service/stack/api/app/del"
        data = {"name":app_name,"namespace":"default"}
        response,code = self.total1(url=url,data=data,type="post")
        if response != None:
            if "success" in response:
                print response
                print "success to delete svc"
            else:
                print "出现异常"
        else:
            print "send the post request is fail"

    def add_store(self):
        url = "http://"+ipaddr+":30000/service/storage/api/storage"
        param = "pluginname=storage"
        data = {"storage_type":"nfs","storage_name":"etcd3","nfs_server":"192.168.22.7","nfs_path":"/nfs","read_only":"false"}
        response = self.total1(url=url,param=param,data=data,type="post")
        print response

    def add_volumn(self):
        url = "http://"+ipaddr+":30000/service/storage/api/storage/pvc"
        param = "pluginname=storage"
        data = {"storage_name":"etcd3","pvc_name":"volumn2","access_modes":"ReadWriteMany","quantity":"1Mi"}
        response = self.total1(url=url,param=param,data=data,type="post")
        print response

    #删除存储
    def delete_store(self,store_name):

        url = "http://"+ipaddr+":30000/service/storage/api/storage/"+str(store_name)
        print url
        param = "pluginname=storage"
        response = self.total1(url=url,param=param,type="delete")
        print response

    #删除存储卷
    def delete_volumn(self,volumn_name):
        url = "http://"+ipaddr+":30000/service/storage/api/storage/pvc/"+str(volumn_name)
        param = "pluginname=storage"
        print url
        response,code = self.total1(url=url,param=param,type="delete")
        print response

    def add_alert(self):
        url = "http://"+ipaddr+":30000/service/monitor/api/addalert"
        data = {"alertName":"aaaa","alertModule":"服务","alertTarget":"app-1","relationTarget":"1","alertRule":[{"alertItem":"CPU使用率(%)|总合","alertThreshold":">|10"}]}
        response = self.total1(url=url,data=data,type="post")
        print response

    #添加报警组
    def add_relation(self):
        url = "http://"+ipaddr+":30000/service/monitor/api/addrelation"
        param = "description=ddss&email=fengqianjun@ghostcloud.cn&phone=15555555555&name=dddd&url=http://www.baidu.com"
        response = self.total1(url=url,param=param,type="get")
        print response

    #配置SMTP
    def SMTP_config(self):
        url = "http://"+ipaddr+":30000/service/monitor/api/changeemailandwebhook"
        data = {"resolve_timeout":"5m","smtp_auth_password":"password","smtp_auth_username":"weijunxu@ghostcloud.cn","smtp_from":"weijunxu@ghostcloud.cn","smtp_smarthost":"smtp.ym.163.com:465"}
        response = self.total1(url=url,data=data,type="post")
        print response



    def get_status(self):
        url = "http://"+ipaddr+":30000/service/stack/api/stack/detail"
        param = "namespace=default&name=test1"
        response,code = self.total1(url=url,param=param,type="get")

        print response
        print type(code),code

    def quck_deploy(self,name):
        url = "http://"+ipaddr+":30000/service/appstore/api/appset"
        param = "tpl=nginx&namespace=default"
        name = "nginx-"+str(name)
        data = {"name":name,"ippool":"","desc":"通过应用模板nginx部署的应用","namespace":"default","apps":[{"name":"app","namespace":"","stack":"","type":"","desc":"","replicas":1,"cpu":125,"memory":64,"collectLog":True,"diskSize":20000,"scheduler":None,"service":{"ports":[]},"containers":[{"name":"cccc","image":"registry.ekos.local/library/hello:latest","command":"","envs":[],"logDir":"","healthCheck":None,"persistentVolumeClaims":None,"cpuPercent":100,"memPercent":100,"stdin":False,"tty":False,"cfgFileMounts":[],"secretMounts":[],"volumes":[],"hostMounts":[]}],"autoScale":{"minReplicas":0,"maxReplicas":0,"targetCPUPercentage":0},"stateful":"none","usePrivateNode":False,"volumes":[]}]}
        response,code = self.total1(url=url,param=param,data=data,type="post")
        print response

    def get_reg_id(self):
        reg_list = dict()
        url = "http://"+ipaddr+":30000/service/registry/api/projects"
        param = "page=1&page_size=10&project_name=&is_public=0&type=8"
        response,code = ec.total1(url=url,param=param,type="get")
        response = json.loads(response)
        for i in response:
            name = i["name"]
            id = i["project_id"]
            reg_list[name] = id
        return reg_list

    # 获取所有镜像
    def get_all_image(self):
        img_list = []
        url = "http://"+ipaddr+":30000/service/registry/api/repositories"
        param = "page=1&page_size=10&project_id=0&q=&detail=1"
        response,code = self.total1(url=url,param=param,type="get")
        response = json.loads(response)
        for i in response:
            if len(i["tags"]) > 1:
                for j in i["tags"]:
                    img = str(i["domain"])+"/"+str(i["repository_name"])+":"+str(j)
                    img_list.append(img)
            else:
                img = str(i["domain"])+"/"+str(i["repository_name"])+":"+str(i["tags"][0])
                img_list.append(img)
        return img_list,code

    #获取所有的镜像仓库
    def get_all_reg(self):
        reg_list = []
        url = "http://"+ipaddr+":30000/service/registry/api/projects"
        param = "page=1&page_size=10&project_name=&is_public=0&type=8"
        response,code = self.total1(url=url,param=param,type="get")
        response = json.loads(response)
        for i in response:
            reg_list.append(str(i["name"]))
        return reg_list,code

    # 获取仓库的操作日志
    def get_reg_log(self,pro_id):
        url = "http://"+ipaddr+":30000/service/auth/api/projects/"+str(pro_id)+"/logs/filter"
        param = "page=1&page_size=10"
        data = {}
        response,code = ec.total1(url=url,param=param,data=data,type="post")
        response = json.loads(response)
        for i in response:
            print i

    # 获取存储是否可以删除（是否有存储卷）
    def get_story_count(self):
        url = "http://"+ipaddr+":30000/service/storage/api/storage"
        param = "page=1&itemsPerPage=10&pluginname=storage&namespace=default"
        response,code = self.total1(url=url,param=param,type="get")
        response = json.loads(response)
        for i in response["items"]:
            name = i["type"]
            if i["volume_count"] != 0:
                print "is not able to delete "+name+" storage"
            else:
                print "be able to delete "+name+" storage"
        return code

    #获取所有的主机信息
    def get_all_node(self):
        node_list = []
        url = "http://"+ipaddr+":30000/service/node/api/node"
        param = "page=1&itemsPerPage=10000&type=node"
        response,code = self.total1(url=url,param=param,type="get")
        response = json.loads(response)
        response = response["nodes"]["nodes"]
        for i in response:
            node_list.append(str(i["status"]["addresses"][0]["address"]))
        return node_list,code

    def get_all_user(self):
        user_list = []
        url = "http://"+ipaddr+":30000/service/auth/api/users"
        param = "username=&page=1&page_size=10"
        response,code = self.total1(url=url,param=param,type="get")
        response = json.loads(response)
        for i in response:
            user_list.append(str(i["username"]))
        return user_list,code
        # print user_list

    #分别获取管理模式和租户模式下所有的群组信息
    def get_all_group(self,is_admin=True):
        group_list = []
        url = "http://"+ipaddr+":30000/service/auth/api/groups"
        if is_admin:
            param = "project_id=0&user_id=0"
        else:
            param = "project_id=6&user_id=0"
        response,code = self.total1(url=url,param=param,type="get")
        response = json.loads(response)
        for i in response:
            group_list.append(str(i["name"]))
        return group_list,code
        # print group_list

    def get_reg_type(self):
        url = "http://"+ipaddr+":30000/service/registry/api/projects"
        param = "page=1&page_size=10&project_name=&is_public=0&type=8"
        response,code = self.total1(url=url,param=param,type="get")
        response = json.loads(response)
        for index,i in enumerate(response):
            if i["project_id"] == 7:
                if i["type"] == 9:
                    return True
                else:
                    return False
            else:
                continue
        return False

if __name__ == "__main__":
    ec = EkOS()
    # ec.get_all_group(True)
    # ec.get_all_node()
    ec.total2()
    # print ec.get_reg_type()
    # ec.get_all_reg()
    # ec.login()
    # ec.get_story_count()
    # ec.delete_svc("hello")
    # ec.get_story_count()
    # 获取仓库ID
    '''
    list = ec.get_reg_id()
    for i in list:
        if i != "default" and i != "library":
            print list[i]
    '''
    # print(ec.get_all_image())
    # ec.get_reg_log(1)
    # plugin_active()   #激活插件
    # create_stack("hellos")    #创建应用栈
    # time.sleep(3)
    # create_svc()      #创建服务
    # get_status()        #GET请求
    # delete_svc()        #删除服务
    # delete_stack()       #删除应用栈
    # add_store()         #添加存储
    # time.sleep(5)
    # add_volumn()       #添加存储卷
    # delete_volumn("volumn2")#删除存储卷
    # delete_store("etcd3")  #删除存储
    # apply_host()     #提交主机申请
    # add_alert()       #添加报警通知
    # add_relation()     #添加报警组
    # SMTP_config()      #SMTP配置
    # 批量删除所有的服务
    '''
    list = ec.get_all_app()
    for name in list:
        ec.delete_svc(name)

    for i in range(30):
        app_name = "hello-"+ str(i)
        # delete_stack(app_name)
        # quck_deploy(app_name)
        ec.create_svc(app_name,"hello")
        # ec.delete_svc(app_name)
    # delete_stack()
'''
#收集日志
'''
    count = 0
    response = logging("192.168.22.3","","","2017.09.11","")  # 获取响应内容（str类型）
    pattern = regulation(response)  #获取匹配规则
    result = pattern.findall(response)# 将内容与匹配规则相对比，取出满足条件的结果集
    if result:  #如果结果不为空，则循环打印
        print "success to search!!!"
        for i in result:
            count += 1
            print (count)
            print i
    else:#结果为空
        print "fail! log is none"
'''