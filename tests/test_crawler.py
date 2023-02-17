from app import crawler
from app import mock


def test_abc():
    robot = crawler.Crawler()
    data = robot.get_data()

    assert data == mock.FAKE_DATA
    assert 0
