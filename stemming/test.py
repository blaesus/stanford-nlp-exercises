from porter import get_m, stem

print('\n~ get_m ~')

get_m_test_data = {
    0: ['TR', 'EE', 'TREE', 'Y', 'BY'],
    1: ['TROUBLE', 'OATS', 'TREES', 'IVY'],
    2: ['TROUBLES', 'PRIVATE', 'OATEN', 'ORRERY'],
}

for m_correct in get_m_test_data:
    for word in get_m_test_data[m_correct]:
        m_calculated = get_m(word.lower())
        print('testing', word, '-', 'comparing', m_correct, 'and', m_calculated)
        assert m_correct == m_calculated


print('\n~ stem ~')

stem_test_data = {
    # 'caresses': 'caress',
    # 'ponies': 'poni',
    # 'ties': 'ti',
    # 'caress': 'caress',
    # 'cats': 'cat',

    'feed': 'feed',
    'agreed': 'agree',
    # 'plastered': 'plaster',
    # 'bled': 'bled',
    # 'motoring': 'motor',
    # 'sing': 'sing',
}

for full_form in stem_test_data:
    stemmed_form_correct = stem_test_data[full_form]
    stemmed_form_calculated = stem(full_form)
    print('testing', full_form, '-',
          'expecting', "'" + stemmed_form_correct + "',",
          'got', "'" + stemmed_form_calculated + "'")
    assert stemmed_form_correct == stemmed_form_calculated

print('All tests passed')
