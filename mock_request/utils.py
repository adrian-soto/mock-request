import json
import pickle

def save_requests_info(requests_info, path):
    r"""
    Save a dictionary containing the request information to file
    """

    json_data = json.dumps(requests_info)

    with open(path, "w") as f:
        f.write(json_data)


def pickle_response(response, path):

    r"""
    Save your response into a pickle file.
    """

    with open(path, "wb") as f:
        pickle.dump(response, f)
