 # coding=utf-8
from crt_stk import EkOS
import sys,json,time
import ConfigParser
import unittest
sys.path.insert(0,"D:\PY_project\EkOS_Test")

config = ConfigParser.ConfigParser()
config.readfp(open("config.ini"))
ipaddr = config.get("main","ipaddr")

data = config.get('json','network_data')
print str(data)

ddd = "dad\"dasd\"dsd"
print ddd.strip('"')