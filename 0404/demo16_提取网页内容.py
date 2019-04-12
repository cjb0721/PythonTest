# import requests
# import re
#
# response = requests.get("http://quote.stockstar.com/stock/ranklist_a_3_1_1.html?tdsourcetag=s_pcqq_aiomsg")
#
# text = response.text
# # print(text)
#
# # r1 = re.findall(r'<a href="//stock.quote.stockstar.com/(.*?).shtml">(.*?)</a>', text)
# # print(r1)
#
# table = re.search(r'<table width="100%" border="0" cellpadding="0" cellspacing="0" class="trHover" id="table1">(.*?)</table>', text, flags=re.S)
# print(table.group(1))
# # threads = re.search(r'<thead class="tbody_right"><tr>(.*?)</tr></thead>', table)
# # print(type(threads))


import requests, re

response = requests.get("http://quote.stockstar.com/stock/ranklist_a_3_1_1.html")
# print(response.text)

tbody = re.search(r'<tbody class="tbody_right" id="datalist">(.*?)</tbody>', response.text, flags=re.S)
# print(tbody.group(1))

trs = re.findall(r'<tr>(.*?)</tr>', tbody.group(1))
# print(trs)
for i in trs:
    # print(i)
    tds = re.findall(r'<td class="(.*?)">(.*?)</td>', i)
    # print(tds[0][1])
    # print(tds[1][1])
    # print(tds[2][1])
    ids = re.search(r'<a href="//stock.quote.stockstar.com/(.*?).shtml">(.*?)</a>', tds[0][1])
    # print(ids.group(1))
    name = re.search(r'<a href="//stock.quote.stockstar.com/(.*?).shtml">(.*?)</a>', tds[1][1])
    # print(name.group(2))
    price = re.search(r'<span class="red">(.*?)</span>', tds[2][1])
    # print(price.group(1))

    with open("data.txt", 'a', encoding='utf8') as f:
        # title = '代码\t\t简称\t\t最新价\n'
        # f.write(title)
        info = str(ids.group(1)) + "\t" + str(name.group(2)) + "\t" + price.group(1) + "\n<br>\n"
        f.write(info)








