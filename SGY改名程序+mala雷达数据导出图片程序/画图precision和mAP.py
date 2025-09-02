import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use('TKAgg')
# 读取第一个文件的数据
file_path1 = r'D:\pycode\yolov5-master\runs\train\6.18\exp\results.csv'
data1 = pd.read_csv(file_path1)
data1.columns = data1.columns.str.strip()

# 读取第二个文件的数据
file_path2 = r'D:\pycode\yolov5-master\runs\train\6.18\exp2\results.csv'
data2 = pd.read_csv(file_path2)
data2.columns = data2.columns.str.strip()

# 计算训练损失（框损失、对象损失、类别损失的总和）
train_loss1 = data1['train/box_loss'] + data1['train/obj_loss'] + data1['train/cls_loss']
train_loss2 = data2['train/box_loss'] + data2['train/obj_loss'] + data2['train/cls_loss']

# 获取损失和精确度的最大最小值，用于设置统一的纵坐标范围
loss_min = min(train_loss1.min(), train_loss2.min())
loss_max = max(train_loss1.max(), train_loss2.max())
precision_min = min(data1['metrics/precision'].min(), data2['metrics/precision'].min())
precision_max = max(data1['metrics/precision'].max(), data2['metrics/precision'].max())

# 创建一个Figure和一个subplot
fig, ax = plt.subplots(figsize=(15, 8))

# 绘制第一个文件的训练损失和精确度
color1 = 'tab:red'
ax.set_xlabel('Epoch', fontsize=30)
ax.set_ylabel('Train Loss', color=color1, fontsize=30)
train_loss_line1, = ax.plot(data1['epoch'], train_loss1, color=color1, label='Train Loss', linewidth=3)
ax.tick_params(axis='y', labelcolor=color1, labelsize=16)

# 绘制第一个文件的精确度
color2 = 'tab:blue'
ax2 = ax.twinx()  # 使用相同的x轴
ax2.set_ylabel('Precision', color=color2, fontsize=30)
precision_line1, = ax2.plot(data1['epoch'], data1['metrics/precision'], color=color2, label='Precision', linestyle='--', linewidth=3)
ax2.tick_params(axis='y', labelcolor=color2, labelsize=16)

# 绘制第二个文件的训练损失和精确度
train_loss_line2, = ax.plot(data2['epoch'], train_loss2, color='tab:green', label='Train Loss (with Transfer Learning)', linewidth=3)
precision_line2, = ax2.plot(data2['epoch'], data2['metrics/precision'], color='tab:orange', label='Precision (with Transfer Learning)', linestyle='--', linewidth=3)

# 创建统一的图例
lines = [train_loss_line1, precision_line1, train_loss_line2, precision_line2]
labels = ['Train Loss', 'Precision', 'Train Loss (with Transfer Learning)', 'Precision (with Transfer Learning)']
fig.legend(lines, labels, loc='center', fontsize=10)

fig.tight_layout()  # 调整布局以避免标签被裁切
plt.show()