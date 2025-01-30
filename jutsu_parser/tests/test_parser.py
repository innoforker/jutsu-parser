import sys
sys.path.append("../..")
from jutsu_parser import parser
from random import randint
from asyncio import run

def log_info(message, success=True):
    print(f"[{'SUCCESS or NEUTRAL' if success else 'FAIL'}] {message}")

def test_default_anime_list():
    _parser = parser.JutsuParser("../web-cache/jutsu_parser_cache")
    log_info("Created web cache")
    anime_list = _parser.get_default_anime_list()
    if anime_list:
        log_info("Retrieved anime list successfully.")
        for anime in anime_list:
            print(f"ID: {anime['@id']}, Title: {anime['title']}, Image URL: {anime['image_url']}, Release URL: {anime['release_url']}, Extra Info: {anime['extra']}")
    else:
        log_info("Failed to retrieve anime list.", False)
    log_info("test_default_anime_list completed.")
def test_raw_anime_list():
    _parser = parser.JutsuParser("../web-cache/jutsu_parser_cache")
    log_info("Created web cache")
    anime_list = _parser.get_default_anime_list()
    if anime_list:
        log_info("Retrieved anime list successfully. Showing raw list.")
        print(anime_list)
    else:
        log_info("Failed to retrieve raw anime list.", False)
    log_info("test_raw_anime_list completed.")

def test_another_page_default_list():
    page = randint(3, 10)
    log_info(f"Page #{page}")
    _parser = parser.JutsuParser("../web-cache/jutsu_parser_cache")
    log_info("Created web cache")
    anime_list = _parser.get_default_anime_list(page)
    if anime_list:
        log_info(f"Retrieved anime list on page {page} successfully.")
        for anime in anime_list:
            print(f"ID: {anime['@id']}, Title: {anime['title']}, Image URL: {anime['image_url']}, Release URL: {anime['release_url']}, Extra Info: {anime['extra']}")
    else:
        log_info(f"Failed to retrieve anime list on page {page}.", False)
    log_info(f"test_another_page_default_list completed.")

def test_search_anime_url_by_query():
    query = "Tokyo Ghoul"
    log_info(f"Searching for anime with query: {query}")
    _parser = parser.JutsuParser("../web-cache/jutsu_parser_cache")
    log_info("Created web cache")
    anime_url = _parser.get_anime_link_by_query(query)
    if anime_url:
        log_info(f"Found anime URL for {query}: {anime_url}")
    else:
        log_info(f"Results not found.", False)
def test_random_technique():
    _parser = parser.JutsuParser("../web-cache/jutsu_parser_cache")
    log_info("Created web cache")
    technique = _parser.get_random_technique()
    if technique:
        log_info(f"Random technique dict: {technique}")
    else:
        log_info("Failed to retrieve random technique.", False)
    log_info("test_random_technique completed.")
async def test_async_default_anime_list():
    _parser = parser.Nurparse()
    log_info("Creating anime list (in async mode)")
    anime_list = await _parser.get_async_default_anime_list()
    print(anime_list) if anime_list else log_info("Failed to retrieve in async")
    log_info("test_async_default_anime_list completed.")
async def test_async_another_page_default_list():
    page = randint(3, 10)
    log_info(f"Page #{page} (in async mode)")
    _parser = parser.Nurparse()
    anime_list = await _parser.get_async_default_anime_list(page)
    print(anime_list) if anime_list else log_info(f"Failed to retrieve on page {page} in async", False)
    log_info("test_async_another_page_default_list completed.")
async def test_async_search_anime_url_by_query():
    query = "Tokyo Ghoul"
    log_info(f"Searching for anime with query: {query} (in async mode)")
    _parser = parser.Nurparse()
    anime_url = await _parser.get_async_anime_link_by_query(query)
    print(anime_url) if anime_url else log_info(f"Results not found.", False)
    log_info("test_async_search_anime_url_by_query completed.")
async def test_async_random_technique():
    _parser = parser.Nurparse()
    log_info("Creating random technique (in async mode)")
    technique = await _parser.get_async_random_technique()
    print(technique) if technique else log_info("Failed to retrieve in async", False)
    log_info("test_async_random_technique completed.")

def test_get_video_link_sync():
    _tv = parser.JutsuTV()
    href = "/tokushu/season-1/episode-1.html"
    video_link = _tv.get_video_link_sync(href)
    print(f"Video link: {video_link} with href: {href}")
if __name__ == "__main__":
    test_default_anime_list()
    test_raw_anime_list()
    test_another_page_default_list()
    test_search_anime_url_by_query()
    test_random_technique()
    run(test_async_default_anime_list())
    run(test_async_another_page_default_list())
    run(test_async_search_anime_url_by_query())
    run(test_async_random_technique())
    test_get_video_link_sync()
    # Test other methods by yourself