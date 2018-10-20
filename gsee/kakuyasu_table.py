#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
f = open(sys.argv[1],encoding="utf8")
text = f.read()
f.close()
result = re.sub('商品名', r'@\n商品名', text)
result = re.sub(r'冷やした商品：.+', "", result)
result = re.sub(r'.+：', "", result)
result = re.sub(r'\(税込\)', "", result)
result = re.sub(r'\n', r'\t', result)
result = re.sub(r'@', r'\n', result)
# result = re.sub(r'円', r'', result)
# result = re.sub(r'本', r'', result)

print (result)
file_head = '\n'+sys.argv[1]+'\n'
file=open('result.txt','a',encoding="utf8")
file.write(file_head)
file.write(result)
file.close()
# import re
# regex = r'ab+'
# text = "abbabbabaaabb"
# matchObj = re.match(regex, text)
