import os
uppath = 'E:\\第一轮不能下载种子\\'
uppath2 = 'E:\\xDownload2\\'
# os.rename(uppath,uppath2)
files = os.listdir(uppath)
i = 1
for file in files:
    os.rename(uppath + file, uppath2 + str(i) + '.torrent')
    i = i + 1