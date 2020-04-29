#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 14:33
# @Author  : Cxk
# @File    : C.py

from tkinter import *
from tkinter.messagebox import *
import random
 
def answer():
    global results,b1
    if b1==None:
        b1 = Toplevel()
        b1.title('答案')
        winWidth = 250
        winHeight = 600
        screenWidth = b1.winfo_screenwidth()
        screenHeight = b1.winfo_screenheight()
        x = int((screenWidth - winWidth) / 2)
        y = int((screenHeight - winHeight) / 2)
        # 设置窗口初始位置在屏幕居中
        b1.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x+430, y))
        # 设置窗口宽高固定
        b1.resizable(0, 0)
        result=results
#         print(result)
        results=""
        j=0
        for i in result:
            j+=1
            results+="   "+str(i)+"   "
            if j==3:
                Label(b1,font=("微软雅黑", 20),text=results).pack()
                j=0
                results=""
    else:
        pass
    
def range_num_10():
    """
    返回小于10的数
    """
    return random.randint(0,11)

def range_num_100():
    """
    返回小于100的数
    """
    return random.randint(0,101)

def range_ope():
    """
    返回操作符
    """
    a=random.randint(0,100)
    if a%2==0:
        return "+"
#     elif a%3==0:
#         return "X"
#     elif a%7==0:
#         return "÷"
    else:
        return "-"
    
def timu():
    global results
    result=[]
    for i in range(1,12):
        j=range_num_100()
        k=str(range_ope())
        l=range_num_10()
        a=0
        if k=="+":
            a=j+l
            result.append(a)
        else:
            a=j-l
            result.append(a)
        Label(root,font=("微软雅黑", 20),text=str(j)+k+str(l)+"=").grid(row=i,column=0)
        Entry(root,font="Helvetica 13 bold", bd =5,width=8).grid(row=i,column=1)

        j=range_num_100()
        k=str(range_ope())
        l=range_num_10()
        a=0
        if k=="+":
            a=j+l
            result.append(a)
        else:
            a=j-l
            result.append(a)
        Label(root,font=("微软雅黑", 20),text=str(j)+k+str(l)+"=").grid(row=i,column=2)
        Entry(root,font="Helvetica 13 bold", bd =5,width=8).grid(row=i,column=3)
        
        j=range_num_100()
        k=str(range_ope())
        l=range_num_10()
        a=0
        if k=="+":
            a=j+l
            result.append(a)
#         elif k=="X":
#             a=j*l
#             result.append(a)
#         elif k=="÷":
#             if l!=0:
#                 a=j/l
#                 result.append(a)
        else:
            a=j-l
            result.append(a)
        Label(root,font=("微软雅黑", 20),text=str(j)+k+str(l)+"=").grid(row=i,column=4)
        Entry(root,font="Helvetica 13 bold", bd =5,width=8).grid(row=i,column=5)
#     print(result)
    Button(text='查看答案', bd =5,width=10,command=answer).grid(row=13,column=1)
    Button(text='刷新题目', bd =5,width=10,command=del_all).grid(row=13,column=4)
    results=result
    
def del_all(): 
    """
    清空控件并刷新题目
    """
    global b1
    for widget in root.winfo_children():
        widget.destroy()
    timu()
    b1=None

root = Tk() 
root.title('小学一年级加减法') 
winWidth = 600
winHeight = 600
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
x = int((screenWidth - winWidth) / 2)
y = int((screenHeight - winHeight) / 2)
# 设置窗口初始位置在屏幕居中
root.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
# 窗口小图标
# # root.iconbitmap("./image/icon.ico")
# # 设置窗口宽高固定
root.resizable(0, 0)
global results,b1
b1=None
timu()
root.mainloop() 
