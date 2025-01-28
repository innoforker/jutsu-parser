# Jut.su Web Parser

**Description**  
_jutsu_parser_ allows you to use features of the russian anime website [jut.su](https://jut.su) in your Python projects. **Parse animes from the main page, search them and you even can get random techniques from the site!**<br /><br />
**Docs**  
[Read the documentation](https://github.com/innoforker/jutsu-parser/blob/main/docs/README.md)

# FAQ

**Q: — What is "Fast Mode" in parser.py file?**  
**A: — Fast Mode is the use of *requests* module instead of _requests-cache_ module. Because _requests-cache_ stores the parsing result for a long time, it _will not be useful_ for the get_random_technique() function. The parser automatically enables Fast Mode when you use this function in your code.**<br /><br />
**Q: — Will the parser create the session's web cache .sqlite file at the path which I specified if I just use get_random_technique() function?**
**A: No. You can simply specify an empty string when creating the class prototype and use this function, since it uses a regular module and not one intended for long-term caching.**<br /><br />
For example:  
```py
from jutsu_parser import parser
_parser = parser.JutsuParser("")
technique = _parser.get_random_technique()
print(technique["title"]) # Returning the title of random technique
```
