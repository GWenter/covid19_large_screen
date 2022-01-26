# -*- coding: utf-8 -*-
import csv
import time
import traceback
from datetime import datetime
import utils
import spider
import pandas as pd

# ----------------------------------------开始保存爬取的数据到数据库-----------------------------------------------------


# 完成
def save_china_covid19_data():
    '''
    ['country','province', 'city', 'confirm_t', 'confirm_d', 'confirm_n', 'dead_', 'heal']
    :return:
    '''
    with open(r'data/save_china_covid19_data.csv', 'w', encoding='utf-8') as fd:
        list_ = spider.get_china_covid19_data()
        writer = csv.writer(fd)
        writer.writerows(list_)


# 完成
def save_world_covid19_data():
    '''
    [pub_date, continent, name, confirm, confirm_add, dead_, dead_add, heal, heal_add,
     nowConfirm, nowConfirmCompare, confirmAddCut, suspect, confirmCompare]
    :return:
    '''
    with open(r'data/save_world_covid19_data.csv', 'w', encoding='utf-8') as fd:
        list_ = spider.get_world_covid19_data()
        writer = csv.writer(fd)
        writer.writerows(list_)


# 完成
def save_vaccine():
    '''
    ['总接种','新增接种','每百人接种']

    :param data: ['total','new','per']
    :return:
    '''
    with open(r'data/save_vaccine.csv', 'w', encoding='utf-8') as fd:
        list_ = spider.get_vaccine()
        writer = csv.writer(fd)
        writer.writerows(list_)


# 完成
def save_world_map():
    '''

    :return: ['name','value']
    '''

    with open(r'data/save_map_data.csv', 'w', encoding='utf-8') as fd:
        list_ = spider.get_world_map()
        writer = csv.writer(fd)
        writer.writerows(list_)


# 完成
def save_world_covid19():
    '''
    [name,confirm,dead,recovered,in_treat,fatality_rate,recovery_date]
    :return:
    '''
    with open(r'data/save_world_covid19.csv', 'w', encoding='utf-8') as fd:
        list_ = spider.get_world_covid19()
        writer = csv.writer(fd)
        writer.writerows(list_)


# 完成
def save_chine_vaccine():
    '''

    :return:
    '''
    with open(r'data/save_china_vaccine.csv', 'w', encoding='utf-8') as fd:
        list_ = spider.get_china_vaccine()
        writer = csv.writer(fd)
        writer.writerows(list_)


# 完成
def save_world_daily_data():
    '''
    [year,date,confirm,dead,heal,confirm_add,dead_rate,heal_rate]
    :return:
    '''
    with open(r'data/save_world_daily_data.csv', 'w', encoding='utf-8') as fd:
        list_ = spider.get_world_daily_data()
        writer = csv.writer(fd)
        writer.writerows(list_)

# ----------------------------------------结束保存爬取的数据到数据库-----------------------------------------------------


# ----------------------------------------开始数据分析----------------------------------------------------------

# 完成   原世界疫情地图，现弃用，使用query_world_covid_data()
def query_world_map_data():
    """
    :return:世界疫情地图的数据，数据格式 [{name: 'Afghanistan',value: 28397.812},...]
    """
    data = pd.read_csv('data/save_map_data.csv', names=['name', 'value'])
    data_ = data.T
    list_ = []
    for i in data_:
        name = data_[i]['name']
        value = data_[i]['value']
        dict_ = {
            'name': utils.get_en_name(name),
            'value': value
        }
        list_.append(dict_)
    return list_


