import tkinter as tk
import webbrowser as wb
from tkinter import ttk
from search_site import *

window = tk.Tk()
window.title('Design search')
window.geometry('400x200')
#var = tk.StringVar()
select2 = 'inspiration'

#选择搜索类型
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
    return site

def search_inspiration():
    #global select1
    #comboxlist.get()
    site=var_text()
    search_pinterest(site)
    search_dribbble(site)
    search_behance(site)
    search_google(site)

def search_image():
    #global select1
    #comboxlist.get()
    site=var_text()
    search_picjumbo(site)
    search_unsplash(site)
    search_pixabay(site)
    search_pexels(site)
    search_envato(site)
    search_shopify(site)

def search_png():
   # global select1
    #comboxlist.get()
    site=var_text()
    search_cleanpng(site)
    search_pngtree(site)
    search_favpng(site)

def search_vector():
   # global select1
    #comboxlist.get()
    site=var_text()
    search_freepic(site)
    search_vecteezy(site)
    search_nipic(site)
    search_vectstock(site)

def search_icon():
    #global select1
    #comboxlist.get()
    site=var_text()
    search_icons8(site)
    search_thenounproject(site)
    search_nipic(site)
    search_iconfont(site)

def search_mockup():
    #global select1
    comboxlist.get()
    site=var_text()
    search_unblast(site)
    search_placeit(site)
    search_mockupworld(site)
    search_mockupplanet(site)

#def if_english():
#def search_button(select2):
    #global select1
b = tk.Button(window, text = 'search_ins', font = ('Arial',18), width = 20,height = 2,command = search_inspiration)
b.place(x =80,y=80,anchor = 'nw')

#search_button()
tk.mainloop()



