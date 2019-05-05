# mock-request
_Bypass an API request by retrieving pre-saved responses_

## Description
This package allows you to write code that looks exactly like an API request, but which instead it loads response objects previously saved into pickle files. 

In order for `mock-request` to load the correct response object, the user must specify a lookup table containing the request attributes as well as the local address of the corresponding pickle file (see the **Usage** section below for details).

The creation of this package was motivated as part of an online course. By using `mock-request`, the code is not sensitive to API changes or server availability, thereby providing a robust and consistent interactive experience.

However, an interesting use case for this package is to write unit tests on code that performs API requests. By setting up mock requests, the unit testing framework is insensitive to network disruptions, server access, and API changes.  

## Requirements
This package requires installation of the following packages:
- `pandas>=0.24.2`
- `requests>=2.18.4`

It also requires the `pickle` package, but this is part of the Python standard library since `Python 1.4`.

## Installation
This package is installable via `pip`:
```shell
pip install mock-request
```
## Usage
ToDo: link to jupyter notebook showing example step-by-step

## Acknowledgements
Thanks to Lee Hachadoorian (@leehach) for working on the code that motivated this package –including the exmaple above–, as well as for bug report/fixes. Thanks to Amany Mayfouz (@amfz) for motivating including `kwargs` in the `.get()` method in version `0.0.2`.