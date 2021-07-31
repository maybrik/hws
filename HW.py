import re


def parse(query: str):
    text = query
    res = {}
    text_prep = text.split('/')[-1]
    text_fin = ''.join(text_prep)
    pattern_key = r'(\w+)='
    pattern_value = r'=(\w+)'
    key = re.findall(pattern_key, text_fin)
    value = re.findall(pattern_value, text_fin)
    for item1, item2 in zip(key, value):
        res.update({item1: item2})
    print(res)

if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}

    assert parse('http://test.com/=ferret') == {}
    assert parse('https://test.com/some_path/path_2?name=Dima') == {'name': 'Dima'}
    assert parse('http://skate.com/compet&???&?skate=karla&owner=kaoru') == {'skate': 'karla', 'owner': 'kaoru'}
    assert parse('https://score_skale?compet=football&%&??&game=over') == {'compet': 'football', 'game': 'over'}
    assert parse('http://skate.com/compet&???&?skate===karla&owner===kaoru') == {'skate': 'karla', 'owner': 'kaoru'}
    assert parse('htttp:/test.com?/?=') == {}
    assert parse('http://test.com/==?==&?') == {}
    assert parse('http://test7.com/777&7&?777&=7=7') == {'7': '7'}
    assert parse('http://test.com/?/?=exit') == {}
    assert parse('http://skate.com/race?track====??&difficulty===unexpected') == {{'track': 'unexpected'}}