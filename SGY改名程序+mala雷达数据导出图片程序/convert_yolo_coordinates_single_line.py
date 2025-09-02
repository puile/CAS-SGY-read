import os


def convert_yolo_coordinates_single_line(label_folder, output_folder, image_width, image_height):
    # 创建输出目录如果它不存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历目录中的所有文件
    for filename in os.listdir(label_folder):
        if filename.endswith(".txt"):
            input_path = os.path.join(label_folder, filename)
            output_path = os.path.join(output_folder, "converted_" + filename)
            with open(input_path, 'r') as file, open(output_path, 'w') as new_file:
                lines = file.readlines()
                # 准备存储所有坐标在一行
                all_coords = []
                for line in lines:
                    parts = line.strip().split()
                    if len(parts) == 5:
                        # 读取类别和归一化坐标
                        class_id, cx, cy, w, h = parts
                        cx, cy, w, h = float(cx), float(cy), float(w), float(h)

                        # 计算非归一化坐标
                        cx *= image_width
                        cy *= image_height
                        w *= image_width
                        h *= image_height

                        # 计算左下角和右上角坐标
                        x1 = int(cx - w / 2)
                        y1 = int(cy - h / 2)
                        x2 = int(cx + w / 2)
                        y2 = int(cy + h / 2)

                        # 添加坐标到列表
                        all_coords.extend([x1, y1, x2, y2])

                # 将所有坐标写入一行
                new_file.write(",".join(map(str, all_coords)) + "\n")


# 设置标签文件夹路径和图像尺寸
label_folder = 'E:\\yolov5-master\\runs\\detect\\exp8\\labels'
output_folder = 'E:\\yolov5-master\\runs\\detect\\exp8\\converted_labels'
image_width, image_height = 628, 628

convert_yolo_coordinates_single_line(label_folder, output_folder, image_width, image_height)
