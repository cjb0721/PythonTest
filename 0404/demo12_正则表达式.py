from collections.abc import Iterator
import re


str = "hello worlld"

# result = re.match("h", str)
# result = re.search("l", str)
# result = re.fullmatch("hello world", str)

# result = re.findall("ll", str)
# result = re.split("ll", str)
# result = re.split("ll", str, maxsplit=2)
# result = re.sub("l", "a", str, count=2)
# result = re.finditer("ll", str)
# print(re)
# print(result, type(result))
# print(dir(result))
#
# if isinstance(result, re.Match):
#     print(result.group(), result.span())
# elif isinstance(result, list):
#     for i in result:
#         print(i)
# elif isinstance(result, Iterator):
#     for i in result:
#         print(i)


strs = "hello world"
# pat = re.compile("h")
pat = re.compile("ll")
print(pat, type(pat))
# result = pat.match(strs)
results = pat.search(strs)
print(results, type(results))
print(results.group())

