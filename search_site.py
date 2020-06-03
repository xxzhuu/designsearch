import tkinter as tk
import webbrowser as wb
#from design_search import *
#搜索灵感
def search_pinterest(site):
    search_site = 'https://www.pinterest.com/search/pins/?q={}&rs=typed&term_meta[]={}%7Ctyped'.format(site,site)
    wb.open_new(search_site)

def search_dribbble(site):
    search_site = 'https://dribbble.com/search/{}'.format(site)
    wb.open(search_site)

def search_behance(site):
    search_site = 'https://www.behance.net/search?search={}'.format(site)
    wb.open(search_site)

def search_google(site):
    search_site = 'https://www.google.com/search?safe=active&hl=en&sxsrf=ALeKk02SEdCqE21xe17pWYwvGRU8ukXwWQ%3A1588304848061&source=hp&ei=0JurXtlR0-vBA-qaptgK&q={}&oq={}&gs_lcp=CgZwc3ktYWIQAzIECCMQJzIFCAAQgwEyBAgAEEMyBQgAEIMBMgQIABBDMgQIABBDMgQIABBDMgQIABBDMgQIABBDMgQIABBDOgcIABCDARBDOgcIABAUEIcCOgIIAFDLD1iHFmD_F2gBcAB4AIABaYgBowSSAQM1LjGYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwjZ-YrS4JHpAhXTdXAKHWqNCasQ4dUDCAo&uact=5'.format(site,site)
    wb.open(search_site)

def search_designinspiration(site):
    search_site = 'https://www.designspiration.com/search/saves/?q={}&qa=typed&term_meta%5B%5D={}%7Ctyped%7Cword%7C0'.format(site,site)
    wb.open(search_site)

def search_inspirationde(site):
    search_site = 'https://www.inspirationde.com/?s={}&q='.format(site)
    wb.open(search_site)
#搜索图片
def search_picjumbo(site):
    search_site = 'https://picjumbo.com/search/{}'.format(site)
    wb.open_new(search_site)

def search_unsplash(site):
    search_site = 'https://unsplash.com/s/photos/{}'.format(site)
    wb.open(search_site)

def search_pixabay(site):
    search_site = 'https://pixabay.com/images/search/{}/'.format(site)
    wb.open(search_site)

def search_envato(site):
    search_site = 'https://elements.envato.com/all-items/{}'.format(site)
    wb.open(search_site)

def search_shopify(site):
    search_site = 'https://burst.shopify.com/photos/search?utf8=✓&q={}&button='.format(site)
    wb.open(search_site)

def search_pexels(site):
    search_site = 'https://www.pexels.com/zh-cn/search/{}/'.format(site)
    wb.open(search_site)

#搜png
def search_cleanpng(site):
    search_site = 'https://www.cleanpng.com/free/{}.html'.format(site)
    wb.open_new(search_site)

def search_pngtree(site):
    search_site = 'https://pngtree.com/so/{}'.format(site)
    wb.open(search_site)

def search_favpng(site):
    search_site = 'https://favpng.com/png_search/{}'.format(site)
    wb.open(search_site)

#搜矢量
def search_freepic(site):
    search_site = 'https://www.freepik.com/search?dates=any&format=search&page=1&query={}&sort=popular&type=vector'.format(site)
    wb.open_new(search_site)

def search_vecteezy(site):
    search_site = 'https://www.vecteezy.com/free-vector/{}'.format(site)
    wb.open(search_site)

def search_nipic(site):
    search_site = 'http://soso.nipic.com/?q={}'.format(site)
    wb.open(search_site)

def search_vectstock(site):
    search_site = 'https://www.vectorstock.com/free-vectors/{}-vectors'.format(site)
    wb.open(search_site)

#搜icon
def search_icons8(site):
    search_site = 'https://icons8.com/icons/set/{}'.format(site)
    wb.open_new(search_site)

def search_thenounproject(site):
    search_site = 'https://thenounproject.com/search/?q={}'.format(site)
    wb.open(search_site)

def search_iconfont(site):
    search_site = 'https://www.iconfont.cn/search/index?q={}&page=1&tag=hand'.format(site)
    wb.open(search_site)

#搜mockup
def search_unblast(site):
    search_site = 'https://unblast.com/search/{}/'.format(site)
    wb.open_new(search_site)

def search_placeit(site):
    search_site = 'https://placeit.net/?search={}'.format(site)
    wb.open(search_site)

def search_mockupworld(site):
    search_site = 'https://www.mockupworld.co/?s={}'.format(site)
    wb.open(search_site)

def search_mockupplanet(site):
    search_site = 'http://mockupplanet.com/?s={}'.format(site)
    wb.open(search_site)