import tkinter as tk
from tkinter import LEFT

root = tk.Tk()
root.geometry('600x400')

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)
root.title("动态分析仪校准程序")

label = tk.Label(frame1, text="my_adcmt_6146", justify=LEFT)
label.pack(side= LEFT)
label = tk.Label(frame2, text="my_34401a", justify=LEFT)
label.pack(side= LEFT)
label = tk.Label(frame3, text="my_ca3xx", justify=LEFT)
label.pack(side= LEFT)

#显示标签
my_adcmt_6146_var = tk.StringVar()
my_34401a_var = tk.StringVar()
my_ca3xx_var = tk.StringVar()


my_adcmt_6146_label = tk.Label(frame1, text="GPIB", justify=LEFT,textvariable=my_adcmt_6146_var)
my_adcmt_6146_label.pack(side= LEFT)

my_34401a_label = tk.Label(frame2, text="GPIB", justify=LEFT,textvariable=my_34401a_var)
my_34401a_label.pack(side= LEFT)

my_ca3xx_label = tk.Label(frame3, text="GPIB", justify=LEFT,textvariable=my_ca3xx_var)
my_ca3xx_label.pack(side= LEFT)

frame1.pack(padx=1, pady=1)
frame2.pack(padx=10, pady=10)
frame3.pack(padx=20, pady=20)

def my_adcmt_6146_show(my_adcmt_6146_value):
    my_adcmt_6146_var.set(my_adcmt_6146_value)


def my_34401a_show(my_34401a_value):
    my_34401a_var.set(my_34401a_value)

def my_ca3xx_show(my_ca3xx_value):
    my_ca3xx_var.set(my_ca3xx_value)


on_hit = False
#文本显示框
def show():
    #接受值
    my_adcmt_6146_show("one")
    my_34401a_show("one")
    my_ca3xx_show("one")

    global on_hit
    if on_hit == False:
        on_hit = True
        var.set("内容")

    else:
        on_hit = False
        var.set("")

b = tk.Button(root, text='hit me', font=('Arial', 12), width=10, height=1, command=show)
b.pack()


var = tk.StringVar()    # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
l = tk.Label(root, textvariable=var, bg='grey', fg='white', font=('Arial', 12), width=60, height=10)
# 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
l.pack()



root.mainloop()