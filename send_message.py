import yaml
import requests
import pandas as pd

from opens import ReadArchive

class ApiRequest:
    def __init__(self):
        try:
            with open("datas.yaml", 'r') as file:
                self.datas = yaml.safe_load(file)
            
            self.access_token = self.datas['access_token']
            self.file_path = self.datas['path']
        except FileNotFoundError:
            print("O arquivo datas.yaml não foi encontrado.")
            raise
        except KeyError as e:
            print(f"Chave ausente no arquivo YAML: {e}")
            raise

    def body(self, number, name, ids):
        url = "http://localhost:8080/message/sendText/Teste"

        headers = {
            'apikey': f'{self.access_token}',
            'Content-Type': 'application/json'
        }

        payload = {
            "number": number,
            "textMessage": {
                "text": f"Olá {name}, seu ID é {ids}."
            }
        }

        return url, headers, payload

    def request(self, url, headers, payload):
        try:
            response = requests.post(url, headers=headers, json=payload)
            
            if response.status_code == 200:
                print('Mensagem enviada com sucesso!')
                print(response.json())
            else:
                print('Falha ao enviar a mensagem.')
                print(f'Status Code: {response.status_code}')
                print(f'Resposta: {response.text}')
        except requests.exceptions.RequestException as e:
            print(f"Erro ao fazer a requisição: {e}")

    def send_messages(self):
        info = ReadArchive(self.file_path)
        names = info.get_name()
        numbers = info.get_number()
        ids = info.get_ids() 

        for number, name, ids in zip(numbers, names, ids):
            if pd.isna(number):
                number = ''
            if pd.isna(name):
                name = ''
            if pd.isna(ids):
                ids = ''
            
            url, headers, payload = self.body(number, name, ids)
            self.request(url, headers, payload)

api_request = ApiRequest()
api_request.send_messages()
