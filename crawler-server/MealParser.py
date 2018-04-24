import asyncio
import aiohttp
import platform
import os
import codecs
import async_timeout
import random
import re
import datetime
from bs4 import BeautifulSoup
import Database

base_url = 'http://www.game.hs.kr/~game/2013/inner.php?sMenu=E4100&date='

async def update():
    now_time = datetime.datetime.now()
    await get_meal_list(now_time.strftime('%Y-%m-%d'))

async def get_meal_list(date):
    # print(date)
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
        url = base_url + date
        print(url)
        async with session.get(url) as res:
            html = await res.text()       
            soup = BeautifulSoup(html, 'html.parser')

            meal_list = soup.select('#Con > div.boardnew2011 > table > tbody > tr')
            for meals in meal_list:
                year = datetime.datetime.strptime(str(date), '%Y-%m-%d')
                year = year.strftime('%Y')
                contents_date = await get_meal_date(year, meals)
                contents = await get_meal_contents(meals)
                #print(date)
                # print(contents)

                meal_data = {}
                meal_data['date']   = contents_date['all']
                meal_data['week']   = contents_date['week']

                contents_array = []
                for content in contents:
                    content_box = {}
                    content_box['meal_type'] = content
                    content_box['meal_content'] = contents[content]
                    content_box['meal_choice_id'] = await Database.create_meal_choice_id(contents_date['all'] + contents_date['week'] + content)
                    contents_array.append(content_box)
                
                meal_data['contents'] = contents_array
                print(meal_data)

                await Database.insert_meal(meal_data)

async def get_meal_contents(meals):
    meal_contents = meals.select('td')
    meal_contents_box = {}
    meal_group = ['조식', '중식', '석식']
    index = 0
    index_of_group = 0
    for meal_content in meal_contents:
        if index % 2 != 0:
            # 밥
            meal_group_string = meal_group[index_of_group]
            meal_content_list = meal_content.text
            meal_content_list = meal_content_list.split('\n')
            meal_content_list = [meal_content.replace('\r','') for meal_content in meal_content_list]
            meal_content_list = [meal_content.replace('ㆍ','') for meal_content in meal_content_list]
            meal_content_group = []
            # print(meal_content_list)

            for meals in meal_content_list:
                try:
                    meals_list = re.findall('\w+', meals)
                    meal = meals_list[0]
                    # print(meal)
                    # print(meals)
                    # print(meals_list)
                    meal_content_group.append(meal)
                except:
                    pass

            # print(meal_content_group)
            # print('-----')
            # print(meal_content)
            # print(meal_group[index_of_group])
            meal_contents_box[meal_group[index_of_group]] = meal_content_group
            index_of_group += 1
        index += 1
    return meal_contents_box

async def get_meal_date(year, meals):
    meal_date = meals.find('strong').text
    regex = re.compile("(\d+월).(\d+일).(.)")
    mc = regex.findall(meal_date)[0]

    date_box = {}
    # Year, Month, Day, Week                
    mc_month = mc[0].replace('월','')
    mc_day = mc[1].replace('일','')
    mc_week = mc[2].replace(' ', '')

    date_box['all'] = year + mc_month + mc_day
    date_box['year'] = year
    date_box['month'] = mc_month
    date_box['day'] = mc_day
    date_box['week'] = mc_week
    return date_box