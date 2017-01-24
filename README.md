# bash_translate

This uses Yandex Translate API to commit translations.

You need to obtain a token from [this page](https://tech.yandex.com/translate/).

Then insert a token to `.ya_token` file as

```
my.yandex.translate.token
```

You can also copy a `.ya_token` to a home directory

and you can finally run it with

```bash
./translate.py fr Привет
```
