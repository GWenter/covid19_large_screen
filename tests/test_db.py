import db

def test_save_world_covid19_data():
    """
    测试db.py中的save_world_covid19_data函数
    :return:
    """
    db.save_world_covid19_data()


def test_save_china_covid19_data():
    """
    测试db.py中的save_china_covid19_data函数
    :return:
    """
    db.save_china_covid19_data()

def test_query_world_map_data():
    """
    数据条目数一致，则表示通过测试
    :return:
    """
    data = db.query_world_map_data()
    print(data)
    assert len(data) > 0

def test_query_china_map_data():
    data = db.query_china_map_data()
    assert len(data) > 0

def test_query_china_rank_data():
    data = db.query_china_rank_data()
    assert len(data[0]) >= 5


def test_query_world_rank_data():
    data = db.query_world_rank_data()
    assert len(data[0]) >= 5


def test_query_continent_pie_data():
    data = db.query_continent_pie_data()
    assert len(data) >= 5


def test_query_world_daily_confirm_data():
    data = db.query_world_daily_confirm_data()
    assert len(data[0]) >= 5


def test_query_world_daily_dead_data():
    data = db.query_world_daily_dead_data()
    assert len(data[0]) >= 5


def test_query_world_china_vaccinations_data():
    max, maxPer, data = db.query_world_china_vaccinations_data()
    assert len(data[0])


def test_query_world_static_list_data():
    data = db.query_world_static_list_data()
    assert len(data) == 6

def test_save_daily_covid_data():
    db.save_daily_covid_data()