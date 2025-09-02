import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# 输入和输出文件夹路径
input_folder = r'F:\02processingdata\07lhq\jsl\ASCII\images\LHQ-20230505-JSL_001-P_00\results'
output_file_with_coords = r'F:\02processingdata\07lhq\jsl\ASCII\images\LHQ-20230505-JSL_001-P_00\results\imgsave_with_coords.png'

# 获取所有 .png 图像文件并排序
image_files = sorted([f for f in os.listdir(input_folder) if f.endswith('.png')])
L = 20
overlap_ratio = 3 / L

# 确保有足够的图像文件进行拼接
if len(image_files) < 2:
    print("图像文件不足以进行拼接")
    exit()

# 读取第一张图片作为基准
base_image = cv2.imread(os.path.join(input_folder, image_files[0]))

# 遍历后续的图片进行拼接
for i in range(1, len(image_files)):
    image = cv2.imread(os.path.join(input_folder, image_files[i]))

    # 计算重叠区域的像素数量
    overlap_pixels = int(image.shape[1] * overlap_ratio)

    # 融合重叠区域
    if overlap_pixels > 0:
        blended_region = cv2.addWeighted(
            base_image[:, -overlap_pixels:], 0.5,
            image[:, :overlap_pixels], 0.5, 0
        )
        # 将融合的区域放回基准图像的最右侧
        base_image[:, -overlap_pixels:] = blended_region

    # 拼接当前图像的非重叠部分
    base_image = cv2.hconcat([base_image, image[:, overlap_pixels:]])

# 保存拼接后的图片（无坐标轴版本）
output_file = os.path.join(input_folder, "imgsave.png")
cv2.imwrite(output_file, base_image)
print("拼接后的图片已保存到:", output_file)