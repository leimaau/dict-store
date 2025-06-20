import os
import datetime
import shutil
from pathlib import Path
from typing import List, Set, Tuple, Optional
from writemdict import MDictWriter


# 常量定义
Dict_DIR = Path(r'E:\LocalRepository\github\dict-store')
GOLDENDICT_DIR = Path(r'D:\Program Files2\GoldenDict\content\粤语\粤语字典')
OUTPUT_DIRS = {
    'yongxun': Dict_DIR / '邕潯片',
    'pinghua': Dict_DIR / '平話',
    'qingdai': Dict_DIR / '清代粵語'
}
# 文件分类规则（按优先级排序）
FILE_CATEGORIES: List[Tuple[str, Set[str]]] = [
    ('yongxun', {'白話', '楊煥典', '滕祖愛', '現代漢語詞彙表'}),
    ('pinghua', {'平話'}),
    ('qingdai', {'英華分韻撮要'}),
    ('dict', {'dict'})
]
# 获取当前脚本所在目录的上级目录（temp目录）的绝对路径
TEMP_DIR = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def get_file_category(file_name: str) -> Optional[str]:
    """根据文件名确定文件类别"""
    for category, keywords in FILE_CATEGORIES:
        if any(keyword in file_name for keyword in keywords):
            return category
    return None

def convert_txt_to_mdx(txt_file: Path, output_mdx: Path, output_mdd: Optional[Path] = None) -> None:
    """将txt文件转换为mdx格式"""
    dictionary = {}
    try:
        with open(txt_file, 'r', encoding='utf-8') as f:
            content = f.read()
            # 按 </>\n 分割成词条块
            entries = content.split('</>\n')
            for entry in entries:
                if entry.strip():  # 跳过空块
                    # 分割词条和解释
                    parts = entry.strip().split('\n', 1)
                    if len(parts) == 2:
                        key, value = parts
                        key = key.strip()
                        value = value.strip()
                        # 如果词条已存在，将新解释添加到列表中
                        if key in dictionary:
                            if isinstance(dictionary[key], list):
                                dictionary[key].append(value)
                            else:
                                dictionary[key] = [dictionary[key], value]
                        else:
                            dictionary[key] = value
            
            # 处理多义项，将它们合并成一个HTML条目
            for key in dictionary:
                if isinstance(dictionary[key], list):
                    # 为每个义项添加序号和分隔线（注释）
                    combined_value = ""
                    for i, value in enumerate(dictionary[key], 1):
                        # combined_value += f'<div style="margin-bottom: 10px;">'
                        # combined_value += f'<span style="color: #666;">{i}. </span>'
                        combined_value += value
                        # combined_value += '</div>'
                        if i < len(dictionary[key]):
                            # combined_value += '<hr style="border: 0; border-top: 1px solid #eee; margin: 10px 0;">'
                            combined_value += ''
                    dictionary[key] = combined_value
    except UnicodeDecodeError:
        print(f"Error: {txt_file} is not UTF-8 encoded. Please convert it to UTF-8 first.")
        return
    except Exception as e:
        print(f"Error reading {txt_file}: {str(e)}")
        return
    
    # 获取当前时间
    current_time = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # 创建 mdx 文件
    writer = MDictWriter(
        dictionary,
        title=txt_file.stem,
        description=f"<font size=5 color=blue>author:LeiMaau<br>version:{current_time}</font>",
        encoding="utf8"
    )
    
    try:
        with open(output_mdx, "wb") as outfile:
            writer.write(outfile)
        print(f"Successfully created MDX file: {output_mdx}")
    except Exception as e:
        print(f"Error writing {output_mdx}: {str(e)}")
        return

    # 如果指定了 MDD 文件，则处理资源文件
    if output_mdd:
        # 获取文件名（不含扩展名）作为子目录名
        res_dir = txt_file.parent / "res" / txt_file.stem
        if res_dir.exists():
            mdd_dict = {}
            # 支持的资源文件类型
            resource_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.css', '.js', '.mp3', '.wav', '.spx')
            
            for file_path in res_dir.glob('*'):
                if file_path.suffix.lower() in resource_extensions:
                    try:
                        with open(file_path, 'rb') as f:
                            mdd_dict[f"\\{file_path.name}"] = f.read()
                    except Exception as e:
                        print(f"Error reading {file_path.name}: {str(e)}")
            
            if mdd_dict:
                try:
                    # 创建 MDD 文件
                    mdd_writer = MDictWriter(
                        mdd_dict,
                        title=txt_file.stem,
                        description=f"Resource files for {txt_file.stem}",
                        is_mdd=True
                    )
                    with open(output_mdd, "wb") as outfile:
                        mdd_writer.write(outfile)
                    print(f"Successfully created MDD file: {output_mdd}")
                except Exception as e:
                    print(f"Error creating MDD file: {str(e)}")
        else:
            print(f"Warning: Resource directory not found at {res_dir}")

