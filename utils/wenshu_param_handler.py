import math
import random
import execjs

class WenshuParamsHandler:
    def __init__(self, crackjspath='./ruishuCrackerJS.js'):
        with open(crackjspath, 'r', encoding='utf-8') as f:
            jsstr = f.read()
        self.js = execjs.compile(jsstr)
        H80T = self.js.call('calljs', '80T')
        if len(H80T) < 50:
            raise ValueError('Invalid 80T')

    def get_cookies(self):
        CookieStr =  'HM4hUBT0dDOnenable=true; HM4hUBT0dDOn80S=HmncvkTXMmCe.WrF0RBm1y9eogzJie7PYfR2ByQABbm.m8yW3JD0C1.ju0xnIaNf; HM4hUBT0dDOn80T=H80T'
        new_H80T = self.js.call('calljs', '80T')
        return CookieStr.replace('H80T', new_H80T)

    @staticmethod
    def get_pageid():
        return "".join(hex(math.floor(random.random() * 16))[2:] for _ in range(32))

    def get_url_postfix(self):
        return self.js.call('calljs', 'J')




if __name__ == '__main__':
    e = WenshuParamsHandler()
    print(e.get_cookies())
    print(e.get_url_postfix())