import pickle
from ast import literal_eval
import pandas as pd


class MockRequests():
    r"""
    """
    def __init__(self, requests_data_path, errors_data_path, error_type=404):
        """Instantiate a MockRequests object.

        This object will contain the information to retrieve
        previously saved response objects given that the right
        request parameters are passed/provided.

        :param requests_data_path: Path to JSON file containing info
            of all stored request/response pairs.
        :param errors_data_path: Path to CSV file containing error
            type and file paths of error response objects.
        :param error_type: Error type to return if the mocked request
            is not among the saved response/request pairs.
        """

        # Path to file contaning data about all available requests
        self._requests_data_path = requests_data_path

        # Path to file contaning path to pickled request errors
        self._errors_data_path = errors_data_path

        # Error type to display if a wrong request is entered
        self._error_type = error_type


        # Read data from all accessible requests
        requests_data = self._load_requests_data()
        if not isinstance(requests_data, list):
            raise TypeError("The file %(filepath)s does contain a list.".format(self._requests_data_path))

        pickle_paths = list()
        for request_data in requests_data:
            if not isinstance(request_data, dict):
                raise TypeError("File %(filepath)s does not seem to contain a list of dictionaries.".format(self._requests_data_path))

            # Grab path to pickle and remove from dictionary
            pickle_paths.append(request_data['pickle_path'])
            del request_data['pickle_path']


        # From that data, create lookup table with two columns
        self._lookup_table = pd.DataFrame(
            list(zip(*[pickle_paths, requests_data])),  # list(zip(*...)) to transpose list of lists
            columns = ['pickle_path', 'request_info'])


    def get(self, base_url, params=None, **kwargs):
        # THIS IS THE DOCSTRING OF THE get method of the requests package (version x.y.z)
        """Sends a GET request.

        :param url: URL for the new :class:`Request` object.
        :param params: (optional) Dictionary or bytes to be sent in the query string for the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """
        # The get() function in the requests library is a wrapper
        # of the request() function. request() accepts many keyword
        # arguments, as it can be seen in its docstring
        #    https://github.com/kennethreitz/requests/blob/master/requests/api.py
        # In this implementation of the MockRequest.get() method,
        # only the 'headers' keyword argument is allowed. Later
        # versions of mock-request may include more of these
        # arguments.

        # Create dictionary containing the request information.
        request = {}
        request['base_url'] = base_url

        # Include params into dictionary, if any
        if params:
            request.update(params)

        # We could add checks of request headers by uncommenting
        # this code
        #
        # # Include headers, if any
        # if 'headers' in kwargs:
        #     request.update(kwargs['headers'])
        #
        # # This "if" can be generalized quite easily by looping
        # # over kwargs.keys()
        #

        # Do request parameters match any of the
        # rows in the lookup list?
        if (self._lookup_table['request_info'] == request).any():

            # Select all paths with matching request info
            path = self._lookup_table[self._lookup_table['request_info'] == request]['pickle_path']

            # Select the path in string form
            if len(path) != 1:
                raise ValueError('The path to this response is not unique.')
            else:
                path = path.iloc[0]

            # Load pickled response
            response = self._load_pickle(path)

        # If it doesn't match, return error response
        else:
            error_list = pd.read_csv(self._errors_data_path)
            error_path = error_list[error_list['error_type'] == self._error_type]['pickle_path'][0]
            response = self._load_pickle(error_path)

        return response


    def _load_pickle(self, path):
        """
        Load a pickle file.

        :param path: string containing path to pickle file.
        :return: object in pickle file.
        """
        with open(path, 'rb') as f:
            pickled_object = pickle.load(f)

        return pickled_object


    def _load_requests_data(self, path = None):
        """
        Load data of all requests from a file, each encoded in a dictionary.

        :param path: string containing path to data file.

        :return: list of dictionaries containing stored responses info and
            path to the pickled responses.
        """

        # Default _requests_data_path
        if path is None:
            path = self._requests_data_path

        with open(path, 'r') as f:
            return literal_eval(f.read())  # literal_eval converts string into python objects