# 完成
def query_china_rank_data():
    """
    先按新增确诊降序排列，后按总确诊降序排序
    :return: 中国新增确诊排行前5的城市，数据格式 [[城市名称,...], [总确诊,...], [新增确诊,...], [总死亡,...], [总治愈,...]]
    """
    data_ = pd.read_csv('data/save_china_covid19_data.csv', names=['country', 'province', 'city', 'confirm_t', 'confirm_d', 'confirm_n', 'dead_', 'heal'])
    data_s = data_.sort_values(by='confirm_n', ascending=False)
    rank_ = data_s[~data_s['city'].str.contains('境外输入') & ~data_s['city'].str.contains('地区待确认')]
    list_ = [[], [], [], [], []]
    for i in range(0, 5):
        list_[0].append(rank_.iloc[i]['city'])
        list_[1].append(str(rank_.iloc[i]['confirm_t']))
        list_[2].append(str(rank_.iloc[i]['confirm_n']))
        list_[3].append(str(rank_.iloc[i]['dead_']))
        list_[4].append(str(rank_.iloc[i]['heal']))
    return list_


# 完成
def query_continent_pie_data():
    """
    :return:洲确诊数占比饼图数据,[{value: 1000,name: '亚洲'},{value: 2000,name: '南美洲'}]
    """
    data = pd.read_csv('data/save_world_covid19_data.csv',names=['pub_date', 'continent', 'name', 'confirm', 'confirm_add', 'dead_', 'dead_add', 'heal','heal_add', 'nowConfirm', 'nowConfirmCompare', 'confirmAddCut', 'suspect', 'confirmCompare'])
    data_con = data.groupby('continent', as_index=False)
    data_ = data_con.sum()
    list_ = []
    for i in range(0,6):
        dict_ = {
            'name': data_.iloc[i]['continent'],
            'value': str(data_.iloc[i]['confirm'])
        }
        list_.append(dict_)
    return list_


# 完成
def query_world_rank_data():
    """
    :return: 世界新增确诊排行前5的国家，数据格式 [[国家名称,...], [总确诊,...], [新增确诊,...], [新增死亡,...], [总死亡,...]]
    """
    data = pd.read_csv('data/save_world_covid19_data.csv',names=['pub_date', 'continent', 'name', 'confirm', 'confirm_add', 'dead_', 'dead_add', 'heal','heal_add', 'nowConfirm', 'nowConfirmCompare', 'confirmAddCut', 'suspect', 'confirmCompare'])
    data_s = data.sort_values(by='confirm_add', ascending=False)
    list_ = [[], [], [], [], []]
    for i in range(0, 5):
        list_[0].append(data_s.iloc[i]['name'])
        list_[1].append(str(data_s.iloc[i]['confirm_add']))
        list_[2].append(str(data_s.iloc[i]['confirm']))
        list_[3].append(str(data_s.iloc[i]['dead_add']))
        list_[4].append(str(data_s.iloc[i]['dead_']))
    return list_


# 完成
def data_vaccine():
    '''
    大屏头部左边和右边疫情数字信息 [新增死亡, 总死亡数, 总确诊数, 总治愈数, 新增治愈数, 总疫苗接种数]
    :return: data:['total','new','per']
    '''
    data = pd.read_csv('data/save_vaccine.csv', names=['total', 'new', 'per'])
    return data


# 完成
def query_world_daily_confirm_data():
    """
    :return: 世界每日新增确诊历史数据，数据格式 [[年/月/日,...], [每日确诊数]]
    """
    data = pd.read_csv('data/save_world_daily_data.csv', names=['year', 'date', 'confirm', 'dead', 'heal', 'confirm_add', 'dead_rate', 'heal_rate'])
    list_ = [[], []]
    for i in range(0, len(data)):
        date_ = str(int(data.iloc[i]['year'])) + '.' + str(data.iloc[i]['date'])
        date_t = time.strptime(date_, '%Y.%m.%d')
        list_[0].append(date_t)
        list_[1].append(str(data.iloc[i]['confirm_add']))
    return list_


# 完成
def query_world_daily_dead_data():
    """
    :return:世界每日新增死亡历史数据，数据格式 [[年/月/日,...], [每日确诊数]]
    """
    data = pd.read_csv('data/save_world_covid19_data.csv', names=['pub_date', 'continent', 'name', 'confirm', 'confirm_add', 'dead_', 'dead_add', 'heal','heal_add', 'nowConfirm', 'nowConfirmCompare', 'confirmAddCut', 'suspect', 'confirmCompare'])
    list_ = [[], []]
    for i in range(0, len(data)):
        date_t = time.strptime(str(data.iloc[i]['pub_date']), '%Y%m%d')
        list_[0].append(date_t)
        list_[1].append(str(data.iloc[i]['dead_']))
    return list_


# 完成  但无世界接种疫苗数据，故设0
def query_world_china_vaccinations_data():
    """
    :return:(最大接种数，最大接种率， [[日期,...], [世界接种数,...], [中国接种数,...], [世界接种率,...], [中国接种率,...]])
    """
    data = pd.read_csv('data/save_china_vaccine.csv', names=['year', 'date', 'total', 'per'])
    list_ = [[], [], [], [], []]
    for i in range(0, len(data)):
        date_ = str(int(data.iloc[i]['year'])) + '.' + str(data.iloc[i]['date'])
        date_t = time.strptime(date_, '%Y.%m.%d')
        list_[0].append(date_t)     # 日期
        list_[1].append(str(0))     # 世界接种数
        list_[2].append(str(data.iloc[i]['total']))     # 中国接种数
        list_[3].append(str(0))  # 世界接种率
        list_[4].append(str(data.iloc[i]['per']))   # 中国接种率
    max = '2000000000'
    maxPer = '200'
    return max, maxPer, list_


# 完成
def query_world_covid_data():
    '''
    世界疫情地图的数据，数据格式 [{name: 'Afghanistan',value: 28397.812},...]
    :return:
    '''
    data = pd.read_csv('data/save_world_covid19_data.csv', names=['pub_date', 'continent', 'name', 'confirm', 'confirm_add', 'dead_', 'dead_add', 'heal', 'heal_add', 'nowConfirm', 'nowConfirmCompare', 'confirmAddCut', 'suspect', 'confirmCompare'])
    data_c = pd.read_csv('data/save_china_covid19_data.csv', names=['country', 'province', 'city', 'confirm_t', 'confirm_d', 'confirm_n', 'dead_', 'heal'])
    data_pro = data_c.groupby('country', as_index=False)
    data_1 = data_pro.sum()
    value_china = str(data_1['confirm_t'][0])
    list_ = [{'name': 'China', 'value': value_china}]
    for i in range(0, len(data)):
        name = utils.get_en_name(data.iloc[i]['name'])
        value = str(data.iloc[i]['confirm'])
        list_.append({'name': name, 'value': value})
    return list_


# 完成
def china_covid_data():
    '''
    ['country','province', 'city', 'confirm_t', 'confirm_d', 'confirm_n', 'dead_', 'heal']
    :return:
    '''
    data_ = pd.read_csv('data/save_china_covid19_data.csv', names=['country', 'province', 'city', 'confirm_t', 'confirm_d', 'confirm_n', 'dead_', 'heal'])
    data_pro = data_.groupby('province', as_index=False)
    data_1 = data_pro.sum()
    list_china = []
    for i in range(0, len(data_1)):
        name = data_1.iloc[i]['province']
        value = str(data_1.iloc[i]['confirm_t'])
        list_china.append({"name": name, "value": value})
    return list_china


# 完成
def china_covid_all_data():
    '''
    用于全球疫情数据获取中国地区数据
    :return:
    '''
    data_ = pd.read_csv('data/save_china_covid19_data.csv', names=['country', 'province', 'city', 'confirm_t', 'confirm_d', 'confirm_n', 'dead_', 'heal'])
    data_pro = data_.groupby('country', as_index=False)
    data_1 = data_pro.sum()
    value = data_1['confirm_t'][0]
    return value

# ----------------------------------------结束分析数据库的数据----------------------------------------------------------


def save_daily_covid_data():
    """
    linux定时器每日调用此函数，爬取每日疫情数据并存储到数据库。
    :return:
    """
    save_china_covid19_data()
    save_world_covid19_data()
    save_vaccine()
    save_world_map()
    save_world_covid19()
    save_chine_vaccine()
    save_world_daily_data()


if __name__ == '__main__':
    save_daily_covid_data()
