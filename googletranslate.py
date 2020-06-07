from googletrans import Translator

translater = Translator(service_urls = ['translate.google.cn'])
w = translater.translate('我是谁')
print(w.text)