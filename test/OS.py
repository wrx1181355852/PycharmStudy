
# -*- coding: utf-8 -*-
# @Time    : 2021/1/15 18:02
# @Author  : WRX
# @File    : OS.py
# @Software: PyCharm

from File import *
import PySimpleGUI as sg


layout = [
  [sg.Image(filename='转圈.gif', key='-GIF-')],
  [sg.B('确认')],
    [sg.B('取消')],

]

window = sg.Window('文件路径', layout)

while True:
    event, Value = window.read()
    window['-GIF-'].update_animation(source='./转圈.gif',time_between_frames=100)
    if event is None:
        break
    if event=='确认':
        sg.popup_animated(image_source='./转圈.gif',time_between_frames=100)
    if event == '取消':
        sg.popup_animated(image_source=None)

window.close()
