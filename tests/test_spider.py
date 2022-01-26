import spider

def test_get_china_province_covid19_data():
    details = spider.get_china_province_covid19_data()
    print(details)
    assert len(details) > 0

def test_get_world_covid19_data():
    statis, detail, vaccinations = spider.get_world_covid19_data()
    print(statis)
    print(detail)
    print(vaccinations)
    assert (len(statis.values()) > 0 )  & (len(detail) > 0 ) & (len(vaccinations.values()) > 0 )