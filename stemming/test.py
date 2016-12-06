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


print('\n~ stem against official test data ~')

official_stem_test_data = {
    # 'caresses': 'caress',
    # 'ponies': 'poni',
    # 'ties': 'ti',
    # 'caress': 'caress',
    # 'cats': 'cat',
    #
    # 'feed': 'feed',
    # 'agreed': 'agree',
    # 'plastered': 'plaster',
    # 'bled': 'bled',
    # 'motoring': 'motor',
    # 'sing': 'sing',
    #
    # 'happy': 'happi',
    # 'sky': 'sky',
    #
    # 'relational': 'relate',
    # 'conditional': 'condition',
    # 'rational': 'rational',
    # 'valenci': 'valence',
    # 'hesitanci': 'hesitance',
    # 'digitizer': 'digitize',
    # 'conformabli': 'conformable',
    # 'radicalli': 'radical',
    # 'differentli': 'different',
    # 'vileli': 'vile',
    # 'analogousli': 'analogous',
    # 'vietnamization': 'vietnamize',
    # 'predication': 'predicate',
    # 'operator': 'operate',
    # 'feudalism': 'feudal',
    # 'decisiveness': 'decisive',
    # 'hopefulness': 'hopeful',
    # 'callousness': 'callous',
    # 'formaliti': 'formal',
    # 'sensitiviti': 'sensitive',
    # 'sensibiliti': 'sensible',
    #
    # 'triplicate': 'triplic',
    # 'formative': 'form',
    # 'formalize': 'formal',
    # 'electriciti': 'electric',
    # 'electrical': 'electric',
    # 'hopeful': 'hope',
    # 'goodness': 'good',

    'revival': 'reviv',
    'allowance': 'allow',
    'inference': 'infer',
    'airliner': 'airlin',
    'gyroscopic': 'gyroscop',
    'adjustable': 'adjust',
    'defensible': 'defens',
    'irritant': 'irrit',
    'replacement': 'replac',
    'adjustment': 'adjust',
    'dependent': 'depend',
    'adoption': 'adopt',
    'homologou': 'homolog',
    'communism': 'commun',
    'activate': 'activ',
    'angulariti': 'angular',
    'homologous': 'homolog',
    'effective': 'effect',
    'bowdlerize': 'bowdler',
    'fuckatmion': 'fuckatmion',
}

for full_form in official_stem_test_data:
    stemmed_form_correct = official_stem_test_data[full_form]
    stemmed_form_calculated = stem(full_form)
    print('testing', full_form, '-',
          'expecting', "'" + stemmed_form_correct + "',",
          'got', "'" + stemmed_form_calculated + "'")
    assert stemmed_form_correct == stemmed_form_calculated

print('All tests passed')
