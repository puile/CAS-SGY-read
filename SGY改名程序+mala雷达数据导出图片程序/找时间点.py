import math


def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # 地球半径，单位：公里
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c  # 距离，单位：公里
    return distance


def find_points_in_distance_range(file_path, min_distance, max_distance):
    points_in_range = []
    total_distance = 0.0
    previous_point = None

    with open(file_path, 'r') as file:
        for line in file:
            lat, lon = map(float, line.strip().split(','))

            if previous_point is not None:
                distance = haversine(previous_point[0], previous_point[1], lat, lon)
                total_distance += distance * 1000  # 转换为米

                if min_distance <= total_distance <= max_distance:
                    points_in_range.append((lat, lon))

            previous_point = (lat, lon)

    return points_in_range


# 文件路径
file_path = r"D:\pycode\SGY改名程序+mala雷达数据导出图片程序\海珠区滨江西路gps&采样时间_去程.txt"

# 查找2900米到2970米之间的经纬度点
min_distance = 2850
max_distance = 2890
points_in_range = find_points_in_distance_range(file_path, min_distance, max_distance)

# 输出结果
for i, point in enumerate(points_in_range, start=1):
    print(f"Point {i}: Latitude = {point[0]}, Longitude = {point[1]}")
