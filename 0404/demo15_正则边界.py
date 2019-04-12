import re

"""
    边界
"""

result = re.findall("^hello", "hello world hello zhengzhou")
print(result)

result = re.findall("zhengzhou$", "hello world hello zhengzhou")
print(result)

# \b表示回退一定要 使用原始语句 r
result = re.findall(r"\bhello\b", "hello world hello zhengzhou sayhellook")
print(result)

result = re.findall(r"\Bhello\B", "hello world hello zhengzhou sayhellook")
print(result)

print("==========================================================")

"""
    匹配分组
"""

result = re.findall(r"\bhello\b|\bworld\b|\bhi\b", "hello world hi world")
print(result)

retsult = re.match(r".*?@.*?.com", "496575233@qq.com")
print(retsult.group())

retsult = re.match(r"(.*?)@(.*?)(.com)", "496575233@qq.com")
print(retsult.group(), retsult.group(1), retsult.group(2), retsult.group(3))

result = re.match(r"(hello).*?(hello)", "hello world hello china")
print(result.group(), result.group(1))
result = re.match(r"(hello).*?\1", "hello world hello china")
print(result.group(), result.group(1))
result = re.match(r"(?P<hname>hello) world (?P=hname)", "hello world hello china")
print(result.group(), result.group("hname"))






