import requests
from bs4 import BeautifulSoup

def scrape():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    #current_time = datetime.now().strftime("%Y-%m-%d-%I-%M-%S-%p")
    #dont need this right now
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    body = soup.body
    with open('./imdb-250.html', 'w', encoding='utf-8') as file:
        file.write(str(body))

#opening up the html file
with open('imdb-250.html', 'r', encoding='utf-8') as file:
    #reading it to memory
    imdb_250 = file.read()
#creating soup from beautifulsoup class with the file we passed in
soup = BeautifulSoup(imdb_250, 'html.parser')
#beautiful soup result set, set to movies 
movie_divs = soup.find_all('div', class_='sc-935ed930-0')
#itterate over each movie div in the Bs4 result set and print it
for movie_div in movie_divs:
    #each h3 is the title of each movie, find them
    h3_elements = movie_div.find_all('h3', class_='ipc-title__text')
    span_elements = movie_div.find_all('span', class_='sc-935ed930-8 iLiQCS cli-title-metadata-item')
    #loop over each movie title and print it
    for h3_element in h3_elements:
        print(h3_element.text)
    #loop over each metadata and use the python text method .strip() to remove white space
    for span_element in span_elements:
        print(span_element.text.strip())






# div class sc-935ed930-0
#title  h3 class ipc-title__text
#metadata div - sc-935ed930-7 bHIxWH cli-title-metadata
# the next 3 spans
#year
#length
#rated
#rating ipc-rating-star <span aria-label="IMDb rating: 9.3"