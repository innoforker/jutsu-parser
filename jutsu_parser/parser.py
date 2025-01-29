from bs4 import BeautifulSoup
import requests_cache as req # for caching requests
import sys
sys.path.append("..")
from jutsu_parser import __WEBSITE_URL__
from fake_useragent import UserAgent
import requests
import aiohttp

class JutsuParser:
    def __init__(self, web_cache_path="web-cache/jutsu_parser_cache"):
        self.target_url = __WEBSITE_URL__
        self.headers = {
            "User-Agent": UserAgent().random
        }
        self.web_cache_path = web_cache_path
        self.page_payload = {
            "ajax_load": "yes",
            "start_from_page": 1,
        }
        self.search_payload = {
            "makeme": "yes",
            "ystext": "",
        }
    
    def _get_requests_session(self, expiration_after=300):
        return req.CachedSession(cache_name=self.web_cache_path, expire_after=expiration_after, allowable_codes=[200, 301]) # Session will be expired after 300 seconds
    def _get_soup(self, url, page=1, search=False, search_query=None, fast_mode=False):
        session = self._get_requests_session() if not fast_mode else requests # For random techniques
        self.page_payload["start_from_page"] = page
        self.search_payload["ystext"] = search_query
        response = None
        if page <= 1:
            if search and search_query:
                redirect_url = session.post(url, timeout=10, headers=self.headers, data=search_payload).url
                return redirect_url[:-1] if 'search' not in redirect_url else None # Check if there are no results
            else:
                response = session.get(url, timeout=10, headers=self.headers)
        else:
            response = session.post(url, data=page_payload, timeout=10, headers=self.headers)
        response.raise_for_status() # Throws an exception if code is not 200
        soup = BeautifulSoup(response.text, "html.parser")
        for br in soup.find_all("br"):
            br.replace_with("\n") # To fix \r\n in text
        return soup
    # _fd - short for _find_div
    def _fd(self, soup, class_name, text=False):
        div = soup.find("div", {"class": class_name})
        return div if not text else div.text()

    def _get_card_info(self, card, id):
        anime_info = card.find("a") # "a" element with all anime card's in info
        anime_url = self.target_url + anime_info["href"][1:][:-1] # URL
        bg_style = _fd(anime_info, "all_anime_image")["style"] # background url image
        anime_image_url = bg_style.split("('", 1)[1].split("')")[0] # url without background-url
        anime_title = _fd(anime_info, "aaname", True)
        extra_info = _fd(anime_info, "aailines", True)
        if anime_url and anime_image_url and anime_title and extra_info:
            return {"@id": id, "title": anime_title, "image_url": anime_image_url, "release_url": anime_url, "extra": extra_info}
        return None
    def _find_anime_cards(self, soup):
        return soup.find_all("div", {"class": "all_anime_global"})
    def get_default_anime_list(self, page = 1):
        nav_url = f"{self.target_url}anime"
        soup = self._get_soup(nav_url, page)
        all_anime = self._find_anime_cards(soup)
        try:
            anime_list = [self._get_card_info(anime_release, i) for i, anime_release in enumerate(all_anime)]
        except IndexError:
            print("Failed to retrieve anime list.")
            return None
        return anime_list
    # Returns just a link to your anime by query (because jut.su has no search results)
    def get_anime_link_by_query(self, query):
        nav_url = f"{self.target_url}search"
        return self._get_soup(url=nav_url, search=True, search_query=query)
    def get_random_technique(self):
        soup = self._get_soup(self.target_url, fast_mode=True)
        technique = soup.find("div", {"class": "rand_tech_widget"}).find("a", {"class": "media_link"})
        return {
            "title": technique.find("span").text,
            "url": technique["href"],
            "image_url": technique.find("img")["src"]
        }
        
        
#########################################
# THE ASYNCHRONOUS VERSION OF JutsuParser
# ! WITHOUT CACHING
# ! DANGER. IT MAY BE UNSTABLE
#########################################
class Nurparse(JutsuParser):
    async def _get_async_soup(self, response):
        await response.raise_for_status()
        soup = BeautifulSoup(await response.text(), "html.parser")
        for br in soup.find_all("br"):
            br.replace_with("\n")
        return soup
    async def get_async_default_anime_list(self, page=1):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            if page <= 1:
                async with session.get(self.target_url + "anime") as response:
                    soup = await self._get_async_soup(response)
                    all_anime = self._find_anime_cards(soup)
                    try:
                        anime_list = [self._get_card_info(anime_release, i) for i, anime_release in enumerate(all_anime)]
                    except IndexError:
                        print("Failed to retrieve anime list.")
                        return None
                    return anime_list
            else:
                self.page_payload["start_from_page"] = page
                async with session.post(self.target_url + "anime", data=self.page_payload) as response:
                    soup = self._get_async_soup(response)
                    all_anime = self._find_anime_cards(soup)
                    try:
                        anime_list = [self._get_card_info(anime_release, i) for i, anime_release in enumerate(all_anime)]
                    except IndexError:
                        print("Failed to retrieve anime list.")
                        return None
                    return anime_list
    async def get_async_anime_link_by_query(self, query):
        self.search_payload["ystext"] = query
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.post(self.target_url + "search", data=self.search_payload) as response:
                await response.raise_for_status()
                return str(response.url)[:-1] if 'search' not in str(response.url) else None
    async def get_async_random_technique(self):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(self.target_url) as response:
                soup = self._get_async_soup(response)
                technique = soup.find("div", {"class": "rand_tech_widget"}).find("a", {"class": "media_link"})
                return {
                    "title": technique.find("span").text,
                    "url": technique["href"],
                    "image_url": technique.find("img")["src"]
                }
