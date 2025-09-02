import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from PIL import Image
from readmala2 import readmala2
import cv2
import time
import matplotlib.colors as mcolors
import ReadMALA

start_time=time.time()
matplotlib.use('TkAgg')
dataFolder = r'F:\2023_1_30\400MHzrawdata\ASCII'
outputpath = r'F:\2023_1_30\400MHzrawdata\ASCII\images'
# file = 'E:/Mayihang/2023_1_30/zhengding/ASCII/20230224ZHENGDINGHENGZHOUBEIJIE_001_A1'
file_list = [file for file in os.listdir(dataFolder) if file.endswith('.RAD')]
os.chdir(dataFolder)
for file_name in file_list:
    file_name1 = os.path.splitext(file_name)[0]
    folder_name = os.path.join(outputpath, file_name1)
    file_name=os.path.join(dataFolder,file_name1)
    os.makedirs(outputpath, exist_ok=True)
    # os.makedirs(folder_name,exist_ok=True)

    header,Data = readmala2(file_name)
    # Data = np.transpose(Data)
    start = 0
    distance = header['DISTANCE_INTERVAL']
    # 计算数组的最大值和最小值
    max_val = np.max(Data)
    min_val = np.min(Data)
    max_val=max(abs(max_val),abs(min_val))
    # 归一化到 [-1, 1]
    Data = Data.astype(float)
    Data = Data/max_val
    Data=Data-np.mean(Data)
    L=20
    d = int((L-3) / distance)
    # 17米对应的雷达道数

    if Data.shape[0]*distance<L:
        Data=cv2.resize(Data, (600, int(Data.shape[0] * distance / L * 600)))
        meandata = np.mean(Data)
        colVector = meandata * np.ones((600, 600 - Data.shape[0]))  # 生成 600 行 1 列每个元素都为 meandata 的列向量
        Data=np.transpose(Data)
        Data = np.concatenate((Data, colVector), axis=1)
        plt.imshow(Data, cmap='gray', vmin=-0.3, vmax=0.3)
        plt.axis('off')
        # plt.savefig(os.path.join(folder_name, file_name1 + '.png'), bbox_inches='tight', pad_inches=0, dpi=170)
        plt.savefig(os.path.join(outputpath, file_name1 + '.png'), bbox_inches='tight', pad_inches=0, dpi=170)
        plt.clf()
    else:
        i=0

        while (int(L / header['DISTANCE_INTERVAL']) + start < Data.shape[0]):

            Data1 = Data[start:int(L / header['DISTANCE_INTERVAL']) + start,:]
            start = start + d
            Data1 = np.transpose(Data1)
            Data1=cv2.resize(Data1,(600,600))

            plt.imshow(Data1, cmap='gray',vmin=-0.3,vmax=0.3)
            plt.axis('off')
            # plt.savefig(os.path.join(folder_name, '('+"{:05d}".format(i)+')'+file_name1+ '.png'),bbox_inches='tight',pad_inches = 0,dpi=170)
            plt.savefig(os.path.join(outputpath, '(' + "{:05d}".format(i) + ')' + file_name1 + '.png'),bbox_inches='tight', pad_inches=0, dpi=170)
            plt.clf()
            i=i+1
        if int(20 / header['DISTANCE_INTERVAL']) + start>Data.shape[0]:
            Data1 = cv2.resize(Data[start:Data.shape[0],:], (600, int((Data.shape[0] -start)* distance / L * 600)))
            meandata = np.mean(Data1)
            colVector = meandata * np.ones((600, 600 - Data1.shape[0]))  # 生成 600 行 1 列每个元素都为 meandata 的列向量
            Data1= np.transpose(Data1)
            Data1 = np.concatenate((Data1, colVector), axis=1)
            plt.imshow(Data1, cmap='gray', vmin=-0.3, vmax=0.3)
            plt.axis('off')
            # plt.savefig(os.path.join(folder_name, '('+"{:05d}".format(i)+')'+file_name1 +"##" + '.png'),bbox_inches='tight',pad_inches = 0,dpi=170)
            plt.savefig(os.path.join(outputpath, '(' + "{:05d}".format(i) + ')' + file_name1 + "##" + '.png'),
                        bbox_inches='tight', pad_inches=0, dpi=170)
            plt.clf()
    end_time=time.time()
print("总共运行时间是:{}秒".format(-(start_time-end_time)))

#
# start_col = int(160/0.05)
# end_col = int(210/0.05)
# # 设置图像尺寸，使图像更长
# plt.figure(figsize=(24, 6))  # 可以根据需要调整尺寸
# # 显示图像，设置颜色映射和值的范围
# plt.imshow(Data[:, start_col:end_col], cmap='gray', vmin=-0.1, vmax=0.1,aspect='auto')
# # 设置坐标轴范围
# # 横坐标为 160 到 210 米
# # 纵坐标为 0 到 50 纳秒
# plt.xticks(ticks=np.linspace(0, end_col-start_col, 6), labels=np.linspace(160, 210, 6))
# plt.yticks(ticks=np.linspace(0, Data.shape[0], 6), labels=np.linspace(0, 50, 6))
# # 设置坐标轴标签
# plt.xlabel('Distance (m)',fontsize=14)
# plt.ylabel('Time (ns)',fontsize=14)
# # 显示图像
# plt.show()
#
#
# import numpy as np
# import matplotlib.pyplot as plt
# from PIL import Image
# # 读取图片
# image_path = r"D:\mayihang\shengzheng_radardata\LYL_processing\images\LG-20230515-LYL_002_00\Screenshot 2024-06-23 163436.png"
# image = Image.open(image_path)
# # 转换为可用于matplotlib的格式
# image_for_plot = np.array(image)
# # 设置图像尺寸
# plt.figure(figsize=(25, 6))
# # 显示图片并设置坐标轴范围
# # 这里的坐标范围需要根据您的具体需求进行设置
# # 例如：extent=[0, 10, 0, 5] 表示 x 轴从 0 到 10，y 轴从 0 到 5
# plt.imshow(image_for_plot[:,:,:], extent=[0, 27, 50, 0],aspect='auto')
# # 设置坐标轴标签
# plt.xlabel('Distance(m)',fontsize=20)
# plt.ylabel('Time(ns)',fontsize=20)
# plt.tick_params(axis='x', labelsize=14)
# plt.tick_params(axis='y', labelsize=14)
# # 显示图片
# plt.show()
