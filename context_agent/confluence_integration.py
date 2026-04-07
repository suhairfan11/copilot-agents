class ConfluenceIntegration:
    def __init__(self, base_url, auth):
        self.base_url = base_url
        self.auth = auth

    def fetch_documentation(self, page_id):
        import requests
        url = f'{self.base_url}/rest/api/content/{page_id}'
        response = requests.get(url, auth=self.auth)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Error fetching documentation: ' + response.text)