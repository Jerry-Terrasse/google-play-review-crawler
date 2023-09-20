import json

from driver import driver

url = 'https://play.google.com/store/apps'

def get_apps():
    elements = driver.find_elements('css selector', 'div.neq64b')
    print(elements)
    results = []
    for element in elements:
        a_tag = element.find_element('css selector', 'a')
        results.append(a_tag.get_attribute('href'))
    return results

if __name__ == '__main__':
    driver.get(url)
    input('please navigate to target page >')
    res = get_apps()
    json.dump(res, open('apps.json', 'w'), indent=2)
    driver.quit()