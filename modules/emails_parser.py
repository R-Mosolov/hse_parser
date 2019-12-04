from bs4 import BeautifulSoup as bs
from modules import links_constructor
from modules import session_generator


def run():
    request = session_generator.run('https://www.hse.ru/org/persons/133883850')
    links_arr = links_constructor.run()

    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        emails_links = soup.find_all('dl', attrs={'class': 'main-list'})

        return emails_links

    else:
        return 'Connection error'
