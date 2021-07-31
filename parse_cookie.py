import re


def parse_cookie(query: str):
    text = query
    res = {}
    pattern_key = r'(\w+)*;?='
    pattern_value = r'=(\w+\S);'
    #pattern_key = r'(\w+)*;?='
    #pattern_value = r'=(\w+(?=\w+)\S?);'
    #в паттерне значения ошибка, которая не проходит четвертый тест с дополнительным =
    key = re.findall(pattern_key, text)
    value = re.findall(pattern_value, text)
    for item1, item2 in zip(key, value):
         res.update({item1: item2})
    print(res)

if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}

    assert parse_cookie('un@ex%^pec*ted_n@me??') == {}
    assert parse_cookie('status=reluctant_hero;universe=AoT;') == {'status': 'reluctant_hero', 'universe': 'AoT'}
    assert parse_cookie('universe=aot;spoiler=all_dead') == {{'universe': 'aot'}}
    assert parse_cookie('??=??') == {}
    assert parse_cookie('??=??;') == {}
    assert parse_cookie('art1st=halestorm;_none??') == {{'art1st': 'halestorm'}}
    assert parse_cookie('timec0de:kiev=1115') == {}
    assert parse_cookie('timecode:kiev=1116;') == {'kiev': '1116'}
    assert parse_cookie('=;') == {}
    assert parse_cookie(':;;name=anon&name=kojiro;') == {'name': 'kojiro'}