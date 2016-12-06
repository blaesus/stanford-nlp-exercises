rule_sets = {
    # rule_set_name: [
    #   (m_lower_bound_exclusive,
    #    m_upper_bound_exclusive,
    #    ends_with_letters,
    #    stem_contains_vowel,
    #    ends_with_double_consonant,
    #    ends_with_cvc,
    #    search_string,
    #    replacement,
    #   ),
    #   ...
    # ]


    '1a': [
        (None, None, None, None, None, None, 'SSES', 'SS'),
        (None, None, None, None, None, None, 'IES',  'I'),
        (None, None, None, None, None, None, 'SS',   'SS'),
        (None, None, None, None, None, None, 'S',    ''),
    ],

    '1b': [
        (0,    None, None, None, None, None, 'EED', 'EE'),
        (None, None, None, True, None, None, 'ED',  ''),
        (None, None, None, True, None, None, 'ING', ''),
    ],

    '1c': [
        (None, None, None, True, None, None, 'Y', 'I'),
    ],

    '2': [
        (0,    None, None, None, None, None, 'ATIONAL', 'ATE'),
        (0,    None, None, None, None, None, 'TIONAL', 'TION'),
        (0,    None, None, None, None, None, 'ENCI', 'ENCE'),
        (0,    None, None, None, None, None, 'ANCI', 'ANCE'),
        (0,    None, None, None, None, None, 'IZER', 'IZE'),
        (0,    None, None, None, None, None, 'ABLI', 'ABLE'),
        (0,    None, None, None, None, None, 'ALLI', 'AL'),
        (0,    None, None, None, None, None, 'ENTLI', 'ENT'),
        (0,    None, None, None, None, None, 'ELI', 'E'),
        (0,    None, None, None, None, None, 'OUSLI', 'OUS'),
        (0,    None, None, None, None, None, 'IZATION', 'IZE'),
        (0,    None, None, None, None, None, 'ATION', 'ATE'),
        (0,    None, None, None, None, None, 'ATOR', 'ATE'),
        (0,    None, None, None, None, None, 'ALISM', 'AL'),
        (0,    None, None, None, None, None, 'IVENESS', 'IVE'),
        (0,    None, None, None, None, None, 'FULNESS', 'FUL'),
        (0,    None, None, None, None, None, 'OUSNESS', 'OUS'),
        (0,    None, None, None, None, None, 'ALITI', 'AL'),
        (0,    None, None, None, None, None, 'IVITI', 'IVE'),
        (0,    None, None, None, None, None, 'BILITI', 'BLE'),
    ],

    '3': [
        (0,    None, None, None, None, None, 'ICATE', 'IC'),
        (0,    None, None, None, None, None, 'ATIVE', ''),
        (0,    None, None, None, None, None, 'ALIZE', 'AL'),
        (0,    None, None, None, None, None, 'ICITI', 'IC'),
        (0,    None, None, None, None, None, 'ICAL', 'IC'),
        (0,    None, None, None, None, None, 'FUL', ''),
        (0,    None, None, None, None, None, 'NESS', ''),

    ],

    '4': [
        (1, None, None, None, None, None, 'AL', ''),
        (1, None, None, None, None, None, 'ANCE', ''),
        (1, None, None, None, None, None, 'ENCE', ''),
        (1, None, None, None, None, None, 'ER', ''),
        (1, None, None, None, None, None, 'IC', ''),
        (1, None, None, None, None, None, 'ABLE', ''),
        (1, None, None, None, None, None, 'IBLE', ''),
        (1, None, None, None, None, None, 'ANT', ''),
        (1, None, None, None, None, None, 'EMENT', ''),
        (1, None, None, None, None, None, 'MENT', ''),
        (1, None, None, None, None, None, 'ENT', ''),
        (1, None, ('S', 'T'), None, None, None, 'ION', ''),
        (1, None, None, None, None, None, 'OU', ''),
        (1, None, None, None, None, None, 'ISM', ''),
        (1, None, None, None, None, None, 'ATE', ''),
        (1, None, None, None, None, None, 'ITI', ''),
        (1, None, None, None, None, None, 'OUS', ''),
        (1, None, None, None, None, None, 'IVE', ''),
        (1, None, None, None, None, None, 'IZE', ''),
    ]
}

