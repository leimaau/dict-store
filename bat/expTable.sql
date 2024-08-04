set echo off
set trimspool on
set feedback off
set wrap off
set linesize 20000
set pagesize 20000
set newpage none
set heading off
set term off


spool E:\LocalRepository\github\dict_nb.txt
select * from dict_nb;

spool E:\LocalRepository\github\dict_nb_samp.txt
select * from dict_nb_samp;

spool E:\LocalRepository\github\dict_trad_simp_nb.txt
select * from dict_trad_simp_nb;


spool E:\LocalRepository\github\dict_nb_zingjam.txt
select * from dict_nb_zingjam;

spool E:\LocalRepository\github\dict_nb_zingjam_samp.txt
select DBMS_LOB.SUBSTR(word, 4000, 1) word from dict_nb_zingjam_samp;

spool E:\LocalRepository\github\dict_trad_simp_nb_zingjam.txt
select * from dict_trad_simp_nb_zingjam;



spool E:\LocalRepository\github\dict_nb_bw.txt
select * from dict_nb_bw;

spool E:\LocalRepository\github\dict_nb_samp_bw.txt
select * from dict_nb_samp_bw;

spool E:\LocalRepository\github\dict_trad_simp_nb_bw.txt
select * from dict_trad_simp_nb_bw;


spool E:\LocalRepository\github\dict_nb_zingjam_bw.txt
select * from dict_nb_zingjam_bw;

spool E:\LocalRepository\github\dict_nb_zingjam_samp_bw.txt
select DBMS_LOB.SUBSTR(word, 4000, 1) word from dict_nb_zingjam_samp_bw;

spool E:\LocalRepository\github\dict_trad_simp_nb_zingjam_bw.txt
select * from dict_trad_simp_nb_zingjam_bw;


spool E:\LocalRepository\github\v_nbdict_2003.txt
select trad||'chr(10)'||trad||' '||simp||' '||jyutping||' '||ipa_t||' '||replace(sour,'2003年侯精一《現代漢語方言音庫(字庫)》','')||' '||expl||' '||note||'chr(10)'||'</>' from v_nbdict_2003;

spool E:\LocalRepository\github\v_nbdict_200706.txt
select trad||'chr(10)'||trad||' '||simp||' '||jyutping||' '||ipa_t||' '||replace(sour,'2007年李彬《左江土白話研究》','')||' '||expl||' '||note||'chr(10)'||'</>' from v_nbdict_200706;

spool E:\LocalRepository\github\tab_nbdict_201806.txt
select trad||'chr(10)'||trad||' '||simp||' '||jyutping||' '||ipa_t||' '||sour||' '||expl||' '||note||'chr(10)'||'</>' from tab_nbdict_201806;

spool E:\LocalRepository\github\tab_nbdict_2021.txt
select trad||'chr(10)'||trad||' '||simp||' '||jyutping||' '||ipa_t||' '||sour||' '||expl||' '||note||'chr(10)'||'</>' from tab_nbdict_2021;


spool E:\LocalRepository\github\v_nbdict_201703_bw.txt
select trad||'chr(10)'||trad||' '||simp||' '||jyutping||' '||ipa_t||' '||sour||' '||expl||' '||note||'chr(10)'||'</>' from v_nbdict_201703_bw;

spool E:\LocalRepository\github\v_nbdict_201705_bw.txt
select trad||'chr(10)'||trad||' '||simp||' '||jyutping||' '||ipa_t||' '||replace(sour,'2017年詹伯慧、張振興《漢語方言學大詞典》','')||' '||expl||' '||note||'chr(10)'||'</>' from v_nbdict_201705_bw;

spool E:\LocalRepository\github\tab_nbdict_2021_bw.txt
select trad||'chr(10)'||trad||' '||simp||' '||jyutping||' '||ipa_t||' '||sour||' '||expl||' '||note||'chr(10)'||'</>' from tab_nbdict_2021_bw;

spool E:\LocalRepository\github\v_1856yh_single_extend.txt
select word||'chr(10)'||word||' '||old_jp||' '||old_tone||' '||jyutping||' '||ipa||' '||old_jp_type||' '||old_jp_note||' '||page||' '||expl||'chr(10)'||'</>' from v_1856yh_single_extend;


spool off