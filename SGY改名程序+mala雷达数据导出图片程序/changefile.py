import os
import shutil

from pypinyin import lazy_pinyin

def chinese_to_pinyin(chinese_str):
    """将中文字符串转换为拼音，并只保留前两个字母"""
    pinyin = lazy_pinyin(chinese_str)
    return ''.join([x[:1] for x in pinyin])

def find_sgy_files(src_folder):
    """找到所有.SGY文件并返回它们的绝对路径列表"""
    sgy_files = []
    for foldername, subfolders, filenames in os.walk(src_folder):
        for filename in filenames:
            if filename.lower().endswith('.sgy'):
                sgy_files.append(os.path.join(foldername, filename))
    return sgy_files

def custom_transform(part):
    """对路径的每一部分进行处理，中文转为拼音且保留每个拼音的前两个字符，非中文字符序列只保留前两个字符"""
    transformed_part = ""
    for c in part:
        if '\u4e00' <= c <= '\u9fff':  # 判断字符是否为中文
            # 中文字符转拼音，每个拼音只保留前两个字符
            transformed_part += ''.join(x[:1] for x in lazy_pinyin(c))
        else:
            # 非中文字符直接添加，后续进行截断处理
            transformed_part += c
    # 对非中文部分进行截断，只保留前两个字符
    non_chinese_transformed = ""
    for char_group in transformed_part.split():
        if char_group.isascii():  # 如果是非中文（基于ASCII判断）
            non_chinese_transformed += char_group[:6] # 只保留每组的前两个字符
        else:
            non_chinese_transformed += char_group  # 中文拼音保持不变
    return non_chinese_transformed

def extract_file_path_parts(file_path, num_parts=4):
    """从文件路径中提取倒数第三个和倒数第二个部分，进行自定义转换"""
    parts = file_path.split(os.path.sep)[-num_parts:-1]  # 提取倒数第三个和倒数第二个部分
    parts_transformed = [custom_transform(part) for part in parts]
    return '_'.join(parts_transformed)

def copy_and_rename(file_paths, dest_folder):
    """复制文件到目标文件夹，并在必要时重命名"""
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for file_path in file_paths:
        base_name = extract_file_path_parts(file_path)+os.path.basename(file_path)
        new_path = os.path.join(dest_folder, base_name)

        # 检查是否有同名文件存在，如果有，则进行重命名
        counter = 1
        while os.path.exists(new_path):
            name, ext = os.path.splitext(base_name)
            new_name = f"{name}_{counter}{ext}"
            new_path = os.path.join(dest_folder, new_name)
            counter += 1

        # 复制文件到新路径
        shutil.copy2(file_path, new_path)

if __name__=='__main__':
    # 源文件夹路径和目标文件夹路径
    src_folder = r'E:\Mayihang\深圳规自局项目'
    dest_folder = r'E:\Mayihang\radar_kotianyuan\xsj3-7\szzgj'

    # 找到所有.SGY文件并复制到目标文件夹中
    sgy_files = find_sgy_files(src_folder)
    copy_and_rename(sgy_files, dest_folder)
