# -*- coding: utf-8 -*-

# Copyright (c) 2017 Rohit Gupta
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

from os import path, system
import tkinter

self_name = path.basename(__file__)

file = path.expanduser('~\\Auge\\Auge.exe') # File name

dir_name = path.expanduser('~\\Auge') # Directory name

if not path.isdir(dir_name):
    system("mkdir "+dir_name)
if not path.isfile(file):
    copy_com = "copy Auge.exe "+dir_name+"\\"
    system(copy_com)
    task = "schtasks /Create /TN \"Auge\" /SC MINUTE /Mo 20 /tr " +"\"" + file +"\""
    system(task)


def countdown(count):
    label['text'] = 'Look away for : {0}s'.format(count)
    if count > 0:
        label.master.after(1000, countdown, count - 1)
    else:
        label.master.quit()


root = tkinter.Tk()
label = tkinter.Label(font=('Times New Roman', '80'), fg='black')
label.master.overrideredirect(True)

ws = label.master.winfo_screenwidth()
hs = label.master.winfo_screenheight()

hs = hs // 2 - 100
ws = ws // 4
label.master.geometry('+{0}+{1}'.format(ws, hs))
print (ws, hs)

label.master.lift()
label.master.wm_attributes('-topmost', True)
label.master.wm_attributes('-disabled', True)
label.master.wm_attributes('-transparentcolor', 'white')

label.pack()
countdown(20)

label.mainloop()
