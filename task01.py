# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Essarai

import os
import time
import psutil as pt
from tkinter import *
from tkinter.messagebox import *


def getPidByName(Str):
    # 根据程序名获取所有pid
    pids = pt.process_iter()
    pidList = []
    for pid in pids:
        if pid.name() == Str:
            pidList.append(pid.pid)
    return pidList


def kill(pid):
    # 本函数用于中止传入pid所对应的进程
    if os.name == 'nt':
        # Windows系统
        cmd = 'taskkill /pid ' + str(pid) + ' /f'
        try:
            os.system(cmd)
            # print(pid, 'killed')
        except Exception as e:
            print(e)


class LoginPage(Frame):
    def __init__(self):
        super().__init__()
        self.soft_name = StringVar()
        self.time_set = StringVar()
        self.pack()
        self.createForm()

    def createForm(self):
        # 创建窗口
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='软件名称: ').grid(row=1, stick=W, pady=10)  # 360Game.exe
        Entry(self, textvariable=self.soft_name).grid(row=1, column=1, stick=E)
        Label(self, text='定时(/s): ').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.time_set).grid(row=2, column=1, stick=E)
        Button(self, text='确定', command=self.loginCheck).grid(
            row=3, stick=W, pady=10)
        Button(self, text='取消', command=self.quit).grid(
            row=3, column=1, stick=E)

    def loginCheck(self):
        try:
            count = 0
            soft_name = self.soft_name.get()
            time_set = int(self.time_set.get())
        except:
            showwarning(title='错误', message='请输入软件名和时间')
        else:
            while True:
                pid = getPidByName(soft_name)
                if pid != []:
                    while (count < time_set):
                        time.sleep(1)  # sleep 1 second
                        count += 1
                        pid = getPidByName(soft_name)
                    else:
                        for i in pid:
                            kill(i)
                        showinfo(title='成功', message='%s已停止！' % soft_name)
                        self.destroy()


def main():
    root = Tk()
    root.title('软件计时管理系统')
    width = 280
    height = 200
    # 居中对齐
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height,
                                (screenwidth-width)/2, (screenheight-height)/2)
    root.geometry(alignstr)
    page = LoginPage()
    root.mainloop()


if __name__ == "__main__":
    main()
