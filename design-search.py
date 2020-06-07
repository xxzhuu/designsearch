# -*- coding:utf8 -*-
import tkinter as tk
import webbrowser as wb
from tkinter import ttk
from urllib.parse import quote
from googletrans import Translator
from search_site import *
#from googletranslate import *

window = tk.Tk()
window.title('Design search')
window.geometry('400x200')
#var = tk.StringVar()
select2 = 'inspiration'

#选择搜索类型  我是谁
def select(event):
    global select2
    #select = comboxlist.get()
    print(comboxlist.current(),comboxlist.get())
    select2 = comboxlist.get()
    if select2 == 'inspiration':
        b = tk.Button(window, text = 'search_ins', font = ('Arial',18), width = 20,height = 2,command = search_inspiration)
    elif select2 == 'image':
        b = tk.Button(window, text = 'search_img', font = ('Arial',18), width = 20,height = 2,command = search_image)
    elif select2 == 'png':
        b = tk.Button(window, text = 'search_png', font = ('Arial',18), width = 20,height = 2,command = search_png)
    elif select2 == 'vector':
        b = tk.Button(window, text = 'search_vector', font = ('Arial',18), width = 20,height = 2,command = search_vector)
    elif select2 == 'icon':
        b = tk.Button(window, text = 'search_icon', font = ('Arial',18), width = 20,height = 2,command = search_icon)
    else:
        b = tk.Button(window, text = 'search_mockup', font = ('Arial',18), width = 20,height = 2,command = search_mockup)
    b.place(x =80,y=80,anchor = 'nw')

#单选框
comvalue = tk.StringVar()
comboxlist = ttk.Combobox(window,textvariable = comvalue,state = 'readonly')
comboxlist['value'] = ('inspiration','image','png','vector','icon','mockup')
comboxlist.current(0)
comboxlist.bind('<<ComboboxSelected>>',select)
comboxlist.pack()

#select1 = comboxlist.current()

#输入框
e1 = tk.Entry(window, show = None, font=('Arial',20))
e1.pack()

def var_text():
    #global site
    site = e1.get()
    translate = Translator(service_urls = ['translate.google.cn'])
    site_en = translate.translate(str(site)).text
    site_cn = quote(site)
    print(site_en,site_cn)
    return site_en,site_cn

#判断是否为中文
#def is_chinese(site):
    #for _char in site:
       # if not '\u4e00' <= _char <='\u9fa5':
            #return False
    #return True

def search_inspiration():
    site=var_text()
    site_en = site[0]
    site_cn = site[1]
    search_pinterest(site_en)
    search_dribbble(site_en)
    search_behance(site_en)
    search_google(site_en)
    search_zcool_cn(site_cn)
    search_gtn9_cn(site_cn)

def search_image():
    site=var_text()
    site_en = site[0]
    site_cn = site[1]
    search_picjumbo(site_en)
    search_unsplash(site_en)
    search_pixabay(site_en)
    search_pexels(site_en)
    search_envato(site_en)
    search_shopify(site_en)

def search_png():
    site=var_text()
    site_en = site[0]
    site_cn = site[1]
    search_cleanpng(site_en)
    search_stickpng(site_en)
    search_pngtree(site_en)
    search_favpng(site_en)
    search_pngimg(site_en)

def search_vector():
    site=var_text()
    site_en = site[0]
    site_cn = site[1]
    search_freepic(site_en)
    search_vecteezy(site_en)
    search_nipic(site_en)
    search_vectstock(site_en)

def search_icon():
    site=var_text()
    site_en = site[0]
    site_cn = site[1]
    search_icons8(site_en)
    search_thenounproject(site_en)
    search_nipic_icon(site_en)
    search_iconfont(site_en)

def search_mockup():
    site=var_text()
    site_en = site[0]
    site_cn = site[1]
    search_unblast(site_en)
    search_placeit(site_en)
    search_mockupworld(site_en)
    search_mockupplanet(site_en)
    
#创建默认搜索框
b = tk.Button(window, text = 'search_ins', font = ('Arial',18), width = 20,height = 2,command = search_inspiration)
b.place(x =80,y=80,anchor = 'nw')

#search_button()
tk.mainloop()



