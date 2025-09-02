import os

# 图像所在的路径
images_path = 'E:\\Mayihang\\雷达数据集(图像)\\更新数据(没有分训练集和验证集)\\none'

# 标签保存的路径
labels_path = 'E:\\Mayihang\\雷达数据集(图像)\\更新数据(没有分训练集和验证集)\\nonelabel'

# 确保标签目录存在
os.makedirs(labels_path, exist_ok=True)

# 获取图像目录中所有的图像文件
image_files = [f for f in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, f))]

# 为每个图像文件创建一个对应的空的.txt标签文件
for image_file in image_files:
    # 构建新的文件名，将图像的扩展名替换为.txt
    label_file = os.path.splitext(image_file)[0] + '.txt'
    # 创建并打开标签文件
    with open(os.path.join(labels_path, label_file), 'w') as f:
        # 由于需要生成空文件，这里不需要写入任何内容
        pass

print(f"已为{len(image_files)}个图像文件生成空的标签文件。")
