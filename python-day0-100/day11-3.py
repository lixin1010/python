import requests
import json


def main():
    resp = requests.get('http://news.baidu.com/')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])


if __name__ == '__main__':
    main()
