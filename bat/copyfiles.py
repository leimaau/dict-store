#!/usr/bin/python
# coding: utf-8 

import os
import sys
import shutil
import subprocess
from pathlib import Path
from typing import List, Dict, Set, Tuple, Optional

# 常量定义
BASE_DIR = Path(r'E:\LocalRepository\github\dict-store-txt')
TEMP_DIR = BASE_DIR / 'temp'
BAT_DIR = BASE_DIR / 'bat'
OUTPUT_DIRS = {
    'yongxun': BASE_DIR / '邕潯片',
    'pinghua': BASE_DIR / '平話',
    'qingdai': BASE_DIR / '清代粵語'
}
bat_path = BAT_DIR / 'expbat.bat'

# 文件分类规则（按优先级排序）
FILE_CATEGORIES: List[Tuple[str, Set[str]]] = [
    ('yongxun', {'白話', '楊煥典', '滕祖愛', '現代漢語詞彙表'}),
    ('pinghua', {'平話'}),
    ('qingdai', {'英華分韻撮要'}),
    ('dict', {'dict'})
]

def process_text_files(directory: Path) -> None:
    """处理指定目录下的所有文本文件，将chr(10)替换为换行符"""
    for file_path in directory.glob('*.txt'):
        if file_path.is_file():
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            processed_content = content.replace('chr(10)', '\n')
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(processed_content)

def combine_files(output_path: Path, input_files: List[Path]) -> None:
    """将多个输入文件合并为一个输出文件"""
    combined_content = []
    for input_file in input_files:
        with open(input_file, 'r', encoding='utf-8') as f:
            combined_content.extend(f.readlines())
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(''.join(combined_content))

def rename_files() -> None:
    """重命名临时目录中的文件为最终名称"""
    rename_mappings = {
        'v_nbdict_2003.txt': '2003年楊煥典《現代漢語方言音庫字庫》.txt',
        'v_nbdict_200706.txt': '2007年李彬《左江土白話研究》（南寧白話）.txt',
        'tab_nbdict_201806.txt': '2018年滕祖愛《南寧市與桂平市粵方言比較研究》.txt',
        'tab_nbdict_2021.txt': '2021年Leimaau《單字音零散資料匯總》（南寧白話）.txt',
        'v_nbdict_201703_bw.txt': '2017年教育部《漢語方言用字規範》（南寧亭子平話）.txt',
        'v_nbdict_201705_bw.txt': '2017年詹伯慧、張振興《漢語方言學大詞典》（南寧亭子平話）.txt',
        'tab_nbdict_2021_bw.txt': '2021年Leimaau《單字音零散資料匯總》（南寧亭子平話）.txt',
        'v_1856yh_single_extend.txt': '1856年《英華分韻撮要》.txt',
        'tab_nbdict_1997_phrase.txt': '1997年楊煥典《南寧話音檔》分類詞表.txt',
        'tab_nbdict_1998_phrase.txt': '1998年《廣西通誌·漢語方言誌》（南寧白話）分類詞表.txt',
        'tab_nbdict_2007_phrase.txt': '2007年謝建猷《廣西漢語方言研究》（南寧白話）分類詞表.txt',
        'tab_nbdict_2008_phrase.txt': '2008年林亦《廣西南寧白話研究》分類詞表.txt',
        'tab_nbdict_2021_phrase.txt': '2021年Leimaau《詞彙零散資料匯總》（南寧白話）.txt',
        'tab_nbdict_2021_bw_phrase.txt': '2021年Leimaau《詞彙零散資料匯總》（南寧亭子平話）.txt',
        'tab_nb_zingjam_phrase.txt': '南寧白話分類詞表.txt',
        'v_xiandaihanyu_phrase.txt': '現代漢語詞彙表（南寧白話和南寧亭子平話）.txt',
        'v_xiandaihanyu_phrase_book.txt': '《現代漢語詞典》南寧白話讀音表.txt',
        'v_xiandaihanyu_phrase_book_bw.txt': '《現代漢語詞典》南寧亭子平話讀音表.txt'
    }
    
    for old_name, new_name in rename_mappings.items():
        old_path = TEMP_DIR / old_name
        new_path = TEMP_DIR / new_name
        
        if old_path.exists():
            # 如果目标文件已存在，先删除它
            if new_path.exists():
                try:
                    new_path.unlink()
                    print(f"已删除已存在的文件: {new_name}")
                except Exception as e:
                    print(f"删除文件 {new_name} 时出错: {str(e)}")
                    continue
            
            try:
                old_path.rename(new_path)
                print(f"已重命名: {old_name} -> {new_name}")
            except Exception as e:
                print(f"重命名文件 {old_name} 时出错: {str(e)}")
                continue