def copy_files_to_targets(source_dir: Path, mdx_mdd_files: List[str]) -> None:
    """将处理好的文件复制到目标目录"""
    print("\n开始复制文件到目标目录...")
    
    # 检查目标目录是否存在
    for target_dir in OUTPUT_DIRS.values():
        if not target_dir.exists():
            raise ValueError(f"目标目录不存在: {target_dir}")
    
    for file_name in mdx_mdd_files:
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

def copy_to_goldendict(source_dir: Path, files: List[str]) -> None:
    """将文件复制到GoldenDict目录"""
    print("\n开始复制文件到GoldenDict目录...")
    
    # 检查目标目录是否存在
    if not GOLDENDICT_DIR.exists():
        raise ValueError(f"GoldenDict目录不存在: {GOLDENDICT_DIR}")
    
    # 复制文件
    for file_name in files:
        source_path = source_dir / file_name
        if not source_path.is_file():
            print(f"跳过不存在的文件: {file_name}")
            continue
            
        try:
            target_path = GOLDENDICT_DIR / file_name
            shutil.copy2(source_path, target_path)
            print(f"已复制到GoldenDict目录: {file_name}")
        except Exception as e:
            print(f"复制文件 {file_name} 时出错: {str(e)}")
            continue
    
    print("GoldenDict目录复制完成")

def main() -> None:
    """主函数"""
    # 要处理的文件列表
    txt_files = [
        f for f in os.listdir(TEMP_DIR)
        if f.endswith('.txt') and 'dict' not in f.lower()
    ]

    # 需要生成 MDD 的文件列表
    mdd_files = {
        "南寧白話常用字讀音表.txt"
    }

    # 处理所有文件
    for txt_file in txt_files:
        txt_path = TEMP_DIR / txt_file
        if txt_path.exists():
            mdx_path = TEMP_DIR / txt_file.replace('.txt', '.mdx')
            mdd_path = TEMP_DIR / txt_file.replace('.txt', '.mdd') if txt_file in mdd_files else None
            
            print(f"\nProcessing {txt_file}...")
            convert_txt_to_mdx(txt_path, mdx_path, mdd_path)
            print(f"Conversion completed for {txt_file}")
        else:
            print(f"Error: {txt_file} not found in {TEMP_DIR}")

    # 获取所有 mdx/mdd 文件
    mdx_files = [f.name for f in TEMP_DIR.glob('*.mdx')]
    mdd_files = [f.name for f in TEMP_DIR.glob('*.mdd')]
    mdx_mdd_files = mdx_files + mdd_files
    
    if not mdx_mdd_files:
        raise ValueError("源目录中没有找到 mdx/mdd 文件")

    # 复制文件到目标目录
    copy_files_to_targets(TEMP_DIR, mdx_mdd_files)
    
    # 复制文件到GoldenDict目录
    copy_to_goldendict(TEMP_DIR, mdx_mdd_files)

if __name__ == '__main__':
    main()