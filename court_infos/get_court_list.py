from utils.wenshu_requests import WenshuRequest
from bs4 import BeautifulSoup as bs
import json
from utils.wenshu_decoder import decode_json

s = WenshuRequest()

def start():
    with open('./court_root_div.txt', 'r', encoding='utf-8') as f:
        a = f.read()
    soup = bs(a, 'lxml')
    province_tags = soup.find_all('div', attrs={'class': 'map_p'})
    root = [] # province codes
    for tag in province_tags:
        if t := tag['data-val']:
            root.append(t)
    with open('./root.json', 'a', encoding='utf-8') as f:
        json.dump(root, f)

def get_child_court_of_root():
    with open('./root.json', 'r', encoding='utf-8') as f:
        roots = json.load(f)
    root_childs = [] # level 1 courts
    for prov_code in roots:
        resp = get_child(prov_code, isParent=True)
        print(resp.json())
        root_childs.append(resp.json()['result']['fy'])
    with open('./level1_courts.json', 'w', encoding='utf-8') as f:
        json.dump(root_childs, f)

def get_all_courts():
    with open('./child_courts.json', 'r', encoding='utf-8') as f:
        courts = json.load(f) # [ {}, {} , ...]
    level2_courts = []
    for district in courts:
        for court in district:
            print(court)
            resp = get_child(court['id'], True)
            level2_courts.append(resp.json()['result']['fy'])
    with open('./level2_courts.json', 'w', encoding='utf-8') as f:
        json.dump(level2_courts, f)


def get_child(courtid, isParent=False) -> json:
    data = {
        'provinceCode': courtid,
        'searchParent': isParent,
        'cfg': 'com.lawyee.judge.dc.parse.dto.LoadDicDsoDTO@loadFy',
        '__RequestVerificationToken': 'iqMciGrmBiYYmg686IG2HWAa'
    }
    resp = s.post(data)
    if resp.status_code == 200:
        return resp

def test_results():
    with open('./level2_courts.json', 'r') as f:
        a = json.load(f)
    count = 0
    for i in a:
        for j in i:
            count += 1
    print(count)



if __name__ == '__main__':
    # start()
    # get_child_court_of_root()
    get_all_courts()