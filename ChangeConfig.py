import os,shutil
model = 'y2'
get_path = os.getcwd()
config_path = get_path + '\\configure'
config_file = config_path + '\\'+ model + '_testconfig.ini'
config_file1 = config_path + '\\'+ 'y3'+ '_testconfig.ini'
shutil.copy(config_file, config_file1)
os.rename(os.path.join(config_file1), os.path.join(config_path + '\\'+ 'y4'+ '_testconfig.ini'))