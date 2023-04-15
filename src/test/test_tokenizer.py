from collections import Counter

from src.data import DATA_DIR
from src.pars_subtitle import Subtitle

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

def test_tokenizer():

    file_path = DATA_DIR / 'Game of Thrones _Winter is Coming_en.srt'
    obj = Subtitle(file_path)
    obj.tokenize()

    assert '.' ==  Counter(obj.words).most_common(10)[0][0]