from urllib.parse import urlencode
import requests
import yaml


class RokuController:
    """Control a Roku that is accessible on your network"""

    def __init__(self):
        # Load the config file
        with open('.config.yaml', 'r') as stream:
            self.config = yaml.load(stream)

    def __roku_api_address(self):
        return 'http://{}:{}'.format(self.config['roku_ip'], self.config['roku_port'])

    def search(self, **search_params_dict):
        search_params_string = urlencode(search_params_dict)
        response = requests.post('{}/search/browse?{}'.format(self.__roku_api_address(), search_params_string), data={})
        response.raise_for_status()

    def key_press(self, key_name):
        response = requests.post('{}/keypress/{}'.format(self.__roku_api_address(), key_name), data={})
        response.raise_for_status()
