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


class Boom:
    def __init__(self):
        self.num = random.randint(0, 101)
        self.minNum = 0
        self.maxNum = 100
        self.guess = 0
        self.gif = '爆炸.gif'
        self.layout = [
            [sg.T('      请输入数字：    ', key='-TEXT1-')],
            [sg.T('    1-100   ', key='-TEXT2-')],
            [sg.In(size=(30, 1), do_not_clear=False, key='-IN-')],
            [sg.B('确认', bind_return_key=True), sg.B('退出'), sg.B('刷新')],
        ]
        self.window = sg.Window('数字炸弹', self.layout, keep_on_top=True,
                                element_justification='c',
                                size=(200, 120))

        self.mian()

    def mian(self):
        while True:
            self.event, self.values = self.window.read()

            print(self.event, self.values)

            if self.event in ('退出', None):
                break

            if self.event == '确认':
                try:
                    self.guess = int(self.values['-IN-'])
                except ValueError:
                    self.window['-TEXT1-'].update('请输入正确范围：')
                    self.window['-TEXT2-'].update('1-100')
                else:
                    print(type(self.guess), type(self.minNum), type(self.maxNum), type(self.num))
                    if self.num > self.guess > self.minNum:
                        self.minNum = self.guess
                        self.window['-TEXT1-'].update('猜错了！再来。')
                        self.window['-TEXT2-'].update(f'{self.minNum}到{self.maxNum}')
                    elif self.num < self.guess < self.maxNum:
                        self.maxNum = self.guess
                        self.window['-TEXT1-'].update('猜错了！再来。')
                        self.window['-TEXT2-'].update(f'{self.minNum}到{self.maxNum}')
                    elif self.guess == self.num:
                        self.window['-TEXT1-'].update('猜对啦！就是：')
                        self.window['-TEXT2-'].update(self.num)
                        while True:
                            time.sleep(0.01)
                            state = sg.PopupAnimated(image_source=self.gif, time_between_frames=140, no_titlebar=False)
                            if not state:
                                break
                    else:
                        self.window['-TEXT1-'].update('请输入正确范围：')
                        self.window['-TEXT2-'].update(f'{self.minNum}到{self.maxNum}')
            if self.event == '刷新':
                self.num = random.randint(0, 101)
                self.minNum = 0
                self.maxNum = 100
                self.window['-TEXT1-'].update('请输数字：')
                self.window['-TEXT2-'].update('1-100')
        self.window.close()
        sys.exit()


if __name__ == '__main__':
    boom = Boom()
