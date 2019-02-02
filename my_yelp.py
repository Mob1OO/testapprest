import requests

def search_businesses(search_term, search_location):

    api_key = "b6bMHyf3Fep0H4R-gBFS-Su-p74Eh_S-f_iUDjb2YTKtYM3micMNr6bi0cOIRU1gGFpfBOuKveAXzrHmTMXhGGDVYYEtjDHWfb7NWo-OyedJdqLwYFm_dQe8PdBVXHYx"

    url = "https://api.yelp.com/v3/businesses/search"

    my_headers = {
        "Authorization": "Bearer %s" % api_key
    }

    my_params = {
        "term": search_term,
        "location": search_location,
        "limit": 3,
    }

    businesses_object = requests.get(url, headers=my_headers, params=my_params)

    businesses_dict = businesses_object.text

    print(businesses_dict)

#calling the search_businesses function
search_businesses("restaurants", "chicago")
