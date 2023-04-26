# WebScraping
Some Web scraping projects: requests, BeatifulSoup, Scrapy, and Selenium.

## Project 1: Movie Recommender

### Tools used:
Libraries: **requests** and **BeautifulSoup**

1. The file **[1_merging_search.py](https://github.com/santijob2022/WebScraping/blob/master/BS4/recommenderSystem/1_merging_search.py)** contained in the folder **[BS4/recommenderSystem](https://github.com/santijob2022/WebScraping/tree/master/BS4)** is a script that asks the user for the title of a movie.
2. The script looks for the movie on the website **https://www.imdb.com/chart/top/**.
3. It scraps the directors of the movie.
4. Then it gives the user the scraped top 4 movies for each of the found directors.

## Project 2: Fetching data from an e-commerce Website

### Tools used:
Libraries: **scrapy** and **Request**

1. The file **[products.csv](https://github.com/santijob2022/WebScraping/blob/master/Scrapy/HugoBoss/products.csv)** contains the final fetched data.
2. The columns are Product Name, Available Colors, and Image 1920px (pagination was used to fetch all the data).
3. The data was fetched in the following order.
    - Start at the website: https://www.hugoboss.com
    - Then the clothing for men was visited and each type of clothe was visited: https://www.hugoboss.com/us/men-clothing/
    - Then each product within each type of clothe was visited, for example https://www.hugoboss.com/us/regular-fit-polo-shirt-with-two-tone-micro-pattern/hbna50494991_404.html
    - From this direction, we collected the data: product name, available colors, and images of size 1920px.
