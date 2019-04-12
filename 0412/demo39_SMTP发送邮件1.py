from smtplib import SMTP
# from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

try:
    # 连接到服务器
    smtp = SMTP(host="smtp.163.com")
    useemail = "18137128152@163.com"
    # 登录
    smtp.login(useemail, "qikuedu")
    # 构造发送文件内容对象
    # sendmulti = MIMEMultipart("这是Python写的一封邮件")
    # sendtext = MIMEText("这是Python写的一封邮件")
    sendtext = MIMEText("<h1>这是<p>Python</p>写的一封邮件</h1>", _subtype="html")
    # 显示发件人
    # sendmulti["from"] = useemail
    sendtext["from"] = useemail
    # 显示收件人
    # sendmulti["to"] = "1451055806@qq.com"
    sendtext["to"] = "1451055806@qq.com"
    # 邮件主题
    # sendmulti["subject"] = "测试邮件"
    sendtext["subject"] = "测试邮件"
    # 发送方法  第一个参数：发件人  第二个参数：收件人列表  第三个参数：邮件转字符串
    # smtp.sendmail(useemail, ["1451055806@qq.com"], sendmulti.as_string())
    smtp.sendmail(useemail, ["1451055806@qq.com"], sendtext.as_string())
    # 退出链接
    smtp.quit()
except Exception as e:
    print(e)

