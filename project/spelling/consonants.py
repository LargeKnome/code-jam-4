search = {
    "M": ["chm", "gm", "lm", "tm", "m", "mm", "mb", "mbe", "me", "mh", "mme",
          "mn"],

    "N": ["cn", "dn", "gn", "gne", "kn", "ln", "mn", "mp", "pn", "sne", "n",
          "nn", "nd", "ne", "ng", "nh", "nne", "nt"],

    "NG": ["ng", "n", "nc", "nd", "ngh", "ngue"],

    "P": ["gh", "p", "pp", "pe", "ph", "ppe"],

    "B": ["pb", "b", "bb", "be", "bh"],

    "T": ["ght", "bt", "cht", "ct", "d", "ed", "pt", "t", "tt", "te", "th",
          "tte", "tw"],

    "D": ["ed", "ld", "t", "d", "dd", "de", "dh"],

    "K": ["c", "cc", "cch", "ch", "ck", "cq", "cqu", "cque", "cu", "lk", "q",
          "qu", "que", "x", "k", "ke", "kh", "kk"],

    "G": ["ckg", "g", "gg", "gge", "gh", "gu", "gue"],

    "S": ["c", "cc", "ce", "ps", "ts", "tsw", "tz", "z", "s", "ss", "sc",
          "sce", "se", "sse", "st", "sth", "sw"],

    "Z": ["s", "cz", "sc", "se", "sp", "ss", "sth", "ts", "tz", "x", "z", "zz",
          "ze"],

    "SH": ["sh", "sch", "ti", "ch", "c", "ce", "che", "chi", "chsi", "ci", "s",
           "sc", "sci", "she", "shi", "si", "ss", "ssi"],

    "ZH": ["g", "ge", "j", "s", "si", "ti", "z", "zh", "zi"],

    "F": ["lf", "phe", "pph", "f", "ph", "ff", "fe", "ffe", "gh", "v", "ve"],

    "V": ["lve", "v", "vv", "f", "ph", "ve", "w"],

    "TH": ["chth", "phth", "tth", "th", "the"],

    "DH": ["th", "the"],

    "Y": ["y", "i", "j", "ll", "r"],

    "HH": ["wh", "ch", "h", "j", "x"],

    "R": ["wr", "r", "rr", "l", "re", "rh", "rre", "rrh", "rt"],

    "L": ["l", "ll", "le", "lh", "lle"],

    "W": ["w", "ww", "ou", "u", "o", "we", "wh"],

    "CH": ["tch", "t", "tche", "te", "th", "ti", "ts", "tsch", "tsh", "tz",
           "tzs", "tzsch", "ch", "c", "cc", "che", "chi", "cz"],

    "JH": ["ch", "d", "dg", "dge", "di", "dj", "g", "j", "ge", "gg", "gi",
           "jj", "t"],

    "KS": ["x", "cks", "lks", "ks", "xx", "cast", "cc", "chs", "cques", "cs",
           "cz", "kes", "ques", "xc", "xe", "xs", "xsc", "xsw"],

    "KW": ["cqu", "qu"]
}

replace_start = {
    'B': {'b': 7287, 'be': 1538, 'bh': 15},

    'S': {'s': 9409, 'se': 1190, 'c': 370, 'ce': 279, 'ps': 53, 'sc': 45,
          'sce': 12, 'sw': 7, 'ss': 1, 'ts': 1},

    'K': {'c': 7032, 'k': 2933, 'ke': 604, 'cu': 364, 'ch': 231, 'kh': 40,
          'q': 15, 'qu': 12, 'que': 1},

    'CH': {'ch': 548, 'che': 241, 'chi': 215, 'c': 130, 'cz': 18, 'tsch': 6,
           't': 4, 'te': 3, 'tch': 1, 'ts': 1},

    'SH': {'sh': 816, 'sch': 694, 'she': 265, 'shi': 225, 's': 192, 'ch': 91,
           'che': 27, 'chi': 9, 'sci': 5, 'ci': 1, 'si': 1},

    'HH': {'h': 5773, 'wh': 36, 'j': 11, 'ch': 2},

    'Z': {'z': 626, 'ze': 200, 'x': 46, 'cz': 4},

    'D': {'d': 4464, 'de': 2355, 'ed': 153, 'dh': 14, 't': 3},

    'JH': {'j': 1326, 'ge': 374, 'gi': 197, 'g': 52, 'd': 13, 'dj': 4, 't': 2},

    'F': {'f': 4092, 'fe': 590, 'ph': 276, 'phe': 29},

    'G': {'g': 4023, 'gu': 445, 'gh': 51, 'gue': 50},

    'ZH': {'j': 28, 'ge': 15, 'g': 15, 'zh': 8, 'z': 4, 'si': 1, 'zi': 1},

    'N': {'n': 1994, 'ne': 753, 'kn': 208, 'gn': 27, 'pn': 6, 'mn': 2,
          'gne': 1, 'ng': 1},

    'Y': {'y': 642, 'j': 131, 'i': 4},

    'L': {'l': 4036, 'le': 1102, 'll': 14, 'lh': 3},

    'M': {'m': 7436, 'me': 1141, 'mm': 1}, 'NG': {'ng': 2},

    'W': {'w': 2435, 'we': 774, 'wh': 338, 'o': 15, 'ou': 5, 'u': 4},

    'P': {'p': 5724, 'pe': 1205},

    'T': {'t': 3633, 'te': 801, 'th': 28, 'pt': 8, 'tw': 6},

    'KW': {'qu': 378}, 'R': {'r': 3740, 're': 2571, 'wr': 120, 'rh': 100},

    'TH': {'th': 467, 'the': 123},

    'DH': {'the': 34, 'th': 22},

    'V': {'v': 1672, 've': 480, 'w': 52},

    'KS': {'x': 9, 'xe': 1, 'xs': 1}
}

replace_middle = {
    'B': {'b': 7235, 'be': 2119, 'bb': 474, 'pb': 7, 'bh': 7},

    'K': {'c': 7507, 'k': 3617, 'ck': 1871, 'ke': 1454, 'ch': 1112, 'cc': 547,
          'cu': 349, 'lk': 81, 'que': 61, 'cch': 59, 'kk': 54, 'qu': 34,
          'kh': 25, 'q': 12, 'cque': 10, 'cqu': 2},

    'N': {'n': 31628, 'ne': 3955, 'nn': 748, 'nne': 488, 'kn': 80, 'gn': 72,
          'ln': 34, 'gne': 21, 'nh': 19, 'nd': 9, 'pn': 5, 'nt': 3, 'dn': 3,
          'mp': 2, 'ng': 1},

    'L': {'l': 22397, 'le': 5217, 'll': 3779, 'lle': 934, 'lh': 12},

    'S': {'s': 14531, 'se': 1606, 'c': 1318, 'ss': 1304, 'ce': 1249,
          'sse': 550, 'z': 248, 'st': 116, 'sce': 94, 'sc': 81, 'ts': 22,
          'sw': 10, 'cc': 1, 'sth': 1, 'ps': 1},

    'M': {'m': 11571, 'me': 2458, 'mm': 515, 'mme': 320, 'lm': 155,
          'chm': 102, 'mb': 67, 'gm': 45, 'tm': 41, 'mbe': 15, 'mn': 10,
          'mh': 2},

    'T': {'t': 22200, 'te': 5279, 'tt': 1174, 'tte': 605, 'ght': 378, 'd': 208,
          'bt': 29, 'th': 23, 'cht': 10, 'ct': 8, 'pt': 5},

    'R': {'r': 26657, 're': 4433, 'rr': 1173, 'rre': 292, 'wr': 90, 'l': 69,
          'rt': 6, 'rh': 4, 'rrh': 1},

    'D': {'d': 9038, 'de': 3089, 'ed': 1684, 'dd': 442, 't': 107, 'ld': 25,
          'dh': 20},

    'V': {'v': 3685, 've': 2715, 'w': 96, 'vv': 8, 'ph': 6, 'f': 2},

    'SH': {'ti': 1747, 'sh': 702, 'shi': 393, 'she': 392, 'ci': 281, 's': 205,
           'sch': 187, 'ssi': 151, 'che': 75, 'si': 57, 'ch': 48, 'ss': 41,
           'ce': 25, 'chi': 24, 'sci': 6, 'c': 5, 'sc': 3},

    'HH': {'h': 2297, 'ch': 40, 'wh': 18, 'j': 13, 'x': 1},

    'Z': {'s': 2704, 'z': 1724, 'se': 781, 'ze': 623, 'zz': 192, 'ss': 24,
          'x': 6, 'sth': 2, 'sc': 1},

    'F': {'f': 3606, 'fe': 729, 'ff': 635, 'ph': 563, 'ffe': 359, 'phe': 138,
          'gh': 57, 'lf': 41, 'v': 11, 'pph': 1},

    'TH': {'th': 1115, 'the': 310, 'tth': 11},

    'JH': {'ge': 970, 'gi': 720, 'j': 533, 'g': 289, 'dge': 169, 'd': 115,
           'dg': 89, 'dj': 51, 'gg': 33, 't': 8, 'di': 8, 'ch': 1},

    'G': {'g': 5728, 'gg': 394, 'gu': 248, 'gge': 122, 'gh': 88, 'gue': 87},

    'NG': {'n': 2202, 'ng': 1477, 'nc': 35, 'ngh': 11, 'ngue': 4, 'nd': 2},

    'Y': {'i': 579, 'y': 329, 'r': 138, 'j': 118, 'll': 3},

    'P': {'p': 6606, 'pe': 1765, 'pp': 631, 'ppe': 426, 'ph': 18, 'gh': 3},

    'CH': {'ch': 492, 't': 490, 'che': 370, 'c': 349, 'chi': 205, 'tche': 191,
           'cc': 147, 'tch': 128, 'ti': 106, 'cz': 90, 'tsch': 27, 'tsh': 19,
           'te': 13, 'ts': 7, 'th': 2, 'tzs': 1, 'tzsch': 1},

    'W': {'w': 1945, 'we': 515, 'u': 402, 'o': 196, 'wh': 43, 'ou': 26},

    'ZH': {'si': 205, 's': 82, 'ge': 29, 'j': 24, 'g': 12, 'z': 8, 'zh': 4,
           'zi': 3, 'ti': 2},

    'KS': {'x': 1062, 'xe': 139, 'ks': 127, 'cks': 108, 'cc': 89, 'xc': 49,
           'cs': 37, 'chs': 31, 'xs': 26, 'kes': 24, 'xx': 4, 'lks': 4,
           'cz': 2, 'cques': 1},

    'DH': {'the': 319, 'th': 104},

    'KW': {'qu': 555, 'cqu': 64}
}

