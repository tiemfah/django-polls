from typing import List
import requests
from selenium import webdriver


def get_links(url: str) -> List[str]:
    """Find all links on page at the given url.
       Return a list of all link addresses, as strings.
    """
    # chrome_options = Options()
    # chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--headless")
    # browser = webdriver.Chrome(options=chrome_options)
    browser = webdriver.ChromeOptions()
    browser.add_argument('--headless')
    browser.get(url)
    elements = browser.find_elements_by_tag_name('a')
    links = [element.get_attribute("href") for element in elements]
    browser.close()
    return links


def invalid_urls(urllist: List[str]) -> List[str]:
    temp = []
    for link in urllist:
        r = requests.head(link)
        if r.status_code == 404:
            temp.append(link)
    return temp


def main():
    # links = get_links("https://cpske.github.io/ISP/")
    # [print(link) for link in links]
    # bad_link = (invalid_urls(links))
    # [print(link)for link in bad_link]
    pass
