"""
import os,sys,time,threading,pymysql,traceback,requests,json
project_path = os.path.abspath('../..')
sys.path.append(project_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SDUVJ.settings")
import django
django.setup()
from submiter import *


def getCode(source):
    global project_path
    try:
        print("Path : "+project_path+'/codes/'+str(source))
        
        file_object = open(project_path+'/codes/'+str(source))
        all_the_text = 'NULL'
        try:
            all_the_text = file_object.read( )
        finally:
            file_object.close( )
        return all_the_text
    except:
        print("The code file does not exist")
Prob = '1001'
acc = 'sduvj1'
Code = getCode('hdu1000')

submiter = ZojSubmiter(Prob,acc,Code,'0')

submiter.submit2OJ()




import requests,json

baseURL = 'http://127.0.0.1:6800/'
delProUrl = baseURL + 'delproject.json'
dictdata = {"project":"vjspider"}
r = requests.post(delProUrl,data=dictdata)
"""
from updateProb2DB import *

updateProb('ZOJ','1009')
"""
for i in range(0,10):
    updateProb('HDU',str(1000+i))
for i in range(0,10):
    updateProb('FZU',str(1000+i))
for i in range(0,10):
    updateProb('ZOJ',str(1000+i))

"""