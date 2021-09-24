import requests
from bs4 import BeautifulSoup
import csv
import time
from card import *

HEADERS = {'user-agent': 'put_your_user_agent_here', 'accept': '*/*'}
FILE = 'cars.csv'

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_pages(html):
    soup = BeautifulSoup(html, 'html.parser')
    try:
        pagination = soup.find('a', class_='css-5k0bl6 e24vrp30').get('href')
        return pagination
    except Exception as ex:
        print(ex)
        print('Страницы закончились')
        return 1

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_= 'css-1psewqh ewrty961')
    cars = []
    cnt = 0
    for item in items:
        name_cars = item.find('div', class_='css-1svsmzw e1vivdbi2')
        if name_cars:
            name_cars = name_cars.find_next('span').get_text(strip=True)
        else:
            name_cars = 'Продано'
        cars.append({
            'title': name_cars,
            'link':item.get('href'),
            'price':item.find('span', class_= 'css-bhd4b0 e162wx9x0').find_next('span').get_text(strip=True),
            'set':item.find('div', class_='css-3xai0o e162wx9x0').get_text(strip=True),
            'city':item.find('span', class_='css-fbscyn e162wx9x0').get_text(strip=True),
            'engine':engine(item.get('href')),
            'transmission':transmission(item.get('href')),
            'power':power(item.get('href')),
            'wheel':wheel(item.get('href')),
            'color':color(item.get('href')),
            'milage':milage(item.get('href')),
            'rule': rule(item.get('href')),
            'crime':crime(item.get('href')),
            'police':polic_finding(item.get('href')),
            'image': image(item.get('href')),
            'diskription':discription(item.get('href')),
        })
        cnt += 1
        print(f'Take {cnt} cars')
    return cars

def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Модель', 'Ссылка', 'Цена', 'Комплектация', 'Город', 'Двигатель', 'Трансмиссия', 'Мощность', 'Привод', 'Цвет', 'Пробег', 'Руль', 'Ограничения', 'Розыск', 'Ссылка на главное фото', 'Описание'])
        for i in items:
            writer.writerow([i['title'], i['link'], i['price'], i['set'], i['city'], i['engine'], i['transmission'], i['power'], i['wheel'], i['color'], i['milage'], i['rule'], i['crime'], i['police'],i['image'], i['diskription']])

def parse():
    url = input('Put your Drom URL: ')
    time.sleep(2)
    html = get_html(url)
    if html.status_code == 200:
        print('Enter on web-site...')
        time.sleep(2)
        cars = []
        cnt = 1
        print('Find information about cars...')
        time.sleep(2)
        print('Wait...')
        while cnt <= 100:
            try:
                cars.extend(get_content(html.text))
                url = get_pages(html.text)
                html = get_html(url)
                print(f'\nParsing {cnt} page\n')
                cnt += 1
                time.sleep(3)
            except Exception as ex:
                print(ex)
                time.sleep(3)
                print('Ошибка в получении страниц')
                break
        time.sleep(2)
        print('Save file...')
        save_file(cars, FILE)
        time.sleep(2)
        print(f'Takes {len(cars)} cars')
    else:
        print('Error')

parse()
