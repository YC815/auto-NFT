# mods
from PIL import Image
import os
import glob

count = 0
# list
a_pic = []
b_pic = []
c_pic = []
d_pic = []
e_pic = []
main_pic = []
for f in glob.glob(os.path.join("make-pic/a", "*")):
    a_pic.append(f)

for f in glob.glob(os.path.join("make-pic/b", "*")):
    b_pic.append(f)

for f in glob.glob(os.path.join("make-pic/c", "*")):
    c_pic.append(f)

for f in glob.glob(os.path.join("make-pic/d", "*")):
    d_pic.append(f)

for f in glob.glob(os.path.join("make-pic/e", "*")):
    e_pic.append(f)

for f in glob.glob(os.path.join("make-pic/main", "*")):
    main_pic.append(f)

# 統一圖片大小
max_size = (0, 0)
for path in a_pic + b_pic + c_pic + d_pic + e_pic + main_pic:
    with Image.open(path) as img:
        max_size = (max(max_size[0], img.width), max(max_size[1], img.height))

for main in range(len(main_pic)):
    for a in range(len(a_pic)):
        for b in range(len(b_pic)):
            for c in range(len(c_pic)):
                for d in range(len(d_pic)):
                    for e in range(len(e_pic)):
                        image1 = Image.open(main_pic[main]).convert(
                            'RGBA').resize(max_size)
                        image2 = Image.open(a_pic[a]).convert(
                            'RGBA').resize(max_size)
                        image3 = Image.open(b_pic[b]).convert(
                            'RGBA').resize(max_size)
                        image4 = Image.open(c_pic[c]).convert(
                            'RGBA').resize(max_size)
                        image5 = Image.open(d_pic[d]).convert(
                            'RGBA').resize(max_size)
                        image6 = Image.open(e_pic[e]).convert(
                            'RGBA').resize(max_size)
                        merged_image = Image.alpha_composite(image1, image2)
                        merged_image = Image.alpha_composite(
                            merged_image, image3)
                        merged_image = Image.alpha_composite(
                            merged_image, image4)
                        merged_image = Image.alpha_composite(
                            merged_image, image5)
                        merged_image = Image.alpha_composite(
                            merged_image, image6)
                        merged_image.save("make-pic/maked/%s.png" % str(count))
                        # merged_image.save("%s.png" % str(count))
                        count += 1

print(a_pic, b_pic, c_pic, d_pic, e_pic, main_pic)
