# TODO make requests to github API

import requests
import logging

def get_github_user(username):
    
    # 404 errors
    # other errors
    # success
        # return a tuple of: (data, error)
        # success will: return (data, None)
        # error will: return (None, error)

    try:
        response = requests.get(f'https://api.github.com/users/{username}')
        
        if response.status_code == 404: # not found
            return None, f'Username {username} not found'
        
        response.raise_for_status()

        response_json = response.json()
        user_info = extract_user_info(response_json)
        return user_info, None #return data, error
    
    except Exception as er:
        logging.exception(er)
        return None, 'Error connecting to Github'


def extract_user_info(response_json):

    json_dict = { 
        'login': response_json.get('login'),
        'name': response_json.get('name'),
        'avatar_url': response_json.get('avatar_url'),
        'home_page': response_json.get('html_url'),
        'repos': response_json.get('public_repos'),
    }

    return json_dict
