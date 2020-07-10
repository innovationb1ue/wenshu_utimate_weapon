import json

from utils.wenshu_decoder import decode_json
from utils.wenshu_param_handler import WenshuParamsHandler
from utils.wenshu_requests import WenshuRequest
from utils.token import RequestVerificationToken
from utils.cipher import CipherText


class WenshuCrawler:
    def __init__(self):
        self.h = WenshuParamsHandler('./utils/ruishuCrackerJS.js')
        self.s = WenshuRequest()

    def start_Crawl(self):
        timestr = '2020-03-22'
        with open('./court_infos/level2_courts.json', 'r', encoding='utf-8') as f:
            courts_bundles_provincial = json.load(f)
        for court_bundle in courts_bundles_provincial[:1]:
            boss_court_id = court_bundle[0]['id']
            for court in court_bundle:
                if court['parentid'] == "0":
                    print(court['name'], self.search_on_court(timestr, '2020-06-22', court['code'], 's38'))
                elif court['parentid'] == boss_court_id:
                    print(court['name'],self.search_on_court(timestr, '2020-06-22', court['code'], 's39'))
                else:
                    print(court['name'],self.search_on_court(timestr, '2020-06-22', court['code'], 's40'))

    def search_on_court(self, startdate:str, enddate, courtcode:str, keycode:str) -> str:
        data = {'pageId': WenshuParamsHandler.get_pageid(),
                keycode: '{}'.format(courtcode),
                'sortFields': 's50:desc',
                'ciphertext': CipherText(),
                'pageNum': 1,
                'pageSize': 5,
                'cfg': 'com.lawyee.judge.dc.parse.dto.SearchDataDsoDTO@queryDoc',
                '__RequestVerificationToken': RequestVerificationToken(24),
                'queryCondition': json.dumps(
                    [{"key": keycode, "value": '{}'.format(courtcode)},
                     {"key": "cprq", "value": "STARTDATE TO ENDDATE"
                         .replace('STARTDATE', startdate)
                      .replace('ENDDATE', enddate)}
                     ]
                    )  # 2019-01-01
                }
        if resp := self.s.post(data, timeout=10):
            try:
                resjson = resp.json()
                text = decode_json(resjson)
                return text.strip()
            except:
                print(resp.content.decode('utf-8'))
        else:
            return ''

    def get_doc(self):
        data = {
            'docId': '8bf6c34e38de4702af90abde00361a1c',
            'ciphertext': CipherText(),
            'cfg': 'com.lawyee.judge.dc.parse.dto.SearchDataDsoDTO@docInfoSearch',
            '__RequestVerificationToken': RequestVerificationToken(24)
        }
        if resp := self.s.post(data, timeout=5):
            resjson = resp.json()
            text = decode_json(resjson)
            print(json.loads(text))
        else:
            print(resp.content.decode('utf-8'))


if __name__ == '__main__':
    e = WenshuCrawler()
    # e.start_Crawl()
    e.get_doc()
