import re
text = '匹配一段中文，this is a book ,非中文部分不要'
pattern = re.compile('[\u4e00-\u9fa5]+')
res = pattern.search(text)

lst = []

while res:
    start, end = res.span()
    lst.append(res.group())
    res = pattern.search(text, end+1)
print(lst)
