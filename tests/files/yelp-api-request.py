#!/usr/bin/env python
# coding: utf-8

# # Get a Yelp API response

# In[1]:


import requests
import pickle
import yaml


# You must create the `../.private/api_key.yml` YAML file with the following structure:
# 
# ```
# - API_KEY:
#     <YOUR API KEY VALUE>
# ```
# 

# In[2]:


# Read API key
with open("../.private/api_key.yml", "r") as f:
    API_KEY = yaml.load(f)[0]["API_KEY"]


# In[3]:


# Define the base URL for the request
base_url = "https://api.yelp.com/v3/businesses/search"

# Set up the request headers -- API key is used here
headers = {"Authorization": "Bearer " + API_KEY}


# In[4]:


# Define the request parameters
params = {
    "location": "Newark, NJ",
    "term": "laundromat",
    "limit": 5
}


# In[5]:


response = requests.get(
    base_url,
    headers=headers,
    params=params
)


# In[6]:


with open("./yelp-api-laundromat-newark-response.pkl", "wb") as f:
    pickle.dump(response, f)


# # Is my key exposed in the response?
# 

# In[7]:


from inspect import ismethod


# In[8]:


# Load pickled response
with open("./yelp-api-laundromat-newark-response.pkl", "rb") as f:
    loaded_response = pickle.load(f)
    

# List of methods to skip in the check
SKIP = [
    "__nonzero__", 
    "__setstate__", 
    "__repr__", 
    "__iter__", 
    "__module__", 
    "__init__", 
    "next"
]

# Check if API_KEY is in response attributes
for name in dir(loaded_response):
    
    if name in SKIP:
        continue
    
    # 
    att = getattr(loaded_response, name)
 
    if ismethod(att):
        att_text = str(att())
    elif not isinstance(att, str):
        att_text = str(att)
    else:
        att_text = att

    if API_KEY in att_text:
        print(name, ": FAIL.\tWARNING: KEY EXPOSED!")

    else:
        print(name, ": PASS.")


# # Errors

# In[9]:


# 
errored_requests = [
    # Wrong base URL
    {
        "pickle_file": "./yelp-api-wrong-base-url-response.pkl",
        "url": "https://api.yelp.com/v3/a_wrong_url",
        "headers": headers,
        "params": params
    },
    
    # Missing API key
    {
        "pickle_file": "./yelp-api-missing-key-response.pkl",
        "url": base_url,
        "params": params,
        "headers": {}
    },
    
    # Wrong location parameter name
    {
        "pickle_file": "./yelp-api-wrong-location-parameter-response.pkl",
        "url": base_url,
        "headers": headers,
        "params": {
            "locationnnnnnn": "Newark, NJ",
            "term": "laundromat",
            "limit": 5
        }
    }
]

for er in errored_requests:

    with open(er["pickle_file"], "wb") as f:

        
        del(er["pickle_file"])
        
        r = requests.get(**er)

        #pickle.dump(r, f)
        print(r)


# # Save objects for tests

# In[10]:


from mock_request.utils import save_requests_info


# In[11]:


test_params = params.copy()
test_params["base_url"] = base_url
test_params["pickle_path"] = "/home/adrian/Projects/mock-request/tests/files/yelp-api-laundromat-newark-response.pkl"
save_requests_info([test_params], "./test.json")
del test_params["pickle_path"]


# In[12]:


from mock_request.requests import MockRequests


# In[13]:


requests = MockRequests("./requests_info_tests.json", "../tests/files/errors_test.csv", 404)


# In[14]:


# SCRATCHPAD

#requests._lookup_table['request_info'][0]# == test_params
#requests._lookup_table[requests._lookup_table['request_info'] == test_params]['pickle_path'].iloc[0]
requests._load_pickle(requests._lookup_table[requests._lookup_table['request_info'] == test_params]['pickle_path'].iloc[0])


# In[15]:


requests.get(base_url, test_params)

