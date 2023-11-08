import paramiko,time,os,configparser,sys
from selenium import webdriver
sys.path.append("..")
from tools import *
t = tools()

img_path = ''
projectpath = os.path.dirname(os.getcwd())
config_file = projectpath + '/configure/' + 'testconfig.ini'
filename = os.path.basename(__file__).split('.')[0]
t.log(filename)
config = configparser.ConfigParser()
config.read(config_file, encoding='UTF-8')
default_ip = config.get('Default', 'default_ip')
default_pw = config.get('Default', 'default_pw')
thumbnail_cmd = 'nice -n 19 /pic_thumb /mnt/sda1/1.JPG'

print(t.ssh_cmdss(default_ip, default_pw, thumbnail_cmd))
