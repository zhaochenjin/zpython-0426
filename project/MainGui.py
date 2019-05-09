import re
from tkinter import Tk, Entry, Button, scrolledtext, filedialog, ttk, S, E, W, N, Frame, Label, Text, TOP, BOTH, \
    messagebox
# from PIL import Image, ImageTk
from urllib.request import urlopen

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from wordcloud import WordCloud
import jieba
from scipy.misc import imread
from os import path
from PIL import Image
from urllib import *

class BigWork(Frame):

    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.master = master
        self.initUI()

        self.file_path = ''
        self.url_or_txt = ''
        self.yunciIm = ''
        self.yinxie = ''
        self.initUI()

    def initUI(self):

        self.master.title('答辩')

        self.mainFrame = ttk.Frame(self.master, padding='3 3 12 12')
        self.mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))

        self.urlTxt = Text(self.mainFrame, width=90, height=5)
        self.urlTxt.grid(row=1, column=1, sticky=W)

        self.getfileBtn = Button(self.mainFrame, text='Open file', width=30, height=5, command=self.readImage)
        self.getfileBtn.grid(row=1, column=2)

        #
        # def remain():
        #     self.messagebox.showinfo('你的url找不到东西，我就当成文本处理哦')

        # labelImage = Label(window, width=125, height=55, bg='white', image= self.yunci())
        self.labelImage = Label(self.master, width=125, height=30, bg='white')
        self.labelImage.grid(row=2)

        self.ciyunBtn = Button(self.master, text='用文本去的文本或url里的内容云词', width=60, height=5, command=self.draw_wordcloud)
        self.ciyunBtn.grid(row=3, sticky=W)
        self.yinxieBtn = Button(self.master, text='用文本区的东西隐写入找到的图片', width=60, heigh=5, command=self.yinxieMethod)
        self.yinxieBtn.grid(row=3, sticky=E)

        self.yinxie_info_label = Label(self.master, width=125, height= 3, bg='white', fg='red')
        self.yinxie_info_label.grid(row=4, sticky=S)

    #
    # def remain(self):
    #     self.messagebox.showinfo('你的url找不到东西，我就当成文本处理哦')

    def readImage(self):
        self.getImagePath()
        self.loadImage(self.file_path)


    def getImagePath(self):
        self.file_path = filedialog.askopenfilename(filetypes=(("image files", "*.png;*.jpg;")
                                                         , ("All files", "*.*")))
        # self.loadImage(filename)



    canvas = ''

    def loadImage(self, filename):

        # filename = filedialog.askopenfilename(filetypes=(("image files", "*.png;*.jpg")
        #                                                  , ("All files", "*.*")))

        # filename=self.getfilepath()
        print(filename)

        self.image = misc.imread(filename)
        print(type(misc.imread(filename)))
        fig = plt.figure(figsize=(5, 5))
        if self.canvas == '':
            self.im = plt.imshow(self.image)  # later use a.set_data(new_data)
            axs = plt.gca()
            axs.set_xticklabels([])
            axs.set_yticklabels([])

            # a tk.DrawingArea
            self.canvas = FigureCanvasTkAgg(fig, master=self.labelImage)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        else:
            self.im.set_data(self.image)
            self.canvas.draw()


    def checkTxt(self):
        self.url_or_txt = self.urlTxt.get("1.0", 'end-1c')
        print(self.url_or_txt)
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        if self.url_or_txt.startswith('http'):
            if re.match(regex, self.url_or_txt):
                txtHtml = urlopen(self.url_or_txt).read()
                print(txtHtml)
                return txtHtml
            else:
                print('你的url找不到东西，我就当成文本处理哦')
                return self.url_or_txt
        else:
            return self.url_or_txt
        print(self.url_or_txt)



    def draw_wordcloud(self):
        # 读入一个txt文件
        # comment_text = open('F:\program\MyProjects\clustering\\fenci1.0\wordseg_result.txt', 'r').read()
        # 结巴分词，生成字符串，如果不通过分词，无法直接生成正确的中文词云
        print('This is comment_text')
        comment_text = self.checkTxt()
        cut_text = " ".join(jieba.cut(comment_text))
        d = path.dirname(__file__)  # 当前文件文件夹所在目录
        if  self.file_path == '':
            filename = 'image/einstein.jpeg'
        else:
            filename = self.file_path
        color_mask = imread(filename)  # 读取背景图片
        cloud = WordCloud(
            # 设置字体，不指定就会出现乱码
            # font_path="",
            font_path=path.join(d, 'PiKaPiKa/FangZhengPiKaPiKa-2.ttf'),
            # self.getImagePath()
            # 设置背景色
            background_color='white',
            # 词云形状
            mask=color_mask,
            # 允许最大词汇
            max_words=2000,
            # 最大号字体
            max_font_size=30
        )
        word_cloud = cloud.generate(cut_text)  # 产生词云
        word_cloud.to_file("image/pjl_cloud4.jpg")  # 保存图片
        self.loadImage('image/pjl_cloud4.jpg')
        #  显示词云图片
        # plt.imshow(word_cloud)
        # plt.axis('off')
        # plt.show()



    def yinxieMethod(self):
        if self.checkTxt() == '':
            txt_for_yinxie = '你好世界，Hello world!'
            print('txt for yinxie is ' + txt_for_yinxie)
        else:
            txt_for_yinxie = self.checkTxt()
            print('txt for yinxie' + txt_for_yinxie)

        if self.file_path == '':
            filename = 'image/albert.png'
            print('file path is ' + filename)
        else:
            filename = self.file_path
            print('file path is ' + filename)
        self.encodeDataInImage(Image.open(filename), txt_for_yinxie).save('image/encodeImage.png')
        print('success')
        you_saved_info=self.decodeImage(Image.open("image/encodeImage.png"))
        print(you_saved_info)
        self.loadImage('image/encodeImage.png')
        self.yinxie_info_label.config(text=you_saved_info)



    def makeImageEven(seif,image):
        pixels = list(image.getdata())  # 得到一个这样的列表： [(r,g,b,t),(r,g,b,t)...]
        evenPixels = [(r >> 1 << 1, g >> 1 << 1, b >> 1 << 1, t >> 1 << 1) for [r, g, b, t] in pixels]  # 更改所有值为偶数（魔法般的移位）
        evenImage = Image.new(image.mode, image.size)  # 创建一个相同大小的图片副本
        evenImage.putdata(evenPixels)  # 把上面的像素放入到图片副本
        return evenImage



    def constLenBin(self,int):
        binary = "0" * (8 - (len(bin(int)) - 2)) + bin(int).replace('0b',
                                                                    '')  # 去掉 bin() 返回的二进制字符串中的 '0b'，并在左边补足 '0' 直到字符串长度为 8
        return binary



    def encodeDataInImage(self,image, data):
        evenImage = self.makeImageEven(image)  # 获得最低有效位为 0 的图片副本
        binary = ''.join(map(self.constLenBin, bytearray(data, 'utf-8')))  # 将需要被隐藏的字符串转换成二进制字符串
        if len(binary) > len(image.getdata()) * 4:  # 如果不可能编码全部数据， 抛出异常
            raise Exception("Error: Can't encode more than " + len(evenImage.getdata()) * 4 + " bits in this image. ")
        encodedPixels = [(r + int(binary[index * 4 + 0]), g + int(binary[index * 4 + 1]), b + int(binary[index * 4 + 2]),
                          t + int(binary[index * 4 + 3])) if index * 4 < len(binary) else (r, g, b, t) for
                         index, (r, g, b, t) in enumerate(list(evenImage.getdata()))]  # 将 binary 中的二进制字符串信息编码进像素里
        encodedImage = Image.new(evenImage.mode, evenImage.size)  # 创建新图片以存放编码后的像素
        encodedImage.putdata(encodedPixels)  # 添加编码后的数据
        return encodedImage


    def binaryToString(self,binary):
        index = 0
        string = []
        rec = lambda x, i: x[2:8] + (rec(x[8:], i - 1) if i > 1 else '') if x else ''
        # rec = lambda x, i: x and (x[2:8] + (i > 1 and rec(x[8:], i-1) or '')) or ''
        fun = lambda x, i: x[i + 1:8] + rec(x[8:], i - 1)
        while index + 1 < len(binary):
            chartype = binary[index:].index('0')  # 存放字符所占字节数，一个字节的字符会存为 0
            length = chartype * 8 if chartype else 8
            string.append(chr(int(fun(binary[index:index + length], chartype), 2)))
            index += length
        return ''.join(string)



    def decodeImage(self,image):
        pixels = list(image.getdata())  # 获得像素列表
        binary = ''.join([str(int(r >> 1 << 1 != r)) + str(int(g >> 1 << 1 != g)) + str(int(b >> 1 << 1 != b)) + str(
            int(t >> 1 << 1 != t)) for (r, g, b, t) in pixels])  # 提取图片中所有最低有效位中的数据
        # 找到数据截止处的索引
        locationDoubleNull = binary.find('0000000000000000')
        endIndex = locationDoubleNull + (
                    8 - (locationDoubleNull % 8)) if locationDoubleNull % 8 != 0 else locationDoubleNull
        data = self.binaryToString(binary[0:endIndex])
        return data

#
# encodeDataInImage(Image.open("albert.png"), '你好世界，Hello world!').save('encodeImage.png')
# print(decodeImage(Image.open("encodeImage.png")))


def main():
    root = Tk()
    root.geometry('900x800')
    root.resizable(width=False, height=False)
    app = BigWork(root)
    # steganography.py
    root.mainloop()


if __name__ == '__main__':
    main()
