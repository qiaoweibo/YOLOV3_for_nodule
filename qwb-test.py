# -*- coding: utf-8 -*-
# import torch
# print(torch.cuda.is_available())
#
#
#
# /home/weidu/qwb/PyTorch-YOLOv3-master/data/coco/images/train2014/COCO_train2014_000000000009.jpg
#
#
# data/VOC/OriginalImages/0001.png
#
#
# /home/weidu/qwb/PyTorch-YOLOv3-master/data/VOC/OriginalImages/0001.png


# t = open("/home/weidu/qwb/PyTorch-YOLOv3-master/data/VOC/ImageSets/Main/val.txt", "r")
# list = []
# for line in t.readlines():
#     load = "/home/weidu/qwb/PyTorch-YOLOv3-master/data/VOC/OriginalImages/"+line+".png\n"
#     print(load)
#     list.append(load)
#
# a = open("/home/weidu/qwb/PyTorch-YOLOv3-master/data/VOC/val.txt", "w")
# a.writelines(list)

# /home/weidu/qwb/PyTorch-YOLOv3-master/data/cocoq/images/trainval2014/0001.png



########################

import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

sets = [('', 'train'), ('', 'val'), ('', 'test')]

classes = ["nodule"]


def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(year, image_id):
    in_file = open('/home/weidu/qwb/转化过的Luna16数据集/VOC%s/Annotations/%s.xml' % (year, image_id))
    out_file = open('/home/weidu/qwb/转化过的Luna16数据集/VOC%s/labels/%s.txt' % (year, image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        # difficult = 0
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


wd = getcwd()

for year, image_set in sets:
    if not os.path.exists('data/VOC%s/labels/' % (year)):
        os.makedirs('data/VOC%s/labels/' % (year))
    image_ids = open('data/VOC%s/ImageSets/Main/%s.txt' % (year, image_set)).read().strip().split()
    list_file = open('%s_%s.txt' % (year, image_set), 'w')
    for image_id in image_ids:
        list_file.write('%s/data/VOC%s/JPEGImages/%s.png\n' % (wd, year, image_id))
        convert_annotation(year, image_id)
    list_file.close()
#
# os.system("cat 2007_train.txt 2007_val.txt 2012_train.txt 2012_val.txt > train.txt")
# os.system("cat 2007_train.txt 2007_val.txt 2007_test.txt 2012_train.txt 2012_val.txt > train.all.txt")
#
#
#






#下面的代码是生成VOC2012的labels
# import xml.etree.ElementTree as ET
# import pickle
# import os
# from os import listdir, getcwd
# from os.path import join
#
# sets=[('2012', 'train'), ('2012', 'val'), ('2007', 'train'), ('2007', 'val'), ('2007', 'test')]
#
# classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
#
#
# def convert(size, box):
#     dw = 1./size[0]
#     dh = 1./size[1]
#     x = (box[0] + box[1])/2.0
#     y = (box[2] + box[3])/2.0
#     w = box[1] - box[0]
#     h = box[3] - box[2]
#     x = x*dw
#     w = w*dw
#     y = y*dh
#     h = h*dh
#     return (x,y,w,h)
#
# def convert_annotation(year, image_id):
#     in_file = open('data/VOCdevkit/VOC%s/Annotations/%s.xml'%(year, image_id))
#     out_file = open('data/VOCdevkit/VOC%s/labels/%s.txt'%(year, image_id), 'w')
#     tree=ET.parse(in_file)
#     root = tree.getroot()
#     size = root.find('size')
#     w = int(size.find('width').text)
#     h = int(size.find('height').text)
#
#     for obj in root.iter('object'):
#         difficult = obj.find('difficult').text
#         cls = obj.find('name').text
#         if cls not in classes or int(difficult) == 1:
#             continue
#         cls_id = classes.index(cls)
#         xmlbox = obj.find('bndbox')
#         b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
#         bb = convert((w,h), b)
#         out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
#
# wd = getcwd()
#
# for year, image_set in sets:
#     if not os.path.exists('data/VOCdevkit/VOC%s/labels/'%(year)):
#         os.makedirs('data/VOCdevkit/VOC%s/labels/'%(year))
#     image_ids = open('data/VOCdevkit/VOC%s/ImageSets/Main/%s.txt'%(year, image_set)).read().strip().split()
#     list_file = open('%s_%s.txt'%(year, image_set), 'w')
#     for image_id in image_ids:
#         list_file.write('%s/data/VOCdevkit/VOC%s/JPEGImages/%s.jpg\n'%(wd, year, image_id))
#         convert_annotation(year, image_id)
#     list_file.close()





