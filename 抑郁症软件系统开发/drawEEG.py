import random  # 产生随机数
from tkinter import *

######from matplotlib.widgets import * #导入装置，包括按钮等,会与tkinter包中的按钮冲突
import mat4py  # 读取.mat格式文件所需的包
import matplotlib.pyplot as plt
import numpy as np  # 数值计算扩展包
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d.art3d import Poly3DCollection  # 3D画图填充
from scipy import signal  # 滤波


class Draw:
    def __init__(self, master):
        self.master = master
        #######设置三维图的x轴为时间轴
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 9
        return self.draw_picture()

    ####### 三维图时间轴的分秒四位数
    def time_test(self):
        self.d = self.d + 1
        if self.d == 10:
            self.d = 0
            self.c = self.c + 1
        if self.c == 6:
            self.c = 0
            self.b = self.b + 1
        if self.b == 10:
            self.b = 0
            self.a = self.a + 1

    def draw_picture(self):
        #######导入mat格式数据，并计算长度
        hospital_data = mat4py.loadmat('chenminggang_1.mat')
        Bio_data = hospital_data['Biotrace']
        Bio_datalen = len(Bio_data)

        #######时频转换的采样频率和取样长度
        sampling_rate = 256  # 采样频率
        fft_size = 512  # FFT处理的取样长度
        pinyu_data = Bio_data
        b, a = signal.butter(6, [1 / 128, 40 / 128], 'bandpass')
        filtedData = signal.filtfilt(b, a, Bio_data)

        #######处理数据，三维图每行64个数据点
        dimen3_datanum = 64
        #######处理数据，三维图时频转化时的使用的数据点数512个
        dimen3_timenum = 256
        #######判断要画多少组数据
        if Bio_datalen % dimen3_timenum == 0:
            curve_num = int(Bio_datalen / dimen3_timenum)
        else:
            curve_num = int(Bio_datalen / dimen3_timenum) + 1

        #######处理数据，二维图每次刷新64个数据点
        dimen2_datanum = 64

        #######定义x,y,z坐标,并初始化
        x = [i for i in range(dimen3_datanum)]

        y = [i for i in range(dimen3_datanum)]

        z = [i for i in range(dimen3_datanum)]

        bx_x = [i for i in range(dimen2_datanum)]

        bx_y = [i for i in range(dimen2_datanum)]

        #######定义空字典，用于存放绘制的三维曲线
        curve_remove = {}
        bx_remove = {}
        fill_remove = {}

        #######定义空数组，用于存放迭代数据
        vect = []
        freqs = []
        h = 0.0
        ########生成画板
        centerFrame = Frame(self.master, bg='DarkBlue')
        centerFrame.pack(side=LEFT)
        fig = plt.figure('上海大学443实验室', dpi=100, figsize=(10, 4), facecolor='DarkBlue')  # 调整界面尺寸,dpi为分辨率
        ########创建画布
        canvas = FigureCanvasTkAgg(fig, master=centerFrame)
        #######把matplotlib绘制图形的导航工具栏显示到tkinter窗口上
        ##        toolbar =NavigationToolbar2Tk(canvas, root)
        ##        toolbar.update()
        ##        canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

        ########创建三维图
        ax = fig.add_subplot(212, position=[-0.2, 0, 1.4, 0.6], \
                             projection='3d', facecolor='DarkBlue')  # 设置图形为3d显示
        ax.w_xaxis.set_pane_color((0.3, 0.3, 0.6))  # 设置坐标系背景颜色
        ax.w_yaxis.set_pane_color((0.3, 0.3, 0.6))
        ax.w_zaxis.set_pane_color((0.3, 0.3, 0.6))
        ########创建二维图
        bx = fig.add_subplot(211, position=[0.1, 0.6, 0.8, 0.3], facecolor='DarkBlue')

        x_lim = 20  # 改变三维图每次刷新的图形个数
        y_lim = 40
        z_lim = 30
        ax.set_xlim(0, x_lim)  # 设置三维图x坐标的范围
        ax.set_ylim(0, y_lim)
        bx.set_ylim(-200, 200)  # 设置二维图y坐标的范围

        ax.set_xticklabels(('00:00', '00:01', '00:02', '00:03', '00:04', \
                            '00:05', '00:06', '00:07', '00:08'))

        bx.set_xticklabels(('00:00', '00:01', '00:02', '00:03', '00:04', \
                            '00:05', '00:06', '00:07', '00:08', '00:09'))

        ax.view_init(elev=18, azim=1)  # 改变视角位置

        #######xf = np.fft.rfft(Bio_data)/512
        #######rfft函数的返回值是N/2+1个复数，分别表示从0(Hz)到sampling_rate/2(Hz)的分。
        #######最后我们计算每个频率分量的幅值，并通过 20*np.log10()
        #######将其转换为以db单位的值。为了防止0幅值的成分造成log10无法计算，
        #######我们调用np.clip对xf的幅值进行上下限处理

        for num in range(curve_num):

            canvas.draw()
            canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

            ########产生三维频谱图x轴数据

            x = [num for i in range(dimen3_datanum)]

            ########对原始数据进行傅里叶变换，产生y、z轴数据
            xs = filtedData[num * dimen3_timenum:(num + 1) * dimen3_timenum]
            num_i = dimen3_timenum
            if num == (curve_num - 1):
                num_i = Bio_datalen - (curve_num - 1) * dimen3_timenum
            for i in range(num_i):
                if xs[i] == 0:
                    delta = 1e-7
                    xs[i] = xs[i] + delta

            xf = np.fft.rfft(xs) / fft_size

            freqs = np.linspace(0, sampling_rate / 1.582, fft_size / 2 + 1)

            ######## xfp = 20*np.log10(np.clip(np.abs(xf), 1e-20, 1e100))

            xfp = np.abs(xf)

            ########产生三维频谱图的y,z轴数据
            for k in range(dimen3_datanum):

                y[k] = freqs[k]
                z[k] = xfp[k]
                ########对负值数据进行取反，避免曲线颜色填充问题
                if z[k] < 0:
                    z[k] = -z[k]

            if num % 2 == 0:
                num_2 = num / 2

            ########产生二维时域x,y数据
            for i in range(dimen2_datanum):
                bx_x[i] = num * dimen2_datanum + i

                bx_y[i] = filtedData[num * dimen2_datanum + i]

            ##########迭代填充
            for m in range(len(x) - 1):
                x1 = [x[m], x[m + 1], x[m + 1], x[m]]
                y1 = [y[m], y[m + 1], y[m + 1], y[m]]
                z1 = [z[m], z[m + 1], h, h]
                vect.append(list(zip(x1, y1, z1)))

            ##########显示三维图形

            curve_remove[num], = ax.plot(x, y, z, 'black')

            bx.plot(bx_x, bx_y)

            ##########bx_remove[num], = bx.plot(bx_x,bx_y)

            poly3dCollection = Poly3DCollection(vect, facecolor=
            (random.random(),
             random.random(),
             random.random(),
             1), alpha=1)

            ax.add_collection3d(poly3dCollection)

            fill_remove[num], = [poly3dCollection]

            for fill_delnum in range(dimen3_datanum - 1):
                del vect[0]

            ########每画十个curve，改变x的坐标范围，删除之前绘制的曲线
            if num % x_lim == 0 and num != 0:
                time_0 = str(self.a) + str(self.b) + ':' + str(self.c) + str(self.d)
                self.time_test()

                time_1 = str(self.a) + str(self.b) + ':' + str(self.c) + str(self.d)
                self.time_test()

                time_2 = str(self.a) + str(self.b) + ':' + str(self.c) + str(self.d)
                self.time_test()

                time_3 = str(self.a) + str(self.b) + ':' + str(self.c) + str(self.d)
                self.time_test()

                time_4 = str(self.a) + str(self.b) + ':' + str(self.c) + str(self.d)
                self.time_test()

                time_5 = str(self.a) + str(self.b) + ':' + str(self.c) + str(self.d)
                self.time_test()

                time_6 = str(self.a) + str(self.b) + ':' + str(self.c) + str(self.d)
                self.time_test()

                time_7 = str(self.a) + str(self.b) + ':' + str(self.c) + str(self.d)
                self.time_test()

                time_8 = str(self.a) + str(self.b) + ':' + str(self.c) + str(self.d)
                self.time_test()

                ax.set_xticklabels((time_0, time_1, time_2, time_3, time_4, time_5, \
                                    time_6, time_7, time_8))
                bx.set_xticklabels((time_0, time_1, time_2, time_3, time_4, time_5, \
                                    time_6, time_7, time_8))

                ax.set_xlim(num, num + x_lim)

                for curve_delnum in range(num - x_lim, num):
                    curve_remove[curve_delnum].remove()

                    fill_remove[curve_delnum].remove()

        return centerFrame
