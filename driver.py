import glob
import re
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType

def import_cookies(fname: str, driver: Firefox):
    with open(fname) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    cookies = []
    for line in content:
        if line.startswith('#'):
            continue
        line = line.split('\t')
        if len(line) != 7:
            continue
        
        domain = line[0]
        domain_url = domain if not domain.startswith('.') else domain[1:]
        if driver.current_url.find(domain_url) == -1:
            driver.get(f'https://{domain_url}')
        cookies.append({
            'domain': domain,
            'path': line[2],
            'secure': line[3] == 'TRUE',
            'expiry': int(line[4]),
            'name': line[5],
            'value': line[6],
        })
    for cookie in cookies:
        driver.add_cookie(cookie)

def init_cookies(driver: Firefox):
    for cookie in glob.glob('cookies/*.txt'):
        import_cookies(cookie, driver)

opt = Options()
opt.headless = False
proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': '127.0.0.1:7890',
    'sslProxy': '127.0.0.1:7890',
})
opt.proxy = proxy

opt.profile = './profile'

driver = Firefox(options=opt)
# init_cookies(driver)