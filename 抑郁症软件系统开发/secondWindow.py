from tkinter import *

######from matplotlib.widgets import * #导入装置，包括按钮等,会与tkinter包中的按钮冲突
import firstWindow
import drawEEG


class SecondWindow:
    def __init__(self,master):
        self.master = master
        self.master.config(bg='DarkBlue')
        self.bottomFrame = Frame(self.master,bg='DarkBlue')
        self.bottomFrame.pack(side=BOTTOM,ipadx=1000)
        self.topFrame = Frame(self.master,bg='DarkBlue')
        self.topFrame.pack(side=TOP)
        self.button5 = PhotoImage(file='button5.png')
        self.button6 = PhotoImage(file='button6.png')
        self.button7 = PhotoImage(file='button7.png')
        self.button8 = PhotoImage(file='button8.png')
        self.button9 = PhotoImage(file='button9.png')
        self.button10 = PhotoImage(file='button10.png')
        self.picture2 = PhotoImage(file='picture3.png')
##        ####第二界面文字
        titleLabel = Label(self.topFrame,text='脑电频谱图（压力应对，心理调整，职业倦怠）',
                           fg='yellow',
                           bg='DarkBlue',
                           font=('Arial',20),
                           width=50,height=1)
        titleLabel.pack()  ###这里side可以赋值为LEFT RIGHT TOP BOTTOM
        self.bottomWidgetPadx = 2
        
        ###带图按钮5
        quitButton = Button(self.bottomFrame,image=self.button5,command=self.backToFirstWindow)
        quitButton.pack(side=LEFT, padx=self.bottomWidgetPadx)

        ###在Label中插入图片
        ###带图按钮6
        catalogButton = Button(self.bottomFrame,image=self.button6,command=self.backToFirstWindow)
        catalogButton.pack(side=LEFT, padx=self.bottomWidgetPadx)

        ###带图按钮7
        stopButton = Button(self.bottomFrame, image=self.button7, command=self.backToFirstWindow)
        stopButton.pack(side=LEFT, padx=self.bottomWidgetPadx)

        ###带图按钮8
        playbackButton = Button(self.bottomFrame,image=self.button8,command=self.backToFirstWindow)
        playbackButton.pack(side=LEFT, padx=self.bottomWidgetPadx)

        ###带图按钮9
        BeginStopDrawButton = Button(self.bottomFrame,image=self.button9,command=self.backToFirstWindow)
        BeginStopDrawButton.pack(side=LEFT, padx=self.bottomWidgetPadx)

        ###带图按钮10
        recordButton = Button(self.bottomFrame,image=self.button10,command=self.backToFirstWindow)
        recordButton.pack(side=LEFT, padx=self.bottomWidgetPadx)

        self.centerFrame = drawEEG.Draw(self.master)

    def backToFirstWindow(self):
        self.bottomFrame.destroy()
        self.topFrame.destroy()
        self.centerFrame.destroy()
        firstWindow.FirstWindow(self.master)


