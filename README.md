# Jut.su Web Parser
THE PROJECT IS CLOSED. THERE WON'T BE NEW COMMITS FROM ME, THE AUTHOR. Check [Sec Policy](SECURITY.md).
**Description**  
Jut.su Parser allows you to use features of the russian anime website [jut.su](https://jut.su) in your Python projects. **Parse animes from the main page, search them, download them and you can even get random techniques from the site!** [Know more about the security policy to prevent future troubles](SECURITY.md).<br /><br />
**Docs**  
[Read the documentation](docs/README.md)

# FAQ

**Q: — What is "Fast Mode" in parser.py file?**  
**A: — Fast Mode is the use of *requests* module instead of _requests-cache_ module. Because _requests-cache_ stores the parsing result for a long time, it _will not be useful_ for the get_random_technique() function. The parser automatically enables Fast Mode when you use this function in your code.** <br /><br />
**Q: — Will the parser create the session's web cache .sqlite file at the path which I specified if I just use get_random_technique() function?**  
**A: No. You can simply specify no args when creating the class prototype and use this function, since it uses a regular module and not one intended for long-term caching.**<br /><br />
For example:  
```py
from jutsu_parser import parser
_parser = parser.JutsuParser()
technique = _parser.get_random_technique()
print(technique["title"]) # Returning the title of random technique
```  
**Asynchronous usage**  
Just import the module and chill. Use Nurparse for asynchronous operations. And remember, **you don't need caching and web cache path when you're asynchronous.** Nurparse fully based on JutsuParser, but I don't recommend to use sync functions in class intended for async :3
```py
import asyncio
from jutsu_parser import parser
async def main():
    async_parser = parser.Nurparse() # Different class for async
    technique = await async_parser.get_async_random_technique()
    print(technique) # Raw printing
asyncio.run(main())
```  

# README in different languages
[🇷🇺 README Russian translation](README-ru.md)  
[🇷🇺 Docs Russian translation](docs/README-ru.md)  
[🇷🇺 Security Policy Russian translation](SECURITY-ru.md)  
