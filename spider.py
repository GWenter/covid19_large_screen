import datetime
import requests as req
import json
import jsonpath
import traceback
from lxml import etree


# 完成
def get_vaccine():
    '''

    return :['总接种','新增接种','每百人接种']
    第一行为中国的数据，第二行为全球数据
    '''
    url='https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=VaccineTopData'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    resp = req.get(url, headers=headers)
    html = resp.content.decode('utf-8')
    json_ = json.loads(html)
    vaccine = json_['data']['VaccineTopData']
    list_ = []
    for i in vaccine:
        total = vaccine[i]['total_vaccinations']
        new = vaccine[i]['new_vaccinations']
        per = vaccine[i]['total_vaccinations_per_hundred']
        list_.append([total, new, per])
    return list_


# 完成
def get_world_map():
    '''

    :return: {name:'',value:''}
    '''
    url = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    resp = req.get(url, headers=headers)
    html = resp.content.decode('utf-8')
    json_ = json.loads(html)
    map_ = json_['data']
    list_ = []
    for i in map_:
        name = i['name']
        value = i['confirm']
        list_.append([name, value])
    return list_


# 完成
def get_world_covid19():
    '''
    [name, confirm, dead, recovered, in_treat, fatality_rate, recovery_date]
    :return:
    '''
    url = 'https://www.outbreak.my/world'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    resp = req.get(url, headers=headers)
    html = resp.content.decode('utf-8')
    result_ = etree.HTML(html)
    data_t = result_.xpath('//*[@id="world_stats"]/tbody/tr')
    list_ = []
    for i in data_t:
        name = i.xpath('./td[1]/text()[2]')[0].strip()
        confirm = i.xpath('./td[2]/span/text()')[0].strip()
        dead = i.xpath('./td[4]/span/text()')[0].strip()
        recovered = i.xpath('./td[6]/span/text()')[0].strip()
        in_treat = i.xpath('./td[8]/span/text()')[0].strip()
        fatality_rate = i.xpath('./td[9]/span/text()')[0].strip()
        recovery_date = i.xpath('./td[10]/span/text()')[0].strip()
        list_.append([name, confirm, dead, recovered, in_treat, fatality_rate, recovery_date])
    return list_


# 完成
def get_world_covid19_data():
    '''
    [pub_date, continent, name, confirm, confirm_add, dead_, dead_add, heal, heal_add,
     nowConfirm, nowConfirmCompare, confirmAddCut, suspect, confirmCompare]
    :return:
    '''
    url = 'https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoCountryConfirmAdd,WomWorld,WomAboard'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    resp = req.get(url, headers=headers)
    html = resp.content.decode('utf-8')
    json_ = json.loads(html)
    data_ = json_['data']['WomAboard']
    list_ = []
    for i in range(0, len(data_)):
        continent = data_[i]['continent']
        name = data_[i]['name']
        confirm = data_[i]['confirm']
        confirm_add = data_[i]['confirmAdd']
        dead_ = data_[i]['dead']
        dead_add = data_[i]['deadCompare']
        heal = data_[i]['heal']
        heal_add = data_[i]['healCompare']
        pub_date = data_[i]['pub_date']
        nowConfirm = data_[i]['nowConfirm']
        nowConfirmCompare = data_[i]['nowConfirmCompare']
        confirmAddCut = data_[i]['confirmAddCut']
        suspect = data_[i]['suspect']
        confirmCompare = data_[i]['confirmCompare']
        list_.append([pub_date, continent, name, confirm, confirm_add, dead_, dead_add, heal, heal_add, nowConfirm, nowConfirmCompare, confirmAddCut, suspect, confirmCompare])
    return list_


# 完成
def get_china_covid19_data():
    '''
    ['国家',省份名称', ’城市名称‘, ’累计感染‘, ’今日感染‘, ’新增感染‘, ’死亡‘,'治愈']
    :return:
    '''
    url = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=statisGradeCityDetail,diseaseh5Shelf'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    resp = req.get(url, headers=headers)
    html = resp.content.decode('utf-8')
    json_ = json.loads(html)
    map_ = json_['data']['diseaseh5Shelf']['areaTree'][0]['children']
    list_ = []
    for pro in map_:
        for city in pro['children']:
            coutry = '中国'
            pro_ = pro['name']
            city_ = city['name']
            confirm_t = city['total']['confirm']
            confirm_d = city['today']['confirm']
            confirm_n = city['total']['nowConfirm']
            dead_ = city['total']['dead']
            heal_ = city['total']['heal']
            list_.append([coutry, pro_, city_, confirm_t, confirm_d, confirm_n, dead_,heal_])
    return list_


# 完成
def get_china_vaccine():
    '''

    :return:['年份','日期','总接种人数','每百人接种']
    '''
    url = 'https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=ChinaVaccineTrendData'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    resp = req.get(url, headers=headers)
    html = resp.content.decode('utf-8')
    json_ = json.loads(html)
    map_ = json_['data']['ChinaVaccineTrendData']
    list_ = []
    for i in map_:
        y = i['y']
        date = i['date']
        total = i['total_vaccinations']
        total_per = i['total_vaccinations_per_hundred']
        list_.append([y,date,total,total_per])
    return list_


# 完成
def get_world_daily_data():
    '''
    [year,date,confirm,dead,heal,confirm_add,dead_rate,heal_rate]
    :return:
    '''
    url = 'https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoGlobalStatis,FAutoGlobalDailyList,FAutoCountryConfirmAdd'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    resp = req.get(url, headers=headers)
    html = resp.content.decode('utf-8')
    json_ = json.loads(html)
    rank_ = json_['data']['FAutoGlobalDailyList']
    list_ = []
    for i in range(0, len(rank_)):
        year = rank_[i]['y']
        date = rank_[i]['date']
        confirm = rank_[i]['all']['confirm']
        dead = rank_[i]['all']['dead']
        heal = rank_[i]['all']['heal']
        confirm_add = rank_[i]['all']['newAddConfirm']
        dead_rate = rank_[i]['all']['deadRate']
        heal_rate = rank_[i]['all']['healRate']
        list_.append([year, date, confirm, dead, heal, confirm_add, dead_rate, heal_rate])
    return list_

