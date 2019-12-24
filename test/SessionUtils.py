import requests
import urllib3
from http import cookiejar

urllib3.disable_warnings()
session = requests.Session()
session.verify = False  # 取消验证 SSL


def setCookie(key, value):
    session.cookies.set(key, value)


def removeCookies(key=None):
    session.cookies.set(key, None) if key else session.cookies.clear()


def load_cookies(cookie_path="12306cookies.txt"):
    load_cookiejar = cookiejar.LWPCookieJar()
    load_cookiejar.load(cookie_path, ignore_discard=True, ignore_expires=True)
    load_cookies = requests.utils.dict_from_cookiejar(load_cookiejar)
    session.cookies = requests.utils.cookiejar_from_dict(load_cookies)


def save_cookies(cookie_path="12306cookies.txt"):
    new_cookie_jar = cookiejar.LWPCookieJar(cookie_path)
    requests.utils.cookiejar_from_dict({c.name: c.value for c in session.cookies}, new_cookie_jar)
    new_cookie_jar.save(cookie_path, ignore_discard=True, ignore_expires=True)