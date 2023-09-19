from driver import driver
import json
from loguru import logger

@logger.catch
def get_reviews(url: str):
    driver.get(url)
    driver.find_element('css selector', '.Jwxk6d > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)').click()
    elements = driver.find_elements('css selector', 'div.RHo1pe')
    reviews = []
    for element in elements:
        quote = element.find_element('css selector', 'div.h3YV2d').text
        rating_ele = element.find_element('css selector', 'div.iXRFPc')
        rating = rating_ele.get_attribute('aria-label')
        rating = int(rating.split()[1])
        reviews.append((rating, quote))
    return reviews

if __name__ == '__main__':
    with open('apps.json') as f:
        apps = json.load(f)
    for app in apps:
        reviews = get_reviews(app)
        if reviews is None:
            continue
        fname = app.split('=')[-1]
        with open(f'data/{fname}.json', 'w') as f:
            json.dump(reviews, f, indent=2)
    driver.quit()