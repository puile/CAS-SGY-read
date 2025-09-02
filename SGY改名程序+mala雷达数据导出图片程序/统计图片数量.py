# -*- coding: utf-8 -*-
# @Time    : 2024/11/24 20:20
# @Author  : Pupil
# @FileName: 统计图片数量.py
# @Software: PyCharm
# @Cnblogs ：https://www.github.com/puile
import os

# 替换为你的 YOLO 标签文件夹路径
label_folder = r"E:\MaYihang\道路病害数据\第一批深圳自归局数据标注\200Mhzdata\labels"

# 初始化计数器
annotated_images_count = 0

# 遍历标签文件
for label_file in os.listdir(label_folder):
    if label_file.endswith(".txt"):  # 确保是标签文件
        file_path = os.path.join(label_folder, label_file)
        with open(file_path, "r") as file:
            lines = file.readlines()
            if lines:  # 检查文件是否有内容
                annotated_images_count += 1

# 输出结果
print(f"有标注的图片数量：{annotated_images_count}")
