# Jut.su Web Parser

**Description**<br />
_jutsu_parser_ allows you to use features of the russian anime website [jut.su](https://jut.su) in your Python projects. **Parse animes from the main page, search them and you even can get random techniques from the site!**<br /><br/>
**Docs**<br />
[Read the documentation](https://github.com/innoforker/jutsu-parser/blob/main/docs/README.md)

# FAQ

**Q: — What is "Fast Mode" in parser.py file?**
**A: — Fast Mode is the use of *requests* module instead of _requests-cache_ module. Because _requests-cache_ stores the parsing result for a long time, it _will not be useful_ for the get_random_technique() function. The parser automatically enables Fast Mode when you use this function in your code.**
