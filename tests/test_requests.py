import pytest
from mock_request.requests import MockRequests

# Non-existing files
params = [
    ("", "", FileNotFoundError),
    ("", "errors.csv", FileNotFoundError),
    ("", "", FileNotFoundError),
]

@pytest.mark.parametrize("f1, f2, req", params)
def test_init_MockRequests_error(f1, f2, req):
    with pytest.raises(req):
        MockRequests(f1, f2)


params = [
    # TODO-- add more tests
    ("./tests/files/requests_info_tests.json", "./tests/files/errors_tests.csv")
]
@pytest.mark.parametrize("f1, f2", params)
def test_init_MockRequests(f1, f2):
    requests = MockRequests(f1, f2)
    assert len(requests._lookup_table) == 1
