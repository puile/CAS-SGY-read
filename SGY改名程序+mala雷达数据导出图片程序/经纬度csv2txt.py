import pandas as pd


def convert_excel_to_txt(excel_file_path, txt_file_path):
    # 读取Excel文件
    df = pd.read_excel(excel_file_path, usecols=['A', 'B','C'])

    with open(txt_file_path, 'w') as txt_file:
        for index, row in df.iterrows():
            latitude = row['A']  # A列的数据
            longitude = row['B']  # B列的数据
            time = row['C']
            # 写入txt文件，使用逗号分隔
            txt_file.write(f"{latitude},{longitude},{time}\n")


# 文件路径
excel_file_path = r"D:\pycode\SGY改名程序+mala雷达数据导出图片程序\海珠区滨江西路gps&采样时间_去程.xlsx"
txt_file_path = r"D:\pycode\SGY改名程序+mala雷达数据导出图片程序\xunzhao.txt"

# 转换Excel到TXT
convert_excel_to_txt(excel_file_path, txt_file_path)
