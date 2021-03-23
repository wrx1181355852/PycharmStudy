# coding:utf-8
# @时间 : 2021/3/22 13:15
# @文件名 : 数字炸弹.py
# @工程名:PycharmStudy
# @用户：Administrator
# @IDE名字:PyCharm

import random
import time
import sys
import PySimpleGUI as sg
from playsound import *
from threading import Thread


def play_sound():
    playsound('boom.mp3')


class Boom:
    def __init__(self):
        self.minding, self.maxding = self.get_num()
        self.minNum = self.minding  # 初次选择范围，之后固定
        self.maxNum = self.maxding
        self.num = random.randint(self.minNum, self.maxNum)  # 数值范围

        self.guess = 0
        self.gif = '爆炸.gif'  # 爆炸动图地址，可以替换
        self.layout = [  # 定义界面
            [sg.T('   请输入数字:      ', key='-TEXT1-',
                  # size=(20,1),
                  font=('楷体', 20)
                  )],
            [sg.T(f'  {self.minNum}-{self.maxNum}   ', key='-TEXT2-', font=('楷体', 20))],
            [sg.In(size=(30, 1), do_not_clear=False, key='-IN-')],
            [sg.B('确认', bind_return_key=True), sg.B('退出'), sg.B('刷新')],
        ]
        self.window = sg.Window('数字炸弹', self.layout, keep_on_top=True,
                                element_justification='c',
                                size=(250, 150))  # 设置窗口，置顶，居中显示，大小 250*150 标题为‘数字炸弹’
        self.i = 0
        self.mian()

    def get_num(self):
        while True:
            try:
                self.minNum = int(sg.popup_get_text(message='最小值:', keep_on_top=True, size=(17, 2)))
            except TypeError:
                sys.exit()
            except ValueError:
                sg.popup('请输最小值。')
            else:
                while True:
                    try:
                        self.maxNum = int(sg.popup_get_text(message='最大值:', keep_on_top=True, size=(17, 2)))
                    except TypeError:
                        sys.exit()
                    except ValueError:
                        sg.popup('请输最大值。')
                    else:
                        break
                break
        return self.minNum, self.maxNum

    def mian(self):

        while True:
            self.event, self.values = self.window.read()

            # print(self.event, self.values)

            if self.event in ('退出', None):
                break

            if self.event == '确认':
                try:
                    self.guess = int(self.values['-IN-'])  # 转为整数赋值用于比较
                except ValueError:
                    self.window['-TEXT1-'].update('请输入正确范围：')
                    self.window['-TEXT2-'].update(f'  {self.minNum}-{self.maxNum}   ')
                else:
                    # print(type(self.guess), type(self.minNum), type(self.maxNum), type(self.num))
                    if self.num > self.guess > self.minNum:  # 猜小了，更新低点
                        self.minNum = self.guess
                        self.window['-TEXT1-'].update('猜错了！再来。')
                        self.window['-TEXT2-'].update(f'{self.minNum}到{self.maxNum}')
                    elif self.num < self.guess < self.maxNum:  # 猜大了，更新顶点
                        self.maxNum = self.guess
                        self.window['-TEXT1-'].update('猜错了！再来。')
                        self.window['-TEXT2-'].update(f'{self.minNum}到{self.maxNum}')
                    elif self.guess == self.num:  # 猜对了
                        self.window['-TEXT1-'].update('猜对啦！就是：')
                        self.window['-TEXT2-'].update(self.num)
                        Thread(target=play_sound, daemon=True).start()
                        Thread(target=self.gif_show(), daemon=True).start()
                        # while True:    #显示炸弹GIF
                        # time.sleep(0.01)
                        # self.i+=1
                        # state = sg.PopupAnimated(image_source=self.gif, time_between_frames=140)
                        #
                        # if not state or self.i==300:
                        #     sg.PopupAnimated(image_source=None, )
                        #     break
                    else:
                        self.window['-TEXT1-'].update('请输入正确范围：')
                        self.window['-TEXT2-'].update(f'{self.minNum}到{self.maxNum}')
            if self.event == '刷新':  # 刷新程序重新开始
                # self.get_num()   #每次刷新选择范围

                self.minNum = self.minding  # 初次选择范围，之后固定
                self.maxNum = self.maxding

                self.num = random.randint(self.minNum, self.maxNum)
                self.window['-TEXT1-'].update('请输数字：')
                self.window['-TEXT2-'].update(f'  {self.minNum}-{self.maxNum}   ')
        self.window.close()
        sys.exit()

    def gif_show(self):
        while True:  # 显示炸弹GIF
            time.sleep(0.01)
            self.i += 1
            state = sg.PopupAnimated(image_source=self.gif, time_between_frames=140)

            if not state or self.i == 310:
                sg.PopupAnimated(image_source=None, )
                break


if __name__ == '__main__':
    boom = Boom()
