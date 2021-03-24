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


def play_sound(file):
    playsound(file)




class Boom:
    def __init__(self):
        self.state_menu = 0

        self.minding, self.maxding = self.get_num()
        while True:
            if self.maxNum - self.minNum < 2:
                self.minding, self.maxding = self.get_num()
            else:
                break
        self.minNum = self.minding  # 初次选择范围，之后固定
        self.maxNum = self.maxding
        self.num = random.randint(self.minNum + 1, self.maxNum - 1)  # 数值范围

        self.guess = 0
        self.gif = '爆炸.gif'  # 爆炸动图地址，可以替换
        self.menumsg = [
            ['模式', ['开局设置范围', '每局设置范围']]
        ]
        self.layout = [  # 定义界面
            [sg.Menu(self.menumsg, key='-MENU-')],
            [sg.T('   请输入数字:      ', key='-TEXT1-',
                  # size=(20,1),
                  font=('楷体', 20)
                  )],
            [sg.T(f' {self.minNum}-{self.maxNum}不包含{self.minNum}和{self.maxNum}.  ', key='-TEXT2-', font=('楷体', 20))],
            [sg.In(size=(35, 1), focus=True, do_not_clear=False, key='-IN-')],
            [sg.B('确认', bind_return_key=True), sg.B('退出'), sg.B('刷新')],
        ]
        self.window = sg.Window('数字炸弹', self.layout, keep_on_top=True,
                                element_justification='c',
                                grab_anywhere=True,
                                size=(300, 150))  # 设置窗口，置顶，居中显示，大小 250*150 标题为‘数字炸弹’
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
            event, values = self.window.read()

            if event in ('退出', None):
                break

            if event == '开局设置范围':
                self.state_menu = 0

            if event == '每局设置范围':
                self.state_menu = 1

            if event == '确认':
                try:
                    self.guess = int(values['-IN-'])  # 转为整数赋值用于比较
                except ValueError:
                    self.window['-TEXT1-'].update('请输入正确范围：')
                    self.window['-TEXT2-'].update(f'{self.minNum}-{self.maxNum}不包含{self.minNum}和{self.maxNum}.')
                    Thread(target=play_sound, args=('Pleseenterright.mp3',),daemon=True).start()
                else:

                    if self.num > self.guess > self.minNum:  # 猜小了，更新低点
                        self.minNum = self.guess
                        self.window['-TEXT1-'].update(f'{self.guess}太小了！')
                        self.window['-TEXT2-'].update(f'{self.minNum}-{self.maxNum}不包含{self.minNum}和{self.maxNum}.')
                        Thread(target=play_sound, args=('min.mp3',), daemon=True).start()
                    elif self.num < self.guess < self.maxNum:  # 猜大了，更新顶点
                        self.maxNum = self.guess
                        self.window['-TEXT1-'].update(f'{self.guess}太大了！')
                        self.window['-TEXT2-'].update(f'{self.minNum}-{self.maxNum}不包含{self.minNum}和{self.maxNum}.')
                        Thread(target=play_sound, args=('max.mp3',), daemon=True).start()
                    elif self.guess == self.num:  # 猜对了
                        self.window['-TEXT1-'].update('猜对啦！就是：')
                        self.window['-TEXT2-'].update(self.num)

                        Thread(target=play_sound,args=('boom.mp3',), daemon=True).start()
                        Thread(target=self.gif_show(), daemon=True).start()
                        self.flush()

                    else:
                        self.window['-TEXT1-'].update('请输入正确范围：')
                        self.window['-TEXT2-'].update(f'{self.minNum}-{self.maxNum}不包含{self.minNum}和{self.maxNum}.')
                        Thread(target=play_sound, args=('Pleseenterright.mp3',), daemon=True).start()
            if event == '刷新':  # 刷新程序重新开始
                self.flush()

        self.window.close()
        sys.exit()

    def flush(self):
        self.i = 0
        if self.state_menu == 0:
            self.start_set()
        if self.state_menu == 1:
            self.every_set()

    def gif_show(self):
        while True:  # 显示炸弹GIF
            time.sleep(0.01)
            self.i += 1
            state = sg.PopupAnimated(image_source=self.gif, time_between_frames=140)

            if not state or self.i == 310:
                sg.PopupAnimated(image_source=None, )
                break

    def start_set(self):
        self.minNum = self.minding  # 初次选择范围，之后固定
        self.maxNum = self.maxding

        self.num = random.randint(self.minNum + 1, self.maxNum - 1)
        self.window['-TEXT1-'].update('请输数字：')
        self.window['-TEXT2-'].update(f'{self.minNum}-{self.maxNum}不包含{self.minNum}和{self.maxNum}.')

    def every_set(self):
        self.get_num()  # 每次刷新选择范围
        self.num = random.randint(self.minNum + 1, self.maxNum - 1)
        self.window['-TEXT1-'].update('请输数字：')
        self.window['-TEXT2-'].update(f'{self.minNum}-{self.maxNum}不包含{self.minNum}和{self.maxNum}.')


if __name__ == '__main__':
    boom = Boom()
