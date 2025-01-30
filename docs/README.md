# How to use

- Import this package to your project<br />
  Use
  ```py
  import sys
  sys.path.append("here path with jutsu_parser folder")
  ```
  to import the package.<br />
  (Publishing on PyPI coming soon, won't promise that)

# Classes and functions

**JutsuParser (Sync) and Nurparse (Async)** classes for parsing the content

- get\_(async)\_default_anime_list() returns a list of dictionaries (the anime list on the main page)

  - The dictionary structure:
    - **@id**
      - Fake anime's ID for displaying the anime list in order
    - **title**
      - The title of the anime in Russian language
    - **image_url**
      - The anime image's url (default, size unknown)
    - **release_url**
      - The full link to the anime release (in format "https://jut.su/NAME")
    - **extra**
      - Additional information about the release (number of episodes, et cetera)
  - The params you can set:
    - **page**
      - Just the number of page you want to scrap
  - Example
    - <code>from jutsu_parser import parser
      parse_info = parser.JutsuParser("here is your path for web cache .sqlite file")
      \# **Without changing the page**
      print(parse_info.get_default_anime_list())
      \# **With new page**
      print(parse_info.get_default_anime_list(5))</code>

- get\_(async)\_anime_link_by_query() returns just the link to the release by query. If not found, returns **None**.

  - Link format
    - https://jut.su/NAME
  - The params you have to set:
    - **query**
      - The search query to search for the release

- get\_(async)\_random_technique() returns a dictionary of random technique
  - The dictionary structure:
    - **title**
      - The title of a technique
    - **url**
      - The URL of a technique's extra information
    - **image_url**
      - The bad-quality image URL of a technique (image is a frame from anime by default)

_(async) - optional, can only be used in the **Nurparse()** class as an asynchronous function_

**JutsuTV** class for downloading anime

- get_video_link\_(a)sync() returns a link to the player's video or **None** if the video is not available
  - Params:
    - **anime_url_or_href**
      - Anime Link (like _https://jut.su/NAME/season-1/episode-1.html_) or href (like _/NAME/season-1/episode-1.html_). You need to specify season and episode. Anime path may contain no season number (like _https://jut.su/toradora/episode-1.html_)
- download_video\_(a)sync() returns **True** if success and **False** if fail
  - Params:
    - video_url
      - Full path to the MP4 file from the original jut.su player (Take this from previous function)
    - save_path
      - Internal URI path where to save the video
    - proxy
      - Link to your proxy if you need it (the player may not work on various IPs)
