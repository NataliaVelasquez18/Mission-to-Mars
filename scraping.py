# Import Splinter BeautifulSoup Pandas WebDriverManager
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path)


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')
slide_elem.find("div", class_='content_title')

# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p

# ### Featured Images
try:
    PREFIX = "https://web.archive.org/web/20181114023740"
    url = f'{PREFIX}/https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    article = browser.find_by_tag('article').first['style']
    article_background = article.split("_/")[1].replace('");',"")
    print (f'{PREFIX}_if/{article_background}')
except:
    print('https://www.nasa.gov/sites/default/files/styles/full_width_feature/public/thumbnails/image/pia22486-main.jpg')

# ## Mars Facts
df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df


browser.quit()


