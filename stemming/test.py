from porter import get_m

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


print('All tests passed')
