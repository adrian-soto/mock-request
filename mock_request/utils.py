# This module contains utility functions to
# help set up the mocked request.
import json
import pickle

def save_requests_info(requests_info, path):
    """
    Save a dictionary containing request information to JSON file.

    :param requests_info: dictionary containing request info.
    :param path: path to JSON file.
    :return:
    """

    json_data = json.dumps(requests_info)

    with open(path, "w") as f:
        f.write(json_data)


def pickle_response(response, path):
    """
    Save your response into a pickle file.

    :param response: response object to be pickled.
    :param path: path to file where pickle file will
        be saved.
    """

    with open(path, "wb") as f:
        pickle.dump(response, f)
