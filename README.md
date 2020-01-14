# mock-request
Mock API requests with and obtain a pre-saved response object.

With this package you can mock the behavior of the [`requests` library](https://requests.readthedocs.io/en/master/). You can write code that looks identical to the one you'd be using in an actual request, but which in reality loads pre-saved response objects with matching request parameters.

[![CircleCI](https://circleci.com/gh/adrian-soto/mock-request.svg?style=svg)](https://circleci.com/gh/adrian-soto/mock-request)
[![codecov](https://codecov.io/gh/adrian-soto/mock-request/branch/master/graph/badge.svg)](https://codecov.io/gh/adrian-soto/mock-request)


## Requirements
- `pandas>=0.23.0`
- `requests>=2.21.0`


## Usage
Until a more complete of examples is available, you can get a good sense of how to use this package by working through the `[tests/files/yelp-api-request.ipynb](https://github.com/adrian-soto/mock-request/blob/master/tests/files/yelp-api-request.ipynb) notebook`.

## Installation
This package is not yet available in PyPy, but you can still install it using `pip`. First clone the repo, navigate into the repo derectory, and then issue
```sh
$ pip install mock_request --user
```
in your terminal.


## History and usage
The creation of this package was originally created for online courses, for several reasons
1. hitting an API thousands of time a day from the same IP and/or with the same authentication will hit the daily download limit
1. the online course will not rely on the API servers, and will continue to work even if they're down or if the API changes
1. it shortens the execution time of online exercises

However, this package can be used for more generic situations. One good example would be to write unit tests for code performing API requests but without actually executing the requests.

## Contributing
I'll be happy (and proud!) if you'd like to contribute to this package. Feel free to open an issue explaining the fix/improvement/expansion you'd like to develop and let's discuss it.
