# translate.py
# 翻譯功能
import json
import requests
from requests.exceptions import RequestException
from config import Config

config = Config()

class Translator:
    def __init__(self):
        self.auth_url = config.auth_url
        self.translate_url = f"{config.translate_url}?from={config.from_lang}&to={config.to_lang}&api-version={config.api_version}&includeSentenceLength=true"
        self.token = None

    def get_edge_token(self):
        """獲取認證 token。"""
        try:
            auth_headers = {"Content-Type": "text/plain; charset=utf-8"}
            response = requests.get(self.auth_url, headers=auth_headers).text
            self.token = response
        except RequestException as e:
            print(f"Error getting auth token: {e}")
            self.token = None

    def translate_zh_CH(self, contents):
        """將文本從一種語言翻譯到另一種語言。"""
        translate_headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        body = json.dumps([{"Text": contents}], separators=(",", ":"))
        try:
            response = requests.post(self.translate_url, headers=translate_headers, data=body)
            return response.json()[0]['translations'][0]['text']
        except RequestException as e:
            print(f"Error during translation: {e}")
            return None
