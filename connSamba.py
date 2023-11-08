from smb.SMBConnection import SMBConnection
user_name = "root"
pass_word = "12345678"
my_name = "root"
domain_name = ""
remote_smb_IP = "192.168.7.1"

conn = SMBConnection(user_name, pass_word, my_name, domain_name, use_ntlm_v2 = True)
print(conn.connect(remote_smb_IP,60))
# assert conn.connect(remote_smb_IP , 139)