import pytest
from mock_request.requests import MockRequests

# Non-existing files
params = [
    ("", "", FileNotFoundError),
    ("", "errors.csv", FileNotFoundError),
    ("", "", FileNotFoundError)
]

@pytest.mark.parametrize("f1, f2, req", params)
def test_init_MockRequests(f1, f2, req):
    with pytest.raises(req):
        MockRequests(f1, f2)
