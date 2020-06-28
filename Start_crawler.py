import json

from utils.wenshu_decoder import decode_json
from utils.wenshu_param_handler import WenshuParamsHandler
from utils.wenshu_requests import WenshuRequest


class WenshuCrawler:
    def __init__(self):
        self.h = WenshuParamsHandler('./utils/ruishuCrackerJS.js')
        self.s = WenshuRequest()
        self.decode = decode_json

    def start_Crawl(self):
        data = {'pageId': WenshuParamsHandler.get_pageid(),
                's39': 'K20',
                'sortFields': 's50:desc',
                'ciphertext': '1110010 1001000 1010111 1000110 1001101 1000110 1000111 1110100 1101010 1110011 1101000 1100110 1001010 1110001 1101010 1110010 1000100 1010101 1010111 1011010 1010110 1110010 110000 1111010 110010 110000 110010 110000 110000 110110 110010 110111 1011010 1100001 1010011 101111 1110100 1011000 1110100 1110001 1001011 110111 110011 1010110 1010111 110000 1010110 1110100 1110000 110100 1110000 1100001 110101 1000001 111101 111101',
                'pageNum': 1,
                'pageSize': 999,
                'cfg': 'com.lawyee.judge.dc.parse.dto.SearchDataDsoDTO@queryDoc',
                '__RequestVerificationToken': 'HJCFPWsuhmyKjOdPICxsjCoK',
                'queryCondition': json.dumps(
                    [{"key": "s39", "value": "K20"}, {"key": "cprq", "value": "2020-06-01 TO 2020-06-02"}])
                }
        if resp := self.s.post(data, timeout=20):
            resjson = resp.json()
            text = self.decode(resjson)
            print(text)
            print(len(json.loads(text)['relWenshu']))

    def get_doc(self):
        data = {
            'docId': '8bf6c34e38de4702af90abde00361a1c',
            'ciphertext': '1110010 1001000 1010111 1000110 1001101 1000110 1000111 1110100 1101010 1110011 1101000 1100110 1001010 1110001 1101010 1110010 1000100 1010101 1010111 1011010 1010110 1110010 110000 1111010 110010 110000 110010 110000 110000 110110 110010 110111 1011010 1100001 1010011 101111 1110100 1011000 1110100 1110001 1001011 110111 110011 1010110 1010111 110000 1010110 1110100 1110000 110100 1110000 1100001 110101 1000001 111101 111101',
            'cfg': 'com.lawyee.judge.dc.parse.dto.SearchDataDsoDTO@docInfoSearch',
            '__RequestVerificationToken': 'r0EyAV2G9MI7XuDKkvqE0Ma8'
        }
        if resp := self.s.post(data, timeout=5):
            resjson = resp.json()
            text = self.decode(resjson)
            print(json.loads(text))


if __name__ == '__main__':
    e = WenshuCrawler()
    # e.start_Crawl()
    e.get_doc()
