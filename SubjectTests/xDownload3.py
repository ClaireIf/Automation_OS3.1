# -*- coding:utf-8 -*-
import paramiko
import json
import time
import csv

def xDssh():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("192.168.7.1",22,"root", "12345678")
    stdin, stdout, stderr = ssh.exec_command("ubus call xapi.xDownload status '{\"params\":\"ids\"}'")
    downtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(downtime)
    list=stdout.readlines()
    allInfo = json.JSONDecoder().decode(''.join(list))
    #print(allInfo)
    down=allInfo["allInfo"]
    #print(down)
    rateDownload = down[0]["rateDownload"]
    rateDownload1 = down[1]["rateDownload"]
    rateDownload2 = down[2]["rateDownload"]
    print(rateDownload)
    print(rateDownload2)
    print(rateDownload2)
    excl = open("xDownload.csv", 'a+', newline='')
    firstline = [rateDownload, rateDownload1, rateDownload2, downtime]
    csvwriter = csv.writer(excl, dialect='excel')
    csvwriter.writerow(firstline)
    firstline.append(rateDownload)
    firstline.append(downtime)
    excl.close()
xDssh()

##for i in range(10000):
##    xDssh()
##    time.sleep(30)
