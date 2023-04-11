import pysrt
from loguru import logger
from nltk.tokenize import word_tokenize
from tqdm import tqdm


class Subtitle:
    def __init__(self, file_path):
        self.subtitle = pysrt.open(file_path)
        self.words = []

    def tokenize(self):
        logger.info('Tokenizing subtitle...')
        for sub in tqdm(self.subtitle):
            self.words.extend(word_tokenize(sub.text))


if __name__ == '__main__':

    from collections import Counter

    from data import DATA_DIR

    file_path = DATA_DIR /'Game of Thrones _Winter is Coming_en.srt'
    obj = Subtitle(file_path)
    obj.tokenize()
    print(Counter(obj.words).most_common(10))