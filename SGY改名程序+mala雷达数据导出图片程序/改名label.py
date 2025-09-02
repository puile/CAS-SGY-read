import os

# 设置labels和images的文件夹路径
labels_path = r'E:\Mayihang\雷达数据集(图像)\24.3.20更新雷达数据\400MHz_v1\labels'
images_path = r'E:\Mayihang\雷达数据集(图像)\24.3.20更新雷达数据\400MHz_v1\images'

# 初始化一个计数器
counter = 1

# 遍历labels文件夹中的所有.txt文件
for label_file in sorted(os.listdir(labels_path)):
    if label_file.endswith('.txt'):
        # 构建相应的.png文件名和路径
        image_file_name = label_file.replace('.txt', '.png')
        image_file_path = os.path.join(images_path, image_file_name)
        label_file_path = os.path.join(labels_path, label_file)

        # 检查这个.png文件是否存在
        if os.path.exists(image_file_path):
            # 如果存在，执行重命名操作
            new_image_file_name = f"400_{counter}.png"
            new_label_file_name = f"400_{counter}.txt"
            new_image_file_path = os.path.join(images_path, new_image_file_name)
            new_label_file_path = os.path.join(labels_path, new_label_file_name)

            # 重命名文件
            os.rename(image_file_path, new_image_file_path)
            os.rename(label_file_path, new_label_file_path)
            print(f"Renamed {image_file_name} to {new_image_file_name}")
            print(f"Renamed {label_file} to {new_label_file_name}")

            # 增加计数器
            counter += 1
