import json
import pickle

def save_requests_info(requests_info, path):
    r"""
    Save
    """

    json_data = json.dumps(requests_info)

    with open(path, "w") as f:
        f.write(json_data)


def pickle_request(request, path):

    r"""

    """

    with open(path, "wb") as f:
        pickle.dump(request, f)
