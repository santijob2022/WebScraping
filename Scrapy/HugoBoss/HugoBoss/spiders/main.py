import scrapy
from scrapy import Request

class IMDBSpider(scrapy.Spider):
    name = 'boss'
    start_urls = ['https://www.hugoboss.com/us/men/']    

    def parse(self, response):
        """
            We start at https://www.hugoboss.com/us/men/
            We will continue to men's clothing
        """        
        cssSel = """a[data-as-levelinfo='{"levelID":"21000", "levelName":"Men_Clothing"}']+div ul li a::attr(href)"""        
        links = response.css(cssSel).getall() # This provides a list
        for link in links:
            yield Request(link, callback=self.parseProducts)            

    def parseProducts(self, response):
        """
            We will visit each product for each type of clothing
            We will need pagination to visit all products
        """
        #print("\n\n Links:")        
        #print(response.url)
        cssSel = '.search-result-content__wrapper .product-tile-plp__gallery a::attr(href)'
        for prodUrl in response.css(cssSel).getall():
            yield response.follow(prodUrl, callback=self.parseProduct)

        # This part adds the pagination
        #nextPageCss = '.pagingbar__items.pagingbar__items--desktop li.pagingbar__item.pagingbar__item--arrow a::attr(href)'
        nextPageCss= '.pagingbar__items--desktop a.pagingbar__next::attr(href)'
        nextPageUrl = response.css(nextPageCss).get()
        if (nextPageUrl): 
            yield Request(nextPageUrl, callback=self.parseProducts)
        

    def parseProduct(self,response):
        """
            For each product for each type of product:
            We extract: the name, the colors available and the images of size 1920px
        """
        productName = response.css('.pdp-stage__header-title::text').get().strip()
        colors = response.css('.slides__container.js-slides-container a::attr(title)').getall()
        colors = ','.join(colors)
        #colors = ','.join([color.strip() for color in colors])
        cssSel = ".pdp-images__adaptive-picture.js-slide source[media='(min-width: 1920px)']:first-child::attr(srcset)"
        imagesUrls = response.css(cssSel).getall()
        #imagesUrls = ','.join(images)

        yield{
            'Product Name':productName,
            'Available Colors':colors,
            'Images 1920px':imagesUrls
        }


        


