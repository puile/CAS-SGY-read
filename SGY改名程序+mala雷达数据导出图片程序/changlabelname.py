import os

# 图像和标签的根目录
image_root = "E:\Mayihang\雷达数据集(图像)\\24.3.20更新雷达数据\\500MHzall\images"
label_root = "E:\Mayihang\雷达数据集(图像)\\24.3.20更新雷达数据\\500MHzall\labels"


# 获取图像目录下所有的.png文件
images = [f for f in os.listdir(image_root) if f.endswith('.jpg')]
# 获取标签目录下所有的.txt文件
labels = [f for f in os.listdir(label_root) if f.endswith('.txt')]
i=0
# 对每个标签文件执行操作
for label_file in labels:
    # 构建不包含后缀的文件名，用于检查对应的图像文件是否存在
    base_name = label_file.replace('.txt', '')
    img_file = base_name + '.jpg'

    # 检查对应的图像文件是否存在
    if img_file in images:
        # 构造原始和新的完整文件路径
        original_img_path = os.path.join(image_root, img_file)
        new_img_path = os.path.join(image_root, f"500_{i}.jpg")

        original_label_path = os.path.join(label_root, label_file)
        new_label_path = os.path.join(label_root, f"500_{i}.txt")

        # 重命名图像文件和标签文件
        os.rename(original_img_path, new_img_path)
        os.rename(original_label_path, new_label_path)
        i=i+1
print("文件重命名完成。")
