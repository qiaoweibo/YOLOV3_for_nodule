
import cv2

image_name = r"/home/weidu/qwb/PyTorch-YOLOv3-master/data/coco/images/train2014/COCO_train2014_000000000009.jpg"

print('load %s as ...' % image_name)
img = cv2.imread(image_name)
sp = img.shape
print(sp)
sz1 = sp[0]  # height(rows) of image
sz2 = sp[1]  # width(colums) of image
sz3 = sp[2]  # channels
print('height: %d \nwidth: %d \nchannels: %d' % (sz1, sz2, sz3))




