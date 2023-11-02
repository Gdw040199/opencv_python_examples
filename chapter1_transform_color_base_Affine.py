from PIL import Image


def invert_color(fname):
    im = Image.open(fname)
    px = im.load()
    w, h = im.size #拷贝入图片的大小，遍历图像的每一个像素点
    for i in range(w): #遍历每一个像素点
        for j in range(h): 
            if type(px[i, j]) == int: 
                px[i, j] = 255-px[i, j] #将每一个像素点的颜色反转（255阶色度）
            elif len(px[i, j]) == 3: 
                px[i, j] = tuple([255-i for i in px[i, j]]) 
            elif len(px[i, j]) == 4:
                px[i, j] = tuple([255-i for i in px[i, j][:3]]+[px[i, j][-1]])
            else:
                pass
    im.save(fname.replace('.', '_inverted.'))
    im.show(fname.replace('.', '_inverted.')) #注意和openCV中的cv2.imshow()函数的区别(1)是命名的时候，(2)调用窗口的不同
    return im


if __name__ == '__main__':
    invert_color('test_4.png')
