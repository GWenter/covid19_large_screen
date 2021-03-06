# -*- coding: utf-8 -*-
from flask import Flask as _Flask
from flask import jsonify
from flask import render_template
from flask.json import JSONEncoder as _JSONEncoder

import db


# 重写Flask框架中的JSONEncoder类中的default方法
class JSONEncoder(_JSONEncoder):
    def default(self, o):
        import decimal
        if isinstance(o, decimal.Decimal):
            return float(o)
        super(JSONEncoder, self).default(o)


class Flask(_Flask):
    json_encoder = JSONEncoder


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("databoard.html")


# 完成
@app.route('/get_world_map_data')
def get_world_map_data():
    """
    :return:json字符串 获取世界疫情地图数据
    """
    return jsonify(db.query_world_covid_data())


# 完成
@app.route('/get_china_map_data')
def get_china_map_data():
    """
    :return:json字符串  获取中国疫情地图数据
    """
    return jsonify(db.china_covid_data())


# 完成
@app.route('/get_china_rank_data')
def get_china_rank_data():
    """
    :return:中国新增确诊排行前5的城市(不包含境外输入)
    """
    return jsonify(db.query_china_rank_data())


# 完成
@app.route('/get_world_rank_data')
def get_world_rank_data():
    """
    :return:全球新增排行前5的国家
    """
    return jsonify(db.query_world_rank_data())


# 完成
@app.route('/get_continent_pie_data')
def get_continent_pie_data():
    """
    :return:各洲确诊数占比饼图数据
    """
    return jsonify(db.query_continent_pie_data())


# 完成
@app.route('/get_world_daily_confirm_data')
def get_world_daily_confirm_data():
    """
    :return:世界每日新增确认历史数据，数据格式 [[年/月/日,...], [每日确诊数]]
    """
    return jsonify(db.query_world_daily_confirm_data())


# 完成
@app.route('/get_world_daily_dead_data')
def get_world_daily_dead_data():
    """
    :return:世界每日新增死亡历史数据，数据格式 [[年/月/日,...], [每日确诊数]]
    """
    return jsonify(db.query_world_daily_dead_data())


# 完成
@app.route('/get_world_china_vaccinations')
def get_world_china_vaccinations_data():
    """
    :return:世界每日新增死亡历史数据，数据格式：最大接种数，最大接种率,[[日期,...], [世界接种数], [中国接种数], [世界接种率], [中国接种率]]
    """
    max, maxPer, data = db.query_world_china_vaccinations_data()
    return jsonify(max=max, maxPer=maxPer, data=data)


# 完成
@app.route('/get_world_static_list_data')
def get_world_static_list_data():
    """
    :return:大屏头部左边和右边疫情数字信息 ['中国累计接种','中国新增接种（较上日）','中国每百人接种','全球累计接种','全球新增接种（较上日）','全球每百人接种']
    """
    data = db.data_vaccine().to_dict()
    return jsonify(data)


if __name__ == '__main__':
    app.run()
