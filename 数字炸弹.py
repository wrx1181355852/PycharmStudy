# coding:utf-8
# @时间 : 2021/3/22 13:15
# @文件名 : 数字炸弹.py
# @工程名:PycharmStudy
# @用户：Administrator
# @IDE名字:PyCharm

import random
import PySimpleGUI as sg


class Boom:
    def __init__(self):
        self.num = random.randint(1, 101)
        self.minnum = 0
        self.maxnum = 100
        self.layout = [
            [sg.T('请输入数字：', key='-TEXT1-')],
            [sg.T('    1-100   ', key='-TEXT2-')],
            [sg.In(size=(30, 1), do_not_clear=False, key='-IN-')],
            [sg.B('确认'), sg.B('退出'), sg.B('刷新')],
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
                    self.num1 = int(self.values['-IN-'])
                    print(type(self.num1),type(self.maxnum),type(self.num))
                except (AttributeError, ValueError):
                    self.window['-TEXT1-'].update('请输入正确范围。')
                    self.window['-TEXT2-'].update('1-100')

                else:
                    if self.num1 == self.num:
                        self.window['-TEXT1-'].update('答对了！是：')
                        self.window['-TEXT2-'].update(self.num)
                    elif self.minnum < self.num1 < self.num:
                        self.minnum = self.values['-IN-']
                        self.window['-TEXT1-'].update('猜错了！再来。')
                        self.window['-TEXT2-'].update(f'{self.minnum}到{self.maxnum}')
                    elif self.maxnum > self.num1 > self.num:
                        self.maxnum = self.num1
                        self.window['-TEXT1-'].update('猜错了！再来。')
                        self.window['-TEXT2-'].update(f'{self.minnum}到{self.maxnum}')
        self.window.close()


if __name__ == '__main__':
    boom = Boom()
