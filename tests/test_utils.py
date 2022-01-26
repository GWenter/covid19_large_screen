import utils


def test_get_con():
    con = utils.get_con()
    print(con)
    assert con is not None

def test_get_en_name():
    data = utils.get_en_name('中国')
    assert data == 'China'