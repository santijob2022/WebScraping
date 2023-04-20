import requests
from bs4 import BeautifulSoup
import random

user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
]

userMovieName= input("Enter movie: ")

######### Main page #########
res = requests.get('https://www.imdb.com/chart/top/',headers={'User-Agent':random.choice(user_agents_list)})
print(res.status_code)
html = res.text

soap = BeautifulSoup(html,'html.parser')
tbody = soap.find('tbody',{'class':'lister-list'})
trs = tbody.findAll('tr')
for tr in trs:
    td = tr.find('td',{'class':'titleColumn'})
    movieName = td.a.string.strip()
    if movieName == userMovieName:
        movieId = td.a['href']
        movieURL = 'https://www.imdb.com/' + movieId

        ######### Directors #########
        res2 = requests.get(movieURL,headers={'User-Agent':random.choice(user_agents_list)})
        #print(res2.status_code)
        html = res2.text
        soup2 = BeautifulSoup(html,'html.parser')
        div = soup2.find('div',{'class':['sc-52d569c6-3', 'jBXsRT']})
        directors_tags = div.div.ul.li.div.ul.find_all('li')
        directors_names = []
        directors_urls = []
        for dir in directors_tags:
            directors_names.append(dir.text.strip())
            directors_urls.append(f"https://www.imdb.com/{dir.a['href']}")

        print("Director(s): ",directors_names)
        #print(directors_urls)
        #print(movieURL)

        ######### Top 4 Directors' Movies #########
        for dir_name,dir_url in zip(directors_names,directors_urls):
            res3 = requests.get(dir_url,headers={'User-Agent':random.choice(user_agents_list)})
            #print(res3.status_code)
            html = res3.text
            soup3 = BeautifulSoup(html,'html.parser')

            knownFor = (soup3
                        .find('div', {'data-testid':'nm_flmg_kwn_for'})
                        .div
                        .find('div',{'data-testid':'shoveler-items-container'}))

            recommendedMovies = []
            for div in knownFor:
                title = div.find('a',{'class':'ipc-primary-image-list-card__title'}).text
                recommendedMovies.append(title)
            recommendedMovies = ', '.join(recommendedMovies)
            print(dir_name,"recommended movies are:",recommendedMovies)

        break