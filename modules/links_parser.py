from bs4 import BeautifulSoup as bs
from modules import session_generator


def run():
    request = session_generator.run('https://social.hse.ru/persons')

    links_arr = []

    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        links = soup.find_all('div', attrs={'class': 'fa-person__item'})

        for link in links:
            result = link.find('a', attrs={'class': 'fa-person__name'})['href']
            links_arr.append(result)

        return links_arr

    else:
        return 'Connection error'


