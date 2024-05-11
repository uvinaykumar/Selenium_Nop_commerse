import configparser
import json
conf = configparser.RawConfigParser()
conf.read('config.ini')


class ReadConfig:
    @staticmethod
    def getAppUrl():
        url = conf.get(section="common info", option='baseURL')
        #url=conf.get('common info','baseURL')
        #con_data=json.dump(url,open('config.json','rd'))
        return url


    @staticmethod
    def getUsername():
        username=conf.get(section="common info",option="username")
        return username
    @staticmethod
    def getPassword():
        password=conf.get(section="common info",option="password")
        return password

