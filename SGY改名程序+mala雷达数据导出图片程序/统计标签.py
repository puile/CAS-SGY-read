import os
from collections import Counter

# 替换为你的 YOLO 标签文件夹路径
label_folder = r"E:\MaYihang\道路病害数据\雷达图像（已经标注）24.4.11\500MHzall\labels"

# 检查标签文件夹是否存在
if not os.path.exists(label_folder):
    print("标签文件夹不存在，请检查路径。")
else:
    print(f"正在统计标签文件夹中的文件：{label_folder}")

# 初始化计数器
class_counts = Counter()

# 遍历所有标签文件
for label_file in os.listdir(label_folder):
    if label_file.endswith(".txt"):  # 确保是标签文件
        file_path = os.path.join(label_folder, label_file)
        print(f"读取文件：{file_path}")  # 调试信息
        with open(file_path, "r") as file:
            for line in file:
                if line.strip():  # 确保行不为空
                    class_id = line.split()[0]  # 提取类别 ID
                    print(f"检测到类别 ID：{class_id}")  # 调试信息
                    class_counts[class_id] += 1

# 输出统计结果
if class_counts:
    print("\n统计结果：")
    for class_id, count in sorted(class_counts.items()):
        print(f"Class {class_id}: {count} objects")
else:
    print("未在标签文件中检测到任何目标。")
