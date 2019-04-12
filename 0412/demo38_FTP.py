from ftplib import FTP

try:
    ftp = FTP(host="192.168.12.234")
    ftp.login(user="Administrator", passwd="123456")
    # print(ftp.pwd())
    # print(ftp.dir())
    # print(ftp.mkd("newFolder"))
    ftp.cwd("newFolder")
    print(ftp.pwd())
    ftp.quit()
except Exception as e:
    print(e)