def get_file_category(file_name: str) -> Optional[str]:
    """根据文件名确定文件类别，使用优先级规则"""
    for category, keywords in FILE_CATEGORIES:
        if any(keyword in file_name for keyword in keywords):
            return category
    return None

def copy_files_to_targets(source_dir: Path, txt_files: List[str]) -> None:
    """将处理好的文件复制到目标目录"""
    print("\n开始复制文件到目标目录...")
    
    # 检查目标目录是否存在
    for target_dir in OUTPUT_DIRS.values():
        if not target_dir.exists():
            raise ValueError(f"目标目录不存在: {target_dir}")
    
    for file_name in txt_files:
        source_path = source_dir / file_name
        if not source_path.is_file():
            continue
            
        try:
            category = get_file_category(file_name)
            if category:
                if category == 'dict':
                    print(f"保持文件在原目录: {file_name}")
                    continue
                    
                target_dir = OUTPUT_DIRS[category]
                shutil.copy2(source_path, target_dir)
                print(f"已复制到{category}目录: {file_name}")
            else:
                print(f"警告: 无法确定文件类别: {file_name}")
        except Exception as e:
            print(f"复制文件 {file_name} 时出错: {str(e)}")
            continue

def main():
    try:
        print("正在运行 expbat.bat ...")
        subprocess.run(str(bat_path), shell=True, cwd=BAT_DIR, check=True)
    except subprocess.CalledProcessError as e:
        print("bat 执行出错，返回码：", e.returncode)
        print("错误信息：", e)
        sys.exit(1)
    except FileNotFoundError:
        print(f"错误: 找不到文件 {bat_path}")
        sys.exit(1)

    # 处理临时目录中的所有文本文件
    process_text_files(TEMP_DIR)
    
    # 合并文件生成南寧白話常用字讀音表
    combine_files(
        TEMP_DIR / '南寧白話常用字讀音表.txt',
        [TEMP_DIR / f for f in ['dict_nb.txt', 'dict_nb_samp.txt', 'dict_trad_simp_nb.txt']]
    )
    
    # 合并文件生成南寧白話建議讀音表
    combine_files(
        TEMP_DIR / '南寧白話建議讀音表.txt',
        [TEMP_DIR / f for f in ['dict_nb_zingjam.txt', 'dict_nb_zingjam_samp.txt', 'dict_trad_simp_nb_zingjam.txt']]
    )
    
    # 合并文件生成南寧平話常用字讀音表
    combine_files(
        TEMP_DIR / '南寧平話常用字讀音表.txt',
        [TEMP_DIR / f for f in ['dict_nb_bw.txt', 'dict_nb_samp_bw.txt', 'dict_trad_simp_nb_bw.txt']]
    )
    
    # 合并文件生成南寧平話建議讀音表
    combine_files(
        TEMP_DIR / '南寧平話建議讀音表.txt',
        [TEMP_DIR / f for f in ['dict_nb_zingjam_bw.txt', 'dict_nb_zingjam_samp_bw.txt', 'dict_trad_simp_nb_zingjam_bw.txt']]
    )
    
    # 重命名文件
    rename_files()

    # 获取所有 txt 文件
    txt_files = [f.name for f in TEMP_DIR.glob('*.txt')]
    if not txt_files:
        raise ValueError("源目录中没有找到 TXT 文件")

    # 复制文件到目标目录
    copy_files_to_targets(TEMP_DIR, txt_files)

    # 调用convert_txt_to_mdx.py脚本
    convert_script = Path(r'E:\LocalRepository\github\dict-store-txt\temp\writemdict-master\convert_txt_to_mdx.py')
    if convert_script.exists():
        print("\n开始调用convert_txt_to_mdx.py脚本...")
        try:
            result = subprocess.run(['python', str(convert_script)], 
                                 capture_output=True, 
                                 text=True, 
                                 check=True)
            print("脚本执行成功！")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print("脚本执行失败！")
            print(f"错误信息: {e.stderr}")
        except Exception as e:
            print(f"执行脚本时发生错误: {str(e)}")
    else:
        print(f"错误: 找不到脚本文件 {convert_script}")

if __name__ == '__main__':
    main()