import requests


class DynV6:
    def __init__(self, token, api_url='https://dynv6.com/api/v2', timeout=60):
        self._token = token
        self.api_url = api_url
        self.timeout = timeout
        self._base_headers = {'Authorization': f'Bearer {self._token}',
                             'Accept': 'application/json'}

    def get_zone_details_by_name(self, zone_name):
        response = requests.get(f'{self.api_url}/zones/by-name/{zone_name}',
                                headers=self._base_headers, timeout=self.timeout)
        return response.json()

    def get_list_of_records(self, zone_id):
        response = requests.get(f'{self.api_url}/zones/{zone_id}/records',
                                headers=self._base_headers, timeout=self.timeout)
        return response.json()

    def add_txt_record(self, zone_id, name, data):
        json = {
            'name': name,
            'data': data,
            'type': 'TXT',
        }
        response = requests.post(f'{self.api_url}/zones/{zone_id}/records',
                                 headers=self._base_headers, json=json, timeout=self.timeout)
        return response.json()

    def del_record(self, zone_id, record_id):
        response = requests.delete(f'{self.api_url}/zones/{zone_id}/records/{record_id}',
                                   headers=self._base_headers, timeout=self.timeout)
        return response.status_code
