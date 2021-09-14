import ftplib 
import os
from datetime import datetime

print("""
__ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ 
                                                                              
 ___ ___  __      ___         ___          __        __        __       
|__   |  |__)    |__  | |    |__     |  | |__) |    /  \  /\  |  \      
|     |  |       |    | |___ |___    \__/ |    |___ \__/ /~~\ |__/      
                                                                            
__ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ 

""")


host = "http://demo.wftpserver.com/"
username = "demo"
password = "demo"

# connect to host on default port i.e 21
ftp = ftplib.FTP(host=host)
login_status = ftp.login(username,password)
print(login_status)

# change directory to upload
ftp.cwd('upload')    
print(ftp.dir())
fp = open('D:\\Test.text')
# fp = open('D:\\FTPCSV\MINDATA\FTP{}.csv'.format(datetime.today().strftime('%d-%m-%Y')),'rb')
ftp.storbinary('STOR {}.csv'.format(datetime.today().strftime('%d-%m-%Y')), fp)
fp.close()
#print(ftp.dir())
