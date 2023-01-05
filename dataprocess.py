import os

class ImageRename():
    def __init__(self):
        self.path = 'F:\有害垃圾_过期药品'

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)

        i = 1
        for item in filelist:
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), 'image_过期药品_' + str(i) + '.jpg')
                print(i,dst)
                os.rename(src, dst)
                print('将 %s 重命名 %s ...' % (src, dst))
                i = i + 1


if __name__ == '__main__':
    newname = ImageRename()
    newname.rename()


# path='F:\/train.txt'
# file = open(path, 'a',encoding='utf-8')
# i=1
# while(i<=328):
#     file.write('垃圾图片库/可回收垃圾_易拉罐/image_易拉罐_%d.jpg'%i+'\t'+str(6)+'\n')
#     i+=1
# file.close()
# print("保存文件成功")
