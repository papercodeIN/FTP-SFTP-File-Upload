from datetime import datetime
import pysftp

print("""                                                         
                                                                        
__ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ 
                                                                                                                                                                                        
 __   ___ ___  __      ___         ___          __        __        __  
/__` |__   |  |__)    |__  | |    |__     |  | |__) |    /  \  /\  |  \ 
.__/ |     |  |       |    | |___ |___    \__/ |    |___ \__/ /~~\ |__/ 
                                                                                                               
__ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ 
                                                                        
                                                                        
""")

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None


with pysftp.Connection(host="35.154.214.107", username="4pelKatol", password="njs82nHKdb9l02Qn4pnfhksi9D4Z0f8X07AMz", cnopts=cnopts) as sftp:
    print ("Connection succesfully stablished ... ")

    # Switch to a remote directory
    sftp.cwd('/home/4pelKatol/ftp_files/WRPL_Katol/')

    sftp.put(r'F:\FTP_DATA\FTP_HO\DATA\ICR2\{}.csv'.format(datetime.today().strftime('%d-%m-%Y')))

    sftp.close()
