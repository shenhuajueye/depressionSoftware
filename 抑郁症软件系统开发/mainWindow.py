##from tkinter import *
import tkinter as tk  # 使用Tkinter前需要先导入
from tkinter import *

import matplotlib.pyplot as plt
from secondWindow import SecondWindow
######from matplotlib.widgets import * #导入装置，包括按钮等,会与tkinter包中的按钮冲突
plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文显示
plt.rcParams['axes.unicode_minus'] = False  # 负号显示


class BaseWindow:
    def __init__(self, master):
        self.root = master
        self.root.config()
        self.root.title('上海大学脑机接口实验室')
        ###获取电脑屏幕尺寸1920*1080
        ##        w = self.root.winfo_screenwidth()
        ##        h = self.root.winfo_screenheight()
        ##        self.root.geometry("%dx%d" % (w, h))
        ####
        # self.root.geometry('1000x600')
        ###设置窗口最大化显示
        self.root.state("zoomed")
        ###最大化窗口，不过将桌面下方应用的任务栏也覆盖了
        ##        self.root.attributes("-fullscreen", True)

        FirstWindow(self.root)


class FirstWindow:
    def __init__(self, master):
        self.master = master
        self.master.config(bg='DarkBlue')
        ###基准界面initface
        self.topFrame = Frame(self.master, bg='DarkBlue')
        self.topFrame.pack(side=TOP)
        self.bottomFrame = Frame(self.master, bg='DarkBlue')
        self.bottomFrame.pack(side=BOTTOM, ipadx=1000)
        self.middleLeftFrame = Frame(self.master, bg='DarkBlue')
        self.middleLeftFrame.pack(side=LEFT, padx=5)
        self.middleFrame = Frame(self.master, bg='DarkBlue')
        self.middleFrame.pack(side=LEFT)
        self.middleRightFrame = Frame(self.master, bg='DarkBlue')
        self.middleRightFrame.pack(side=LEFT, padx=5)
        self.titleLabelFont = 60
        self.middleWidgetPadx = 20
        self.middleWidgetPady = 30
        self.bottomWidgetPadx = 2
        self.pictureWidth = 500
        self.pictureHeight = 600

        ###创建一个菜单栏，这里我们可以把它理解成一个容器，在窗口的上方
        menubar = Menu(self.master)
        ###创建第一个菜单单元
        firstmenu = Menu(menubar, tearoff=0)  # tearoff意为下拉
        ###将上面定义的空菜单名为'File’，放在菜单栏中，就是装入上面的容器中
        menubar.add_cascade(label='文件', menu=firstmenu)
        ###在‘文件’中加入‘新建’的小菜单，每个小菜单对应命令操作
        ###如果点击这些单元，就会触发相应命令
        firstmenu.add_command(label='新建', command=self.dataPlayback)
        firstmenu.add_command(label='打开', command=self.dataPlayback)
        firstmenu.add_command(label='保存', command=self.dataPlayback)
        ###分割线
        firstmenu.add_separator()
        firstmenu.add_command(label='退出', command=self.dataPlayback)
        ###在第一个菜单单元下创建二级菜单
        submenu = Menu(firstmenu)
        firstmenu.add_cascade(label='导出', menu=submenu, underline=1)
        submenu.add_command(label='导出数据', command=self.dataPlayback)

        ###创建第二个菜单单元
        secondmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='屏幕', menu=secondmenu)
        secondmenu.add_command(label='新建', command=self.dataPlayback)
        secondmenu.add_command(label='打开', command=self.dataPlayback)
        secondmenu.add_command(label='保存', command=self.dataPlayback)

        ###创建第三个菜单单元
        threemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='配置', menu=threemenu)
        threemenu.add_command(label='新建', command=self.dataPlayback)
        threemenu.add_command(label='打开', command=self.dataPlayback)
        threemenu.add_command(label='保存', command=self.dataPlayback)

        ###创建第四个菜单单元
        fourmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='帮助', menu=fourmenu)
        fourmenu.add_command(label='新建', command=self.dataPlayback)
        fourmenu.add_command(label='打开', command=self.dataPlayback)
        fourmenu.add_command(label='保存', command=self.dataPlayback)

        self.master.config(menu=menubar)  ###显示菜单栏

        titleLabel = Label(self.topFrame, text='上海大学443实验室神经心理反馈系统',
                           fg='yellow',
                           bg='DarkBlue',
                           font=('Arial', self.titleLabelFont),
                           width=30, height=1)
        titleLabel.pack()  ###这里side可以赋值为LEFT RIGHT TOP BOTTOM

        ###在middleLeftFrame的Label中插入图片
        middleLeftPhoto = Label(self.middleLeftFrame, height=self.pictureHeight, width=self.pictureWidth,
                                image=picture1,
                                justify=LEFT,
                                compound=CENTER,
                                font=('华文行楷', 20),
                                fg='white')  ### 前景色
        middleLeftPhoto.pack(side=LEFT)

        ###带图按钮1
        beginRunButton = Button(self.middleFrame, image=button1, command=self.changeToSecondWindow)
        beginRunButton.pack(padx=self.middleWidgetPadx, pady=self.middleWidgetPady)

        ###带图按钮2
        dataPlaybackButton = Button(self.middleFrame, image=button2, command=self.showInformation)
        dataPlaybackButton.pack(padx=self.middleWidgetPadx, pady=self.middleWidgetPady)

        ###带图按钮3
        recordNewDataButton = Button(self.middleFrame, image=button3, command=self.dataPlayback)
        recordNewDataButton.pack(padx=self.middleWidgetPadx, pady=self.middleWidgetPady)

        ###带图按钮4
        quitSystemButton = Button(self.middleFrame, image=button3, command=self.dataPlayback)
        quitSystemButton.pack(padx=self.middleWidgetPadx, pady=self.middleWidgetPady)

        ###带图按钮5
        quitButton = Button(self.bottomFrame, image=button5, command=self.dataPlayback)
        quitButton.pack(side=LEFT, padx=self.bottomWidgetPadx)

        ###带图按钮6
        catalogButton = Button(self.bottomFrame, image=button6, command=self.dataPlayback)
        catalogButton.pack(side=LEFT, padx=self.bottomWidgetPadx)

        ###带图按钮7
        stopButton = Button(self.bottomFrame, image=button7, command=self.dataPlayback)
        stopButton.pack(side=LEFT, padx=self.bottomWidgetPadx)

        ###带图按钮8
        playbackButton = Button(self.bottomFrame, image=button8, command=self.dataPlayback)
        playbackButton.pack(side=LEFT, padx=self.bottomWidgetPadx)

        ###带图按钮9
        BeginStopDrawButton = Button(self.bottomFrame, image=button9, command=self.dataPlayback)
        BeginStopDrawButton.pack(side=LEFT, padx=self.bottomWidgetPadx)

        ###带图按钮10
        recordButton = Button(self.bottomFrame, image=button10, command=self.dataPlayback)
        recordButton.pack(side=LEFT, padx=2)

        ###在middleRightFrame的Label中插入图片
        middleRightPhoto = Label(self.middleRightFrame, height=self.pictureHeight, width=self.pictureWidth,
                                 image=picture2,
                                 justify=LEFT,
                                 compound=CENTER,
                                 font=('华文行楷', 20),
                                 fg='white')  ###前景色
        middleRightPhoto.pack(side=RIGHT)

    def changeToSecondWindow(self, ):
        self.middleRightFrame.destroy()
        self.middleLeftFrame.destroy()
        self.middleFrame.destroy()
        self.bottomFrame.destroy()
        self.topFrame.destroy()
        self.bottomFrame.destroy()
        SecondWindow(self.root)


    def showInformation(self):
        tk.messagebox.showinfo(title='hello', message='你好！')

    def dataPlayback(self):
        print('画图')


if __name__ == '__main__':
    root = Tk()

    ###tkinter加载图片不能放在def里，不然就不显示，真坑
    button1 = PhotoImage(file='button1.png')
    button2 = PhotoImage(file='button2.png')
    button3 = PhotoImage(file='button3.png')
    button4 = PhotoImage(file='button4.png')
    button5 = PhotoImage(file='button5.png')
    button6 = PhotoImage(file='button6.png')
    button7 = PhotoImage(file='button7.png')
    button8 = PhotoImage(file='button8.png')
    button9 = PhotoImage(file='button9.png')
    button10 = PhotoImage(file='button10.png')
    picture1 = PhotoImage(file='picture1.png')
    picture2 = PhotoImage(file='picture2.png')

    BaseWindow(root)
    ###显示界面
    root.mainloop()
