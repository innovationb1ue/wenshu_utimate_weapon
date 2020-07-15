import requests
from utils.cipher import CipherText
import json
import base64
from APP_crawler.wenshu_decoder_app import decode_json
json_format = \
    {
    "id":"20200312141952",
    "command":"queryDoc",
    "params":{
        "pageNum":"1",
        "sortFields":"s50:desc",
        "ciphertext":"1011010 110100 1101101 1010111 110000 1000010 1100010 110101 1110011 1010110 1010001 1111010 1001100 110010 1101010 1101000 110011 1110000 1100101 111000 1100001 1101110 1110000 1101101 110010 110000 110010 110000 110000 110111 110001 110101 1000011 1010111 1101001 1001010 1010010 110000 1101111 1000101 101011 1110010 1110010 1100111 1110010 1100110 1101001 110010 1110011 1101011 1110011 1010111 1011000 1010001 111101 111101",
        "devid":"23a9c9828da443abbcfa8ab452201fab",
        "devtype":"1",
        "pageSize":"1000",
        "queryCondition":[
            {
                "key":"s2",
                "value":"北京市高级人民法院" # 法院名称
            },
            {
                "key":"cprq",
                "value":"2020-07-01 TO 2020-07-03"
            }
        ]
    }
}

class WenShuAppCrawler:
    def __init__(self):
        self.s = requests.Session()

    def main(self):
        with open('../court_infos/level2_courts.json', 'r', encoding='utf-8') as f:
            courts_bundles_provincial = json.load(f)
        for court_bundle in courts_bundles_provincial:
            for court in court_bundle:
                name = court['name']
                print(name)
                json_format['params']['queryCondition'][0]['value'] = name
                json_format["params"]['ciphertext'] = CipherText()
                b64_data = base64.b64encode(json.dumps(json_format).encode('utf-8'))
                resp = self.s.post('http://wenshuapp.court.gov.cn/appinterface/rest.q4w', data={'request':b64_data})
                retjson = resp.json()
                text = decode_json(retjson)
                docids = json.loads(text)['relWenshu']
                print(len(docids))


if __name__ == '__main__':
    e = WenShuAppCrawler()
    e.main()