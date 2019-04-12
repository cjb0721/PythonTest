# 1、导入模块
import logging

# # 无法设置编码格式
# # logging.basicConfig(filename='sys.log')
# logging.basicConfig(filename='sys.log', level=logging.DEBUG)
# logging.debug("debug message")
# logging.info("info message")
# logging.warning("You have a warning.")
# logging.error("Error message")
# logging.critical("Hello World")


# 2、创建日志模块
loginLg = logging.getLogger("loginregist")
# 2.1、日志等级
loginLg.setLevel(logging.DEBUG)
# 3、创建日志输出类型
fileHd = logging.FileHandler('loginregist.txt', encoding="utf-8")
# 3.1、文件日志等级
fileHd.setLevel(logging.DEBUG)
# 4、指定日志格式
fileFm = logging.Formatter('%(name)s-%(levelno)s-%(lineno)d-%(asctime)s-%(message)s')
# 5、将文件绑定日志格式
fileHd.setFormatter(fileFm)

streamHd = logging.StreamHandler()
# streamHd.setLevel(logging.DEBUG)
streamHd.setFormatter(fileFm)

# 6、将日志处理方法添加到日志工具
loginLg.addHandler(fileHd)
loginLg.addHandler(streamHd)


#
loginLg.debug("debug message")
loginLg.info("info message")
loginLg.warning("You have a warning.")
loginLg.error("Error message")