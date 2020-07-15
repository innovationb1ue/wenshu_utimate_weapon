import base64
import json
import time

import requests

from APP_crawler.date_handler import date_handler2
from APP_crawler.wenshu_decoder_app import decode_json
from utils.cipher import CipherText


class WenShuAppCrawler:
    def __init__(self):
        self.json_format = self.load_json_format()
        self.s = requests.Session()

    def main(self):
        with open('../court_infos/level2_courts.json', 'r', encoding='utf-8') as f:
            courts_bundles_provincial = json.load(f)
        for court_bundle in courts_bundles_provincial:
            for court in court_bundle:
                for date in date_handler2(2020, 1, 1, 2020, 7, 1):
                    name = court['name']
                    print(name, date)
                    post_json = self.get_search_json(name, date, self.json_format)
                    b64_data = base64.b64encode(str(post_json).encode('utf-8'))
                    retjson = self.search(b64_data)
                    docids = json.loads(decode_json(retjson))['relWenshu']
                    print(len(docids))

    def search(self, b64data):
        resp = requests.post('http://wenshuapp.court.gov.cn/appinterface/rest.q4w', data={'request': b64data})
        if resp.status_code == 200:
            try:
                return resp.json()
            except Exception as e:
                print(str(e))
                time.sleep(5)
                return self.search(b64data)

    @staticmethod
    def get_search_json(name: str, date: str, json_format: json):
        json_format['params']['queryCondition'][0]['value'] = name
        json_format['params']['queryCondition'][1]['value'] = f'{date} TO {date}'
        json_format["params"]['ciphertext'] = CipherText()
        return json_format

    @staticmethod
    def load_json_format():
        with open('./search_list_params.json', 'r', encoding='utf-8') as f:
            json_format = json.load(f)
        return json_format


if __name__ == '__main__':
    e = WenShuAppCrawler()
    e.main()
