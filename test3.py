import pandas as pd
import datetime
from db import MySqlHelper
from basic import get_date_shift, get_yesterday, to_datetime, get_today, check_is_UTC0, timing, logging_channels, date_range, datetime_to_str
from jieba_based import Composer_jieba
from keyword_usertag_report import keyword_usertag_report, delete_expired_rows
import jieba.analyse


@timing
def fetch_usertag_web_id_ex_day():
    query = "SELECT web_id, usertag_keyword_expired_day FROM web_id_table where usertag_keyword_enable=1"
    print(query)
    data = MySqlHelper('dione').ExecuteSelect(query)
    web_id_all = [d[0] for d in data]
    expired_day_all = [d[1] for d in data]
    return web_id_all, expired_day_all







if __name__ == '__main__':
    is_UTC0 = check_is_UTC0()
    jump2gcp = True
    date = get_yesterday(is_UTC0=is_UTC0) ## compute all browsing record yesterday ad 3:10 o'clock
    date_list = [date]
    jieba_base =Composer_jieba()
    all_hashtag = jieba_base.set_config()
    stopwords = jieba_base.get_stopword_list()
    stopwords_usertag = jieba_base.read_file('./jieba_based/stop_words_usertag.txt')
    web_id_all, expired_day_all = fetch_usertag_web_id_ex_day()


