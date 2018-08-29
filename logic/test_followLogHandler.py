import pytest

import mock
from unfollowLogManager import UnfollowLogManager

@pytest.fixture
def nc():
    nc = UnfollowLogManager('niclasguenther')
    return nc

def test_saveInstaInfoInDb(nc):
    nc = UnfollowLogManager('niclasguenther')
    nc.start()
    data_list = nc.getDataFromDb(5)
    users_list = nc.getDataFromDb(5, users_only=True)
    from pprint import pprint
    pprint(data_list)
    pprint(users_list)

    assert 1 == 2
