import os #导入模块


filename = r'/root/siton-tmp/TCM/ocrclip/ctw1500/ctw1500_80/imgs/test' #文件地址
list_path = os.listdir(filename)  #读取文件夹里面的名字

def changename1():
    for index in list_path:  #list_path返回的是一个列表   通过for循环遍历提取元素
        path = filename + '/' + index
        new_path = filename + '/000' + index
        os.rename(path, new_path) #重新命名

changename1()
print('修改完成')