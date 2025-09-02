# -*- coding: utf-8 -*-
# @Time    : 2024/10/31 11:38
# @Author  : Pupil
# @FileName: test.py
# @Software: PyCharm
# @Cnblogs ：https://github.com/puile
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

start_time = time.time()
matplotlib.use('TkAgg')
dataFolder = r'F:\MaYihang\2023SZdata\void\200MHz\ASCII'
outputpath = r'F:\MaYihang\2023SZdata\void\200MHz\ASCII\images1'
file_list = [file for file in os.listdir(dataFolder) if file.endswith('.RAD')]
os.chdir(dataFolder)

for file_name in file_list:
    file_name1 = os.path.splitext(file_name)[0]
    folder_name = os.path.join(outputpath, file_name1)
    file_name = os.path.join(dataFolder, file_name1)
    os.makedirs(outputpath, exist_ok=True)

    header, Data = readmala2(file_name)
    start = 0
    distance = header['DISTANCE_INTERVAL']
    max_val = max(abs(np.max(Data)), abs(np.min(Data)))
    Data = Data.astype(float) / max_val
    L = 20
    d = int((L - 3) / distance)

    if Data.shape[0] * distance < L:
        Data = cv2.resize(Data, (600, int(Data.shape[0] * distance / L * 600)))
        meandata = np.mean(Data)
        colVector = meandata * np.ones((600, 600 - Data.shape[0]))
        Data = np.transpose(Data)
        Data = np.concatenate((Data, colVector), axis=1)

        vmin, vmax = np.percentile(Data, [5, 95])
        plt.imshow(Data, cmap='gray', vmin=vmin, vmax=vmax)
        plt.axis('off')
        plt.savefig(os.path.join(outputpath, file_name1 + '.png'), bbox_inches='tight', pad_inches=0, dpi=170)
        plt.clf()
    else:
        i = 0
        while (int(L / distance) + start < Data.shape[0]):
            Data1 = Data[start:int(L / distance) + start, :]
            start += d
            Data1 = np.transpose(Data1)
            Data1 = cv2.resize(Data1, (600, 600))

            vmin, vmax = np.percentile(Data1, [5, 95])
            plt.imshow(Data1, cmap='gray', vmin=vmin, vmax=vmax)
            plt.axis('off')
            plt.savefig(os.path.join(outputpath, '(' + "{:05d}".format(i) + ')' + file_name1 + '.png'), bbox_inches='tight', pad_inches=0, dpi=170)
            plt.clf()
            i += 1

        if int(L / distance) + start > Data.shape[0]:
            Data1 = cv2.resize(Data[start:Data.shape[0], :], (600, int((Data.shape[0] - start) * distance / L * 600)))
            meandata = np.mean(Data1)
            colVector = meandata * np.ones((600, 600 - Data1.shape[0]))
            Data1 = np.transpose(Data1)
            Data1 = np.concatenate((Data1, colVector), axis=1)

            vmin, vmax = np.percentile(Data1, [5, 95])
            plt.imshow(Data1, cmap='gray', vmin=vmin, vmax=vmax)
            plt.axis('off')
            plt.savefig(os.path.join(outputpath, '(' + "{:05d}".format(i) + ')' + file_name1 + "##" + '.png'), bbox_inches='tight', pad_inches=0, dpi=170)
            plt.clf()

end_time = time.time()
print("总共运行时间是:{}秒".format(-(start_time - end_time)))
