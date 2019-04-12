import logging

# 创建日志模块
logger = logging.getLogger("logs")
# 创建日志输出类型
fileHander = logging.FileHandler("sys.log", encoding="utf-8")
# 设置输出格式
setFormat = logging.Formatter("%(name)s %(levelname)s %(lineno)d %(asctime)s %(message)s")
# 将文件绑定格式
fileHander.setFormatter(setFormat)
# 将日志处理方式添加到日志工具
logger.addHandler(fileHander)

try:
    a, b = 5, 0
    r = a/b
    print(r)
except Exception as e:
    logger.error(e)
