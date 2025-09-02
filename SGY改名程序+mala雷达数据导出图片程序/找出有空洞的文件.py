import os
import glob

# 定义路径
image_dir = r'E:\Mayihang\迁移数据库\钢筋GPR数据库\JPEGImages'
label_dir = r'E:\Mayihang\迁移数据库\钢筋GPR数据库\Labels'


def contains_class1(label_file):
    """检查标签文件是否包含类别为1的对象"""
    with open(label_file, 'r') as f:
        for line in f:
            class_id = int(line.split()[0])
            if class_id == 1:
                return True
    return False


# 遍历标签文件
for label_path in glob.glob(os.path.join(label_dir, '*.txt')):
    if contains_class1(label_path):
        # 构建新的标签文件名
        base_name = os.path.basename(label_path)
        name_without_ext = os.path.splitext(base_name)[0]
        new_label_name = f"1_{name_without_ext}.txt"
        new_label_path = os.path.join(label_dir, new_label_name)

        # 重命名标签文件
        os.rename(label_path, new_label_path)

        # 查找和重命名对应的图像文件
        image_path = os.path.join(image_dir, name_without_ext + '.jpg')
        if os.path.exists(image_path):
            new_image_name = f"1_{name_without_ext}.jpg"
            new_image_path = os.path.join(image_dir, new_image_name)
            os.rename(image_path, new_image_path)

print("重命名完成。")
