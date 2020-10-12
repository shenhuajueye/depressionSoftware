
import matplotlib.pyplot as plt
######from matplotlib.widgets import * #导入装置，包括按钮等,会与tkinter包中的按钮冲突
import firstWindow

plt.rcParams['font.sans-serif'] = ['SimHei']  #中文显示
plt.rcParams['axes.unicode_minus']=False      #负号显示


class BaseDesk:
    def __init__(self,master):
        self.root = master
        self.root.config()
        self.root.title('上海大学脑机接口实验室')

        ###获取电脑屏幕尺寸1920*1080
##        w = self.root.winfo_screenwidth()
##        h = self.root.winfo_screenheight()
##        self.root.geometry("%dx%d" % (w, h))
        ####
        #self.root.geometry('1400x800')
        ###设置窗口最大化显示
        self.root.state("zoomed")
        ###最大化窗口，不过将桌面下方应用的任务栏也覆盖了
##        self.root.attributes("-fullscreen", True)

        firstWindow.FirstWindow(self.root)

