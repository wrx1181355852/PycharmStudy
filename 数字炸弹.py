# coding:utf-8
# @时间 : 2021/3/22 13:15
# @文件名 : 数字炸弹.py
# @工程名:PycharmStudy
# @用户：Administrator
# @IDE名字:PyCharm
import sys
import PySimpleGUI as sg

class Boom():
    def __init__(self):
        self.layout=[
            [sg.T('请输入数字：1-100')],
            [sg.T(''*20)],
            [sg.In()],
            [sg.B('确认'),sg.B('取消'),sg.B('刷新')],
        ]
        pass

    def mian(self):
        pass


if __name__ == '__main__':
    boom =Boom()
