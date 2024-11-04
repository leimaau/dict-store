#!/usr/bin/python
# coding: utf-8 

import os

path = 'E:\\LocalRepository\\github'
files = os.listdir(path)
files = [ele for ele in files if '.txt' in ele]

old_str = 'chr(10)'
new_str = '\n'

for file in files:
    if not os.path.isdir(file):
        file_data = []
        f = open(path+'\\'+file,'r',encoding='utf-8')
        iter_f = iter(f)
        for line in iter_f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data.append(line)
        f.close()
        f2 = open(path+'\\'+file,'w',encoding='utf-8')
        file_data2 = ''.join(file_data)
        f2.write(file_data2)
        f2.close()


f = open('E:\\LocalRepository\\github\\dict-store-txt\\邕潯片\\南寧白話常用字讀音表.txt','w',encoding='utf-8')
f2 = open('E:\\LocalRepository\\github\\dict_nb.txt','r',encoding='utf-8')
f3 = open('E:\\LocalRepository\\github\\dict_nb_samp.txt','r',encoding='utf-8')
f4 = open('E:\\LocalRepository\\github\\dict_trad_simp_nb.txt','r',encoding='utf-8')

new_data = ''.join(f2.readlines() + f3.readlines() + f4.readlines())
f.write(new_data)

f4.close()
f3.close()
f2.close()
f.close()


f = open('E:\\LocalRepository\\github\\dict-store-txt\\邕潯片\\南寧白話建議讀音表.txt','w',encoding='utf-8')
f2 = open('E:\\LocalRepository\\github\\dict_nb_zingjam.txt','r',encoding='utf-8')
f3 = open('E:\\LocalRepository\\github\\dict_nb_zingjam_samp.txt','r',encoding='utf-8')
f4 = open('E:\\LocalRepository\\github\\dict_trad_simp_nb_zingjam.txt','r',encoding='utf-8')

new_data = ''.join(f2.readlines() + f3.readlines() + f4.readlines())
f.write(new_data)

f4.close()
f3.close()
f2.close()
f.close()


f = open('E:\\LocalRepository\\github\\dict-store-txt\\平話\\南寧平話常用字讀音表.txt','w',encoding='utf-8')
f2 = open('E:\\LocalRepository\\github\\dict_nb_bw.txt','r',encoding='utf-8')
f3 = open('E:\\LocalRepository\\github\\dict_nb_samp_bw.txt','r',encoding='utf-8')
f4 = open('E:\\LocalRepository\\github\\dict_trad_simp_nb_bw.txt','r',encoding='utf-8')

new_data = ''.join(f2.readlines() + f3.readlines() + f4.readlines())
f.write(new_data)

f4.close()
f3.close()
f2.close()
f.close()


f = open('E:\\LocalRepository\\github\\dict-store-txt\\平話\\南寧平話建議讀音表.txt','w',encoding='utf-8')
f2 = open('E:\\LocalRepository\\github\\dict_nb_zingjam_bw.txt','r',encoding='utf-8')
f3 = open('E:\\LocalRepository\\github\\dict_nb_zingjam_samp_bw.txt','r',encoding='utf-8')
f4 = open('E:\\LocalRepository\\github\\dict_trad_simp_nb_zingjam_bw.txt','r',encoding='utf-8')

new_data = ''.join(f2.readlines() + f3.readlines() + f4.readlines())
f.write(new_data)

f4.close()
f3.close()
f2.close()
f.close()



os.rename('E:\\LocalRepository\\github\\v_nbdict_2003.txt','E:\\LocalRepository\\github\\2003年楊煥典《現代漢語方言音庫字庫》.txt')
os.rename('E:\\LocalRepository\\github\\v_nbdict_200706.txt','E:\\LocalRepository\\github\\2007年李彬《左江土白話研究》（南寧白話）.txt')
os.rename('E:\\LocalRepository\\github\\tab_nbdict_201806.txt','E:\\LocalRepository\\github\\2018年滕祖愛《南寧市與桂平市粵方言比較研究》.txt')
os.rename('E:\\LocalRepository\\github\\tab_nbdict_2021.txt','E:\\LocalRepository\\github\\2021年Leimaau《單字音零散資料匯總》（南寧白話）.txt')
os.rename('E:\\LocalRepository\\github\\v_nbdict_201703_bw.txt','E:\\LocalRepository\\github\\2017年教育部《漢語方言用字規範》（南寧亭子平話）.txt')
os.rename('E:\\LocalRepository\\github\\v_nbdict_201705_bw.txt','E:\\LocalRepository\\github\\2017年詹伯慧、張振興《漢語方言學大詞典》（南寧亭子平話）.txt')
os.rename('E:\\LocalRepository\\github\\tab_nbdict_2021_bw.txt','E:\\LocalRepository\\github\\2021年Leimaau《單字音零散資料匯總》（南寧亭子平話）.txt')
os.rename('E:\\LocalRepository\\github\\v_1856yh_single_extend.txt','E:\\LocalRepository\\github\\1856年《英華分韻撮要》.txt')
