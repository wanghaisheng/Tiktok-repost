import random
import sys
import time
import os
from crawlers import Crawlers
import configparser


config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')
crawlers_config = config['Crawlers']
keywords_english = crawlers_config['Keywords_english']
keywords_chinese = crawlers_config['Keywords_chinese']


def kill_orphan_chrome():
    num = 1
    while True:
        if sys.argv[1] == 'test':
            break
        else:
            if os.popen('ps -f --ppid 1 | grep chromedriver').read():
                try:
                    os.system("ps -f --ppid 1 | grep chromedriver | awk '{print $2}' | xargs kill -9")
                except:
                    pass
            if os.popen('ps -f --ppid 1 | grep chrome').read():
                try:
                    os.system("ps -f --ppid 1 | grep chrome | awk '{print $2}' | xargs kill -9")
                except:
                    pass
            if os.popen('ps -f --ppid 1 | grep chromedriver').read() == '' and os.popen(
                    'ps -f --ppid 1 | grep chrome').read() == '':
                break
        num += 1
        time.sleep(random.uniform(0.1, 0.2))
        if num > 3:
            break


crawler = Crawlers()
if crawlers_config['Tiktok_crawler'] == 'True' or crawlers_config['Youtube_crawler'] == 'True':
    for keyword in keywords_english.split(','):
        try:
            kill_orphan_chrome()
            print(f'keyword: {keyword}')
            if crawlers_config['Tiktok_crawler'] == 'True':
                try:
                    crawler.tiktok_crawler(keyword)
                except:
                    pass
            if keyword == 'funny' or keyword == 'hot':
                if crawlers_config['Youtube_crawler'] == 'True':
                    try:
                        crawler.youtube_crawler(keyword)
                    except:
                        pass
            time.sleep(6)
        except:
            continue
if crawlers_config['Douyin_crawler'] == 'True':

    for keyword in keywords_chinese.split(','):
        try:
            kill_orphan_chrome()
            print(f'keyword: {keyword}')
            if crawlers_config['Douyin_crawler'] == 'True':
                crawler.douyin_crawler(keyword)
            time.sleep(6)
        except Exception as e:
            print(f'error: {e}')
            continue
