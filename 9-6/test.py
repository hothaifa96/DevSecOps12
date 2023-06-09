
from main import get_status_code
# test case is an function 
import pytest

@pytest.mark.parametrize('url',['https://google.com','https://youtube.com','https://mcdonalds.com','https://linkedin.com','htff.com'])
def test_get_Status_code(url):
    excepted = 2
    try:
        actual = get_status_code(url)
    except:
        pass
    assert actual == excepted