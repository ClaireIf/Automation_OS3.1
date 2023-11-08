# -*- coding:utf-8 -*-
import paramiko
import json
import time
import csv

def xDssh():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("192.168.7.1",22,"root", "87654321")
    stdin, stdout, stderr = ssh.exec_command("ubus call xapi.xDownload status '{\"params\":\"ids\"}'")
    list=stdout.readlines()
    allInfo = json.JSONDecoder().decode(''.join(list))
    down=allInfo["allInfo"]
    rateDownload = down[0]["rateDownload"]
    print(rateDownload)
    downtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(downtime)
    excl = open("xDownload.csv", 'a+', newline='')
    firstline = [rateDownload,downtime]
    csvwriter = csv.writer(excl, dialect='excel')
    csvwriter.writerow(firstline)
    firstline.append(rateDownload)
    firstline.append(downtime)
    excl.close()


for i in range(10000):
    xDssh()
    time.sleep(30)