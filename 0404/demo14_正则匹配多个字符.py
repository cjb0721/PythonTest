import re

str1 = "hello world"
# result = re.findall("l*", str)
# result = re.findall("l+", str)
# result = re.findall("l?", str)
# result = re.findall("l{1}", str)
# result = re.findall("l{1,}", str)
# result = re.findall("l{2}", str)
result = re.findall("l{1,2}", str1)

print(result)
