#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import requests
import os
import os.path


KEY = os.environ.get("YANDEX_TRANSLATE_KEY")


description = """
    Usage `{command} <text> [<lang>|<lang_from-lang_to>]`
    For example: {command} 'I love monkyes' 'en-ru'
    >>>Я люблю обезьянок

    The default pair is 'en-ru' or 'ru-en' depending on
    language of input phrase.
    So:
    `{command} monkey` -> обезьяна
    `{command} обезьянка` -> monkey

    If <lang> provided instead of <lang_from-lang_to> assume
    <lang> is target language:
    `{command} обезьяна de` -> Affe

    flag `--all-lang` force translation into all languages
    supported by yandex translator
"""

def directions_query(key=KEY):
    base_url = u'https://translate.yandex.net/api/v1.5/tr.json/getLangs?key={}'
    query = base_url.format(key)
    return query


def translate_query(text, direction=u'en-ru', key=KEY):
    base_url = u'https://translate.yandex.net/api/v1.5/tr.json/translate?' +\
        'key={}&text={}&lang={}'
    query = base_url.format(key, text, direction)
    return query


def check_lang_query(text, key=KEY):
    base_url = 'https://translate.yandex.net/api/v1.5/tr.json/detect?' +\
        'key={}&text={}'
    query = base_url.format(key, text)
    return query


def directions():
    q = directions_query()
    r = requests.get(q)
    return r.json()['dirs']


def check_lang(text):
    q = check_lang_query(text)
    r = requests.get(q)
    return r.json()['lang']


def translate(text, direction='en-ru'):
    q = translate_query(text, direction)
    r = requests.get(q)
    return r.json()["text"][0]


if __name__ == '__main__':
    command = os.path.basename(sys.argv[0])
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print(description.format(command=command))

    elif len(sys.argv) == 2:
        if check_lang(sys.argv[1]) == 'ru':
            direction = 'ru-en'
        elif check_lang(sys.argv[1]) == 'en':
            direction = 'en-ru'
        translation = translate((sys.argv[1]).decode('utf-8'), direction)
        print('\n\t' + translation + '\n')
    elif len(sys.argv) == 3:
        if sys.argv[2] == '--all-lang':
            lang = check_lang(sys.argv[1])
            dirs = [d for d in directions() if d.startswith(lang)]
            print('\n')
            for d in dirs:
                trans = translate(sys.argv[1].decode('utf-8'), d)
                print('\t' + d[3:] + ': ' + trans)
            print('\n')
        else:
            print('\n\t' + translate((sys.argv[1]).decode('utf-8') + '\n', sys.argv[2]))
