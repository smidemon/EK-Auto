#coding=utf-8
import requests,json
import cookielib,re
import urllib2,urllib,sys

#获取系统cookie，
def get_cookie(ip):
    url = "http://" + ip + ":30000/login"
    data = urllib.urlencode({'username':'admin','password':'admin12345'})
    mycookie = cookielib.CookieJar()#生成cookie对象
    handler = urllib2.HTTPCookieProcessor(mycookie) #利用urllib2库中的HTTPCookieProcessor来声明一个处理cookie的处理器
    opener = urllib2.build_opener(handler) #利用handler来构造opener，opener的用法和urlopen()类似
    response = opener.open(url,data) #opener返回的一个应答对象response
    print mycookie
    # print response.read()
    # for item in mycookie:   #循环打印出cookie的name和value
    #     print"name="+item.name
    #     print"value="+item.value
    # return opener
    # response = opener.open(newurl)
    # return response.read()
    # print opener
    # return opener
    urls = "http://"+ip+":30000/service/stack/api/stack"
    data = {"name":"appdss","ippool":"","namespace":"default"}
    headers = {'Content-Type': 'text/plain; charset=utf-8'}
    datas = urllib.urlencode(data)
    # request = urllib2.Request(
    #     url     = urls,
    #     headers = {'Content-Type': 'text/plain; charset=utf-8'},
    #     data    = datas)
    # result = opener.open(urls,datas)
    # request = urllib2.Request(urls, datas, headers)
    result = opener.open(urls,datas)
    print result.read()

#此模块有问题
def create_stack(url,param=None,data=None):
    datas = urllib.urlencode(data)
    opener = get_cookie("192.168.22.3")

    if param != None:
        newurl = url + "?" + param
    else:
        newurl = url
    print newurl
    # request = urllib2.Request(
        # url     = newurl,
        # headers = {'Content-Type': 'text/plain; charset=utf-8'},
        # data    = datas)

    result = opener.open(newurl,datas)
    # result = opener.open(request).read()
    print result.read()


#获取所有的日志
def logging(ip,app_name,svc_name,query_name):
    apps = app_name
    svc = svc_name
    query = query_name
    url = "http://"+str(ip)+":30000/service/logging/api/logs?" \
          "namespace=default&index=filebeat-6.0.0-beta1-" \
          "&page=1&size=100&application="+str(apps) \
    + "&service=" + str (svc) + "&pod=&containerID=&query=" + str(query)
    opener = get_cookie(ip)  #先获取登陆时的cookie
    # response = get_cookie(ip,url)
    response = opener.open(url)  #获取新地址的内容（现在只针对get请求，post请求暂未作处理）
    #opener.open()
    return response.read()    #将响应内容以文本的形式返回

#正则表达式，匹配满足条件的所有日志
def regulation(response):
    pattern = re.compile(u'_source.*?log":"(.*?)",',re.IGNORECASE)
    #变量pattern实现存储所有满足条件的记录；re.IGNORECASE忽略大小写；中间部分则是匹配规则，截取名为log中的内容
    #re.compile  正则表达式的匹配函数
    return pattern   #返回结果集

if __name__ == "__main__":
    # url = "http://192.168.22.3:30000/service/stack/api/stack"
    #url = "http://192.168.22.3:30000/service/stack/api/app"
    # data = {"name":"appdss","ippool":"","namespace":"default"}
    #data = {"name":"app-3","namespace":"default","stack":"apps","stateful":"none","replicas":1,"cpu":125,"memory":64,"diskSize":20000,"containers":[{"name":"ddddd","image":"registry.ekos.local/library/hello:latest","command":"","envs":[],"logDir":"","healthCheck":null,"cpuPercent":100,"memPercent":100,"stdin":false,"tty":false,"cfgFileMounts":[],"secretMounts":[]}],"service":{"ports":[{"protocol":"TCP","containerPort":80,"servicePort":80}]},"volumes":[],"desc":""}
    #create_stack(url=url,data=data)
    get_cookie("192.168.22.3")
'''
    response = logging("192.168.22.3","apps","app-2","tcp")  # 获取响应内容（str类型）
    pattern = regulation(response)  #获取匹配规则
    result = pattern.findall(response)# 将内容与匹配规则相对比，取出满足条件的结果集
    if result:  #如果结果不为空，则循环打印
        print "success to search!!!"
        for i in result:
            print i
    else:#结果为空
        print "fail! log is none"

'''








