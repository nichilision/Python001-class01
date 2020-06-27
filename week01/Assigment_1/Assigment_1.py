# Assignment 1: 安装并使用 requests、bs4 库，爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间，
#               并以 UTF-8 字符集保存到 csv 格式的文件中。

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'

header = {'Cookie': '__mta=51294998.1593019237048.1593192848759.1593196484073.12; uuid_n_v=v1; uuid=026FD5E0B63F11EA95E3C92BBC8FF019ED098A64C9154A7A9E2DCB2FFC2AD1E3; _lxsdk_cuid=172e7587c85c8-080e353e680b7e-f313f6d-1fa400-172e7587c85c8; _lxsdk=026FD5E0B63F11EA95E3C92BBC8FF019ED098A64C9154A7A9E2DCB2FFC2AD1E3; mojo-uuid=adfd98c2b51fa9ee77bd745aca426af8; _csrf=22f3e47e681ebbe1667b532acc4f6073216d5f4a319e8283f5418b1240eb744d; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593019235,1593019384,1593182423; mojo-session-id={"id":"51b68d3c9728e9671d711b9f21d570ae","time":1593221502313}; mojo-trace-id=1; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593221503; __mta=51294998.1593019237048.1593196484073.1593221509937.13; _lxsdk_s=172f366cd14-b4a-aac-1c6%7C%7C3','user-agent':user_agent}

myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl, headers=header)

bs_info = bs(response.text, 'html.parser')

movies_info = {'title':[], 'type':[], 'date':[]}

# First ten movies informations

for movies in bs_info.find_all('div', attrs={'class': 'movie-item-hover'})[:10]:

# Four elements

    total_info = movies.find_all('div', attrs={'class': 'movie-hover-title'})

#   actor = total_info[2].text

    title = total_info[0].get('title')
    type = total_info[1].text.split('\n')
    date = total_info[3].text.split('\n')



    movies_info['title'].append(title)
    movies_info['type'].append(type)
    movies_info['date'].append(date)

#print(movies_info)

ten_movies = pd.DataFrame(movies_info)
ten_movies.to_csv('./Assignment_1.csv', encoding='UTF-8', index= False, header= False )





