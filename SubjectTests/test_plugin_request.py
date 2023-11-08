# -*- coding: utf-8 -*-
import urllib.request,io,os,sys,time,json
import logging

projectpath = os.path.dirname(os.getcwd())
config_file = projectpath + '/configure/' + 'testconfig.ini'

count = 1
while(True):
    logging.info("---------------------")
    logging.info("第" + str(count) +"次测试")
    logging.info("---------------------")
    time.sleep(5)
    date = time.ctime(time.time())
    try:
        req = urllib.request.Request("https://online-api.xcloud.cc/router/plugins/getPlugins/firmware/3.1.0.1000/version/0.0.0.0/mac/ec:0e:c4:0f:de:73/os/xCloudOS/force/false/platform/y1/pagesize/0/p/0?callback=jQuery19106331227631308138_1460696454396&_=1460696454397")
        f = urllib.request.urlopen(req)
        s = f.read()
        s = s.decode('gbk','ignore')
        s1 = f.getcode()
        logging.info(s1)
        count = count + 1
    except Exception as e:
        logging.info(e)
        continue
