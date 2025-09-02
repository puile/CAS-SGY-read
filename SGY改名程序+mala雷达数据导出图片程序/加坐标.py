import os
import cv2
import numpy as np

# 输入和输出文件夹路径
input_folder = r'F:\02processingdata\07lhq\jsl\ASCII\images\LHQ-20230505-JSL_001-P_02\results'
output_file_with_coords = os.path.join(input_folder, "imgsave_with_coords.png")

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

# 扩展画布来绘制坐标轴标签，并在四周添加黑色边框
padding_top = 100   # 顶部的黑色边框高度
padding_bottom = 100  # 底部的黑色边框高度
padding_left = 150  # 左侧的黑色边框宽度
padding_right = 150 # 右侧的黑色边框宽度

canvas_height = base_image.shape[0] + padding_top + padding_bottom
canvas_width = base_image.shape[1] + padding_left + padding_right

# 创建一个黑色画布
canvas = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)

# 将原始图像粘贴到新画布上
canvas[padding_top:padding_top + base_image.shape[0], padding_left:padding_left + base_image.shape[1]] = base_image

# 绘制 x 轴和 y 轴的刻度线和标签
# x 轴刻度每隔 640 个像素点绘制一个
x_ticks = np.arange(padding_left, padding_left + base_image.shape[1], 628)
y_ticks = np.linspace(padding_top, padding_top + base_image.shape[0], 6).astype(int)

# 设置 x 和 y 轴的刻度标签
x_tick_labels = [f"{i:.2f}" for i in np.linspace(0, 20 / 628 * base_image.shape[1], len(x_ticks))]
y_tick_labels = [f"{i:.0f}" for i in np.linspace(0, 50, len(y_ticks))]

# 绘制 x 轴刻度和标签
for x, label in zip(x_ticks, x_tick_labels):
    # 绘制刻度线
    cv2.line(canvas, (x, canvas_height - padding_bottom), (x, canvas_height - padding_bottom - 20), (255, 255, 255), 2)
    # 绘制刻度标签
    cv2.putText(canvas, label, (x - 15, canvas_height - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

# 绘制 y 轴刻度和标签
for y, label in zip(y_ticks, y_tick_labels):
    # 绘制刻度线
    cv2.line(canvas, (padding_left - 20, y), (padding_left, y), (255, 255, 255), 2)
    # 绘制刻度标签
    cv2.putText(canvas, label, (30, y + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

# 添加坐标轴标签
cv2.putText(canvas, "Distance (m)", (canvas_width // 2, canvas_height - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
cv2.putText(canvas, "Time (ns)", (0, canvas_height // 2), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)

# 保存带坐标轴的拼接图像
cv2.imwrite(output_file_with_coords, canvas)
print("带坐标轴的拼接图片已保存到:", output_file_with_coords)
