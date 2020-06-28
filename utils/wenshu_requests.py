import requests

from utils.wenshu_param_handler import WenshuParamsHandler

from utils.wenshu_decoder import decode_json


class WenshuRequest:
    def __init__(self):
        self.s = requests.Session()
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'Host': 'wenshuapp.court.gov.cn',
            'Origin': 'http://wenshu.court.gov.cn',
            'Referer': 'http://wenshu.court.gov.cn/website/wenshu/181217BMTKHNT2W0/index.html?pageId=515e9cb57d11190521ad5cdd6d5bc998',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive'
        }
        try:
            self.handler = WenshuParamsHandler()
        except:
            self.handler = WenshuParamsHandler('./utils/ruishuCrackerJS.js')

    def post(self, data, retry=0, timeout=5):
        try:
            if retry == 5:
                print('Over maximum retry count !')
                return False
            url = 'http://wenshu.court.gov.cn/website/parse/rest.q4w?' + self.handler.get_url_postfix()
            headers = self.headers
            headers['Cookie'] = self.handler.get_cookies()
            resp = self.s.post(url, data=data, headers=self.headers, timeout=timeout)
        except Exception as e:
            print(str(e), 'retring count: 1')
            return self.post(data, retry=1)
        return resp

    def test(self):
        data = {'pageId': WenshuParamsHandler.get_pageid(),
                'sortFields': 's50:desc',
                'ciphertext': '1110010 1001000 1010111 1000110 1001101 1000110 1000111 1110100 1101010 1110011 1101000 1100110 1001010 1110001 1101010 1110010 1000100 1010101 1010111 1011010 1010110 1110010 110000 1111010 110010 110000 110010 110000 110000 110110 110010 110111 1011010 1100001 1010011 101111 1110100 1011000 1110100 1110001 1001011 110111 110011 1010110 1010111 110000 1010110 1110100 1110000 110100 1110000 1100001 110101 1000001 111101 111101',
                'pageNum': 1,
                'queryCondition': [],
                'cfg': 'com.lawyee.judge.dc.parse.dto.SearchDataDsoDTO@queryDoc',
                '__RequestVerificationToken': 'HJCFPWsuhmyKjOdPICxsjCoK'
                }
        resp = self.post(data)
        print(res := resp.json())
        print(decode_json(res))


if __name__ == '__main__':
    e = WenshuRequest()
    e.test()
