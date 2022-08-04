import os

import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        TOKEN = ''
        filename = file_path.split('\\', )[-1]
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {TOKEN}'}
        params = {"path": f"{filename}", "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params).json()
        href = response.get("href", "")
        download_request = requests.put(href, data=open(file_path, 'rb'))
        download_request.raise_for_status()
        if download_request.status_code == 201:
            return 'Успешно'
        else:
            return f"Ошибка загрузки! Код ошибки: {download_request.status_code}"


if __name__ == '__main__':
    path_to_file = os.path.join(os.getcwd(), '4571316.jpg')
    token = ''
    uploader = YaUploader(token)
    print(f"Загрузка файла {path_to_file.split('/', )[-1]} пожалуйста, подождите ")
    result = uploader.upload(path_to_file)
    print(result)