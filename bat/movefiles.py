#!/usr/bin/python
# coding: utf-8 

import os
import shutil

path = 'E:\\LocalRepository\\github'
files = os.listdir(path)
files = [ele for ele in files if '.txt' in ele]

for file in files:
    if not os.path.isdir(file):
        if '平話' in file:
            shutil.move(path+'\\'+file,'E:\\LocalRepository\\github\\dict-store-txt\\平話'+'\\'+file)
        elif '白話' in file or file=='2003年楊煥典《現代漢語方言音庫字庫》.txt' or file=='2018年滕祖愛《南寧市與桂平市粵方言比較研究》.txt':
            shutil.move(path+'\\'+file,'E:\\LocalRepository\\github\\dict-store-txt\\邕潯片'+'\\'+file)
        else:
            shutil.move(path+'\\'+file,'E:\\LocalRepository\\github\\dict-store-txt\\bat'+'\\'+file)