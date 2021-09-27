import requests
from bs4 import BeautifulSoup

HEADERS = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15', 'accept': '*/*'}

def engine(url, params=None):
    try:
        html = requests.get(url, headers=HEADERS, params=params)
        html = html.text
        soup = BeautifulSoup(html, 'html.parser')
        engine = soup.find('span', class_='css-hgkucx e162wx9x0').get_text(strip=True)
        return engine
    except Exception:
        return 'Не указано'

def transmission(url, params=None):
    try:
        html = requests.get(url, headers=HEADERS, params=params)
        html = html.text
        soup = BeautifulSoup(html, 'html.parser')
        rows = iter(soup.find('table').find_all('tr'))
        next(rows)
        back = []
        for row in rows:
            for cell in row.find_all('td'):
                back.append(cell.text)
        return back[2]
    except IndexError:
        return 'Не указано'

def power(url, params=None):
    try:
        html = requests.get(url, headers=HEADERS, params=params)
        html = html.text
        soup = BeautifulSoup(html, 'html.parser')
        rows = iter(soup.find('table').find_all('tr'))
        next(rows)
        back = []
        for row in rows:
            for cell in row.find_all('td'):
                back.append(cell.text)
        return back[0]
    except IndexError:
        return 'Не указано'

def wheel(url, params=None):
    try:
        html = requests.get(url, headers=HEADERS, params=params)
        html = html.text
        soup = BeautifulSoup(html, 'html.parser')
        rows = iter(soup.find('table').find_all('tr'))
        next(rows)
        back = []
        for row in rows:
            for cell in row.find_all('td'):
                back.append(cell.text)
        return back[3]
    except IndexError:
        return 'Не указано'

def color(url, params=None):
    try:
        html = requests.get(url, headers=HEADERS, params=params)
        html = html.text
        soup = BeautifulSoup(html, 'html.parser')
        rows = iter(soup.find('table').find_all('tr'))
        next(rows)
        back = []
        for row in rows:
            for cell in row.find_all('td'):
                back.append(cell.text)
        return back[4]
    except IndexError:
        return 'Не указано'

def milage(url, params=None):
    try:
        html = requests.get(url, headers=HEADERS, params=params)
        html = html.text
        soup = BeautifulSoup(html, 'html.parser')
        rows = iter(soup.find('table').find_all('tr'))
        next(rows)
        back = []
        for row in rows:
            for cell in row.find_all('td'):
                back.append(cell.text)
        return back[5]
    except IndexError:
        return 'Не указано'

def rule(url, params=None):
    try:
        html = requests.get(url, headers=HEADERS, params=params)
        html = html.text
        soup = BeautifulSoup(html, 'html.parser')
        rows = iter(soup.find('table').find_all('tr'))
        next(rows)
        back = []
        for row in rows:
            for cell in row.find_all('td'):
                back.append(cell.text)
        return back[6]
    except IndexError:
        return 'Не указано'

def discription(url, params=None):
    html = requests.get(url, headers=HEADERS, params=params)
    html = html.text
    soup = BeautifulSoup(html, 'html.parser')
    try:
        diskrip = soup.find('span', class_='css-sts55n e162wx9x0').get_text(strip=True)
        return diskrip
    except AttributeError:
        return 'Описания нет'

def image(url,params=None):
    try:
        html = requests.get(url, headers=HEADERS, params=params)
        html = html.text
        soup = BeautifulSoup(html, 'html.parser')
        images = soup.find('img', class_='css-1mnj4qi evrha4s0').get('src')
        return images
    except Exception:
        return 'Фото отсутствует'

def crime(url, params=None):
    try:
        html = requests.get(url, headers=HEADERS, params=params)
        html = html.text
        soup = BeautifulSoup(html, 'html.parser')
        rows = iter(soup.find('table', class_='css-16eu895 eppj3wm0').find_all('tr'))
        next(rows)
        back = []
        for row in rows:
            for cell in row.find_all('td'):
                back.append(cell.text)
        return back[-1]
    except Exception:
        return 'Не указано'

def polic_finding(url, params=None):
    try:
        html = requests.get(url, headers=HEADERS, params=params)
        html = html.text
        soup = BeautifulSoup(html, 'html.parser')
        rows = iter(soup.find('table', class_='css-16eu895 eppj3wm0').find_all('tr'))
        next(rows)
        back = []
        for row in rows:
            for cell in row.find_all('td'):
                back.append(cell.text)
        return back[-2]
    except Exception:
        return 'Не указано'
