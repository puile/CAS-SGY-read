import os
import xml.etree.ElementTree as ET


def load_classes(classes_file):
    with open(classes_file, 'r') as file:
        classes = file.read().strip().split('\n')
    return {name: idx for idx, name in enumerate(classes)}


def convert_annotation(xml_file, output_file, image_size, classes):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    width, height = image_size

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, 'w') as file:
        for obj in root.findall('object'):
            cls_name = obj.find('name').text
            cls_idx = 1  # Default to -1 if class name not found
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('ymin').text),
                 float(xmlbox.find('xmax').text), float(xmlbox.find('ymax').text))
            bb = convert((width, height), b)
            file.write(f"{cls_idx} {bb[0]} {bb[1]} {bb[2]} {bb[3]}\n")


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[2]) / 2.0
    y = (box[1] + box[3]) / 2.0
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def main(xml_dir, img_dir, output_dir, classes_file):
    classes = load_classes(classes_file)
    for xml_file in os.listdir(xml_dir):
        if xml_file.endswith('.xml'):
            base_filename = os.path.splitext(xml_file)[0]
            img_path = os.path.join(img_dir, f"{base_filename}.jpg")
            output_path = os.path.join(output_dir, f"{base_filename}.txt")
            image_size = (300, 300)  # Replace with actual image size fetching code
            convert_annotation(os.path.join(xml_dir, xml_file), output_path, image_size, classes)


if __name__ == '__main__':
    xml_dir = r'E:\Mayihang\迁移数据库\钢筋GPR数据库\Annotations'
    img_dir = r'E:\Mayihang\迁移数据库\钢筋GPR数据库\JPEGImages'
    output_dir = r'E:\Mayihang\迁移数据库\钢筋GPR数据库\Labels'
    classes_file = r'E:\Mayihang\迁移数据库\钢筋GPR数据库\classes.txt'

    main(xml_dir, img_dir, output_dir, classes_file)
