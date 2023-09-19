from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType

opt = Options()
opt.headless = False
proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': '127.0.0.1:7890',
    'sslProxy': '127.0.0.1:7890',
})
opt.proxy = proxy

driver = Firefox(options=opt)