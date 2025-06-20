set echo off
set trimspool on
set feedback off
set wrap off
set linesize 20000
set pagesize 20000
set newpage none
set heading off
set term off


spool E:\LocalRepository\github\dict-store-txt\temp\dict_nb.txt
select * from dict_nb;

spool E:\LocalRepository\github\dict-store-txt\temp\dict_nb_samp.txt
select * from dict_nb_samp;

spool E:\LocalRepository\github\dict-store-txt\temp\dict_trad_simp_nb.txt
select * from dict_trad_simp_nb;


spool E:\LocalRepository\github\dict-store-txt\temp\dict_nb_zingjam.txt
select * from dict_nb_zingjam;

spool E:\LocalRepository\github\dict-store-txt\temp\dict_nb_zingjam_samp.txt
select DBMS_LOB.SUBSTR(word, 4000, 1) word from dict_nb_zingjam_samp;

spool E:\LocalRepository\github\dict-store-txt\temp\dict_trad_simp_nb_zingjam.txt
select * from dict_trad_simp_nb_zingjam;



spool E:\LocalRepository\github\dict-store-txt\temp\dict_nb_bw.txt
select * from dict_nb_bw;

spool E:\LocalRepository\github\dict-store-txt\temp\dict_nb_samp_bw.txt
select * from dict_nb_samp_bw;

spool E:\LocalRepository\github\dict-store-txt\temp\dict_trad_simp_nb_bw.txt
select * from dict_trad_simp_nb_bw;


spool E:\LocalRepository\github\dict-store-txt\temp\dict_nb_zingjam_bw.txt
select * from dict_nb_zingjam_bw;

spool E:\LocalRepository\github\dict-store-txt\temp\dict_nb_zingjam_samp_bw.txt
select DBMS_LOB.SUBSTR(word, 4000, 1) word from dict_nb_zingjam_samp_bw;

spool E:\LocalRepository\github\dict-store-txt\temp\dict_trad_simp_nb_zingjam_bw.txt
select * from dict_trad_simp_nb_zingjam_bw;


spool E:\LocalRepository\github\dict-store-txt\temp\v_nbdict_2003.txt
select trad||'chr(10)'||trad||' '||simp||' '||jyutping||' '||ipa_t||' '||replace(sour,'2003年侯精一《現代漢語方言音庫(字庫)》','')||' '||expl||' '||note||'chr(10)'||'</>' from v_nbdict_2003;

spool E:\LocalRepository\github\dict-store-txt\temp\v_nbdict_200706.txt
select trad||'chr(10)'||trad||' '||simp||' '||jyutping||' '||ipa_t||' '||replace(sour,'2007年李彬《左江土白話研究》','')||' '||expl||' '||note||'chr(10)'||'</>' from v_nbdict_200706;

spool E:\LocalRepository\github\dict-store-txt\temp\tab_nbdict_201806.txt
select trad||'chr(10)'||trad||' '||simp||' '||jyutping||' '||ipa_t||' '||sour||' '||expl||' '||note||'chr(10)'||'</>' from tab_nbdict_201806;

spool E:\LocalRepository\github\dict-store-txt\temp\tab_nbdict_2021.txt
select trad||'chr(10)'||trad||' '||simp||' '||jyutping||' '||ipa_t||' '||sour||' '||expl||' '||note||'chr(10)'||'</>' from tab_nbdict_2021;


spool E:\LocalRepository\github\dict-store-txt\temp\v_nbdict_201703_bw.txt
select trad||'chr(10)'||trad||' '||simp||' '||jyutping||' '||ipa_t||' '||sour||' '||expl||' '||note||'chr(10)'||'</>' from v_nbdict_201703_bw;

spool E:\LocalRepository\github\dict-store-txt\temp\v_nbdict_201705_bw.txt
select trad||'chr(10)'||trad||' '||simp||' '||jyutping||' '||ipa_t||' '||replace(sour,'2017年詹伯慧、張振興《漢語方言學大詞典》','')||' '||expl||' '||note||'chr(10)'||'</>' from v_nbdict_201705_bw;

spool E:\LocalRepository\github\dict-store-txt\temp\tab_nbdict_2021_bw.txt
select trad||'chr(10)'||trad||' '||simp||' '||jyutping||' '||ipa_t||' '||sour||' '||expl||' '||note||'chr(10)'||'</>' from tab_nbdict_2021_bw;

spool E:\LocalRepository\github\dict-store-txt\temp\v_1856yh_single_extend.txt
select word||'chr(10)'||word||' '||old_jp||' '||old_tone||' '||jyutping||' '||ipa||' '||old_jp_type||' '||old_jp_note||' '||page||' '||expl||'chr(10)'||'</>' from v_1856yh_single_extend;

--詞彙表
spool E:\LocalRepository\github\dict-store-txt\temp\tab_nbdict_1997_phrase.txt
select * from (
select trad||'chr(10)【'||trad||case when simp<>trad then '（'||simp||'）' else null end||'】<br>'||jyutping||' ['||ipa_t||'] '||sour||' ['||ipa_s||']<br>'||expl||case when note is not null then '<br>' else null end||note||case when classifi is not null then '<br>分類：' else null end||classifi||'chr(10)</>' from v_nbdict_1997_phrase
union select simp||'chr(10)@@@LINK='||trad||'chr(10)</>' from v_nbdict_1997_phrase where simp<>trad
);

spool E:\LocalRepository\github\dict-store-txt\temp\tab_nbdict_1998_phrase.txt
select * from (
select trad||'chr(10)【'||trad||case when simp<>trad then '（'||simp||'）' else null end||'】<br>'||jyutping||' ['||ipa_t||'] '||sour||' ['||ipa_s||']<br>'||expl||case when note is not null then '<br>' else null end||note||case when classifi is not null then '<br>分類：' else null end||classifi||'chr(10)</>' from v_nbdict_1998_phrase
union select simp||'chr(10)@@@LINK='||trad||'chr(10)</>' from v_nbdict_1998_phrase where simp<>trad
);

spool E:\LocalRepository\github\dict-store-txt\temp\tab_nbdict_2007_phrase.txt
select * from (
select trad||'chr(10)【'||trad||case when simp<>trad then '（'||simp||'）' else null end||'】<br>'||jyutping||' ['||ipa_t||'] '||sour||' ['||ipa_s||']<br>'||expl||case when note is not null then '<br>' else null end||note||case when classifi is not null then '<br>分類：' else null end||classifi||'chr(10)</>' from v_nbdict_2007_phrase
union select simp||'chr(10)@@@LINK='||trad||'chr(10)</>' from v_nbdict_2007_phrase where simp<>trad
);

spool E:\LocalRepository\github\dict-store-txt\temp\tab_nbdict_2008_phrase.txt
select * from (
select trad||'chr(10)【'||trad||case when simp<>trad then '（'||simp||'）' else null end||'】<br>'||jyutping||' ['||ipa_t||'] '||sour||' ['||ipa_s||']<br>'||expl||case when note is not null then '<br>' else null end||note||case when classifi is not null then '<br>分類：' else null end||classifi||'chr(10)</>' from v_nbdict_2008_phrase
union select simp||'chr(10)@@@LINK='||trad||'chr(10)</>' from v_nbdict_2008_phrase where simp<>trad
);

/*
spool E:\LocalRepository\github\dict-store-txt\temp\tab_nbdict_2020_phrase.txt
select * from (
select trad||'chr(10)【'||trad||case when simp<>trad then '（'||simp||'）' else null end||'】<br>'||jyutping||' ['||ipa_t||'] '||sour||' ['||ipa_s||']<br>'||expl||case when note is not null then '<br>' else null end||note||case when classifi is not null then '<br>分類：' else null end||classifi||'chr(10)</>' from tab_nbdict_2020_phrase
union select simp||'chr(10)@@@LINK='||trad||'chr(10)</>' from tab_nbdict_2020_phrase where simp<>trad
);
*/

spool E:\LocalRepository\github\dict-store-txt\temp\tab_nbdict_2021_phrase.txt
select * from (
select trad||'chr(10)【'||trad||case when simp<>trad then '（'||simp||'）' else null end||'】<br>'||jyutping||' ['||ipa_t||'] '||sour||' ['||ipa_s||']<br>'||expl||case when note is not null then '<br>' else null end||note||case when classifi is not null then '<br>分類：' else null end||classifi||'chr(10)</>' from tab_nbdict_2021_phrase
union select simp||'chr(10)@@@LINK='||trad||'chr(10)</>' from tab_nbdict_2021_phrase where simp<>trad
);

spool E:\LocalRepository\github\dict-store-txt\temp\tab_nbdict_2021_bw_phrase.txt
select * from (
select trad||'chr(10)【'||trad||case when simp<>trad then '（'||simp||'）' else null end||'】<br>'||jyutping||' ['||ipa_t||'] '||sour||' ['||ipa_s||']<br>'||expl||case when note is not null then '<br>' else null end||note||case when classifi is not null then '<br>分類：' else null end||classifi||'chr(10)</>' from tab_nbdict_2021_bw_phrase
union select simp||'chr(10)@@@LINK='||trad||'chr(10)</>' from tab_nbdict_2021_bw_phrase where simp<>trad
);

spool E:\LocalRepository\github\dict-store-txt\temp\tab_nb_zingjam_phrase.txt
select * from (
select trad||'chr(10)【'||trad||case when simp<>trad then '（'||simp||'）' else null end||'】<br>'||jyutping||' ['||ipa_t||']<br>'||expl||case when note is not null then '<br>' else null end||note||case when classifi is not null then '<br>分類：' else null end||classifi||'chr(10)</>' from tab_nb_zingjam_phrase
union select simp||'chr(10)@@@LINK='||trad||'chr(10)</>' from tab_nb_zingjam_phrase where simp<>trad
);

/*
spool E:\LocalRepository\github\dict-store-txt\temp\tab_nbdict_2020_bw_phrase.txt
select * from (
select trad||'chr(10)【'||trad||case when simp<>trad then '（'||simp||'）' else null end||'】<br>'||jyutping||' ['||ipa_t||'] '||sour||' ['||ipa_s||']<br>'||expl||case when note is not null then '<br>' else null end||note||case when classifi is not null then '<br>分類：' else null end||classifi||'chr(10)</>' from tab_nbdict_2020_bw_phrase
union select simp||'chr(10)@@@LINK='||trad||'chr(10)</>' from tab_nbdict_2020_bw_phrase where simp<>trad
);
*/

spool E:\LocalRepository\github\dict-store-txt\temp\v_xiandaihanyu_phrase.txt
select * from (
select trad||'chr(10)【'||trad||case when simp<>trad then '（'||simp||'）' else null end||'】<br>'||'［白］'||jyutping||' ['||ipa||'] '||'［平］'||jyutping2||' ['||ipa2||']<br>'||expl||'chr(10)</>' from V_XIANDAIHANYU_PHRASE
union select simp||'chr(10)@@@LINK='||trad||'chr(10)</>' from V_XIANDAIHANYU_PHRASE where simp<>trad
);

spool E:\LocalRepository\github\dict-store-txt\temp\v_xiandaihanyu_phrase_book.txt
select * from (
select trad||'chr(10)'||SIMP_TRAD_format||'<br>'||jyutping||'<br>'||expl||'chr(10)</>' from v_xiandaihanyu_phrase_book
union select simp||'chr(10)@@@LINK='||trad||'chr(10)</>' from v_xiandaihanyu_phrase_book where simp<>trad
);

spool E:\LocalRepository\github\dict-store-txt\temp\v_xiandaihanyu_phrase_book_bw.txt
select * from (
select trad||'chr(10)'||SIMP_TRAD_format||'<br>'||jyutping||'<br>'||expl||'chr(10)</>' from v_xiandaihanyu_phrase_book_bw
union select simp||'chr(10)@@@LINK='||trad||'chr(10)</>' from v_xiandaihanyu_phrase_book_bw where simp<>trad
);

spool off

exit;