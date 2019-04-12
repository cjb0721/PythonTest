from smtplib import SMTP, SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

try:
    # 连接到服务器
    # smtp = SMTP(host="smtp.163.com")
    smtp = SMTP_SSL(host="smtp.qq.com", port=465)
    # useemail = "18137128152@163.com"
    useemail = "492595085@qq.com"
    # 登录
    # smtp.login(useemail, "zhznarqniufybgia")
    smtp.login(useemail, "rhblddykgdgobjgf")
    # smtp.login(useemail, "qikuedu")
    # 构造发送文件内容对象
    # sendmulti = MIMEMultipart("<h1>这是<b>Python<b>写的一封邮件</h1>", "html")
    sendmulti = MIMEMultipart()
    # sendtext = MIMEText("世外桃源")
    # 显示发件人
    sendmulti["from"] = useemail
    # sendtext["from"] = useemail
    # 显示收件人
    sendmulti["to"] = "1451055806@qq.com, 492595085@qq.com"
    # sendtext["to"] = "1451055806@qq.com, 492595085@qq.com"
    # 邮件主题
    sendmulti["subject"] = "测试邮件"
    # sendtext["subject"] = "测试邮件"

    # 构造文本对象并添加进邮件对象
    # text = MIMEText("世外桃源")
    # sendmulti.attach(text)
    # sendtext.attach(text)

    # 构造图片对象并添加进邮件对象
    with open("图像1.png", "rb") as f:
        imgdata = MIMEImage(f.read())
        imgdata.add_header("Content-ID", "img001")
        sendmulti.attach(imgdata)

    htmlTitle = "<h1>世外桃源</h1><img src='cid:img001' /><p>End</p>"
    html = MIMEText(htmlTitle, "html")
    sendmulti.attach(html)

    # 添加文件附件
    with open("demo40_SMTP发送邮件2.py", "rb") as f:
        mess_file = MIMEText(f.read(), "base64", "utf-8")
        mess_file["Content-Type"] = "application/octet-stream"
        mess_file["Content-Disposition"] = "attachment; filename='new.txt'"
        sendmulti.attach(mess_file)



    # 发送方法  第一个参数：发件人  第二个参数：收件人列表  第三个参数：邮件转字符串
    smtp.sendmail(useemail, ["1451055806@qq.com", "492595085@qq.com"], sendmulti.as_string())
    # smtp.sendmail(useemail, ["492595085@qq.com"], sendtext.as_string())
    # 退出链接
    smtp.quit()
except Exception as e:
    print(e)