replace_end = {
    'G': {'g': 840, 'gg': 62, 'gue': 53, 'gh': 28, 'gge': 20, 'gu': 6},

    'N': {'n': 11812, 'ne': 1494, 'nn': 365, 'nne': 78, 'gn': 26, 'nh': 12,
          'gne': 6, 'nt': 3, 'ln': 2},

    'TH': {'th': 603, 'the': 16},

    'R': {'r': 969, 're': 685, 'rr': 54, 'rre': 30, 'rt': 1},

    'K': {'k': 1590, 'ck': 1151, 'c': 1148, 'ke': 541, 'ch': 393, 'que': 63,
          'lk': 36, 'q': 17, 'kh': 11, 'cq': 8, 'cque': 4, 'cu': 2, 'qu': 1,
          'kk': 1},

    'Z': {'s': 16349, 'z': 362, 'se': 338, 'ze': 311, 'zz': 11, 'ss': 1},

    'S': {'s': 5369, 'ss': 945, 'ce': 746, 'z': 481, 'se': 417, 'ts': 74,
          'sse': 67, 'ps': 26, 'c': 18, 'sce': 6, 'tz': 3},

    'B': {'b': 268, 'be': 118, 'bb': 28, 'bh': 1},

    'D': {'ed': 3901, 'd': 3079, 'de': 503, 'dd': 26, 'ld': 4, 'dh': 3},

    'NG': {'ng': 5048, 'ngue': 6, 'ngh': 3},

    'T': {'t': 5013, 'te': 1237, 'd': 896, 'tt': 644, 'tte': 298,
          'ght': 181, 'cht': 5, 'bt': 3, 'ct': 1, 'pt': 1},

    'L': {'l': 3343, 'le': 1875, 'll': 1355, 'lle': 338},

    'SH': {'sh': 453, 'sch': 147, 'shi': 51, 'che': 24, 'she': 7, 's': 1,
           'ss': 1, 'ce': 1, 'ch': 1, 'chi': 1},

    'KS': {'x': 403, 'ks': 263, 'cs': 244, 'cks': 180, 'kes': 126, 'chs': 21,
           'lks': 14, 'ques': 12, 'xe': 4, 'xx': 3},

    'M': {'m': 1895, 'me': 267, 'mm': 53, 'mb': 53, 'mme': 29, 'lm': 23,
          'mn': 7, 'mbe': 6, 'gm': 2},

    'V': {'ve': 580, 'v': 161, 'f': 2, 'w': 1},

    'P': {'p': 749, 'pe': 178, 'pp': 124, 'ppe': 29, 'gh': 1},

    'CH': {'ch': 333, 'tch': 105, 'cz': 55, 'chi': 46, 'che': 43, 'tsch': 39,
           'c': 8},

    'JH': {'ge': 399, 'dge': 160, 'gi': 15, 'j': 11, 'g': 5, 'jj': 1},

    'F': {'ff': 417, 'f': 329, 'ph': 63, 'fe': 57, 'ffe': 32, 'gh': 14, 'v': 8,
          'phe': 4, 'lf': 4},

    'ZH': {'ge': 17, 'j': 3},

    'HH': {'ch': 16, 'h': 1},

    'DH': {'the': 40, 'th': 2},

    'Y': {'r': 8, 'y': 8, 'i': 2},

    'W': {'we': 7}
}
