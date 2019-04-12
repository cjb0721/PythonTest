import re

str1 = "hello world.\nHi python\nhh"
# result = re.findall("h*", str1, flags=re.S)
result = re.findall(".", "hello \n china", flags=re.S)
# "." 可以匹配换行符
print(result)

result = re.findall(".", "hello \n china", flags=re.M)
# "." 不可以匹配换行符
print(result)

result = re.findall("h.", str1, flags=re.M|re.I)

print(result)



"""
    单字符匹配
"""

result = re.findall("[0123].ello", "0hello 1hello 2 ello 88ello 888ello")
print(result)
result = re.findall("\dhello", "hello 1hello 5hello 0hello")
print(result)
result = re.findall("\Dhello", "xhello 1hello 5hello 0hello")
print(result)
result = re.findall("\shello", "hello hello hello")
print(result)
result = re.findall("\Shello", "1hello shello hello")
print(result)
result = re.findall("\wello", "hello aello5ello_ello .ello ^ello")
print(result)
result = re.findall("\Wello", "hello aello5ello_ello .ello ^ello")
print(result)

