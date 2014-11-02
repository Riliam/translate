Translator
====

Script for translate words or phrases from command line.
Uses yandex translate API.

Use:

1. [Get](https://tech.yandex.ru/keys/get/?service=trnsl) your Yandex Translate app key and store it in environment variable YANDEX_TRANSLATE_KEY. For example:
   `export YANDEX_TRANSLATE_KEY=23hjfoiasuh293rawiefoaiwu3hrhpa9wefh`

2. Put link to translate.py file into folder in PATH. For example (if ~/bin in your PATH):
   `ln -s translate.py ~/bin/t`

3. Use translator, for exapmle: 
   `t monkey` or `t monkey --all-lang` or `t monkey 'en-de'`

TODO: try optparse
