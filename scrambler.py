import argparse
import string
import re
import random

import nltk
from nltk.corpus import stopwords


def main(word_list, min_line_length=2, max_line_length=12):
    word_list = random.sample(word_list, len(word_list))
    all_lines = []
    while len(word_list) > 0:
        x, y = make_line(word_list, min_line_length, max_line_length)
        all_lines.append(x)
        word_list = y
    return '\n'.join(all_lines)


def make_line(word_list, min_line_length=2, max_line_length=12):
    line_length = random.randint(min_line_length, max_line_length)
    cur_line = ' '.join(word_list[:line_length])
    return cur_line, word_list[line_length:]
        

def format_text(text, keep_stopwords=False):
    text = text.replace('“','"').replace('”','"').replace('’', "'").replace('‘', "'")
    text = text.replace('—', '-').replace('…', '...')
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.replace('\n', ' ')
    text = re.sub(' +', ' ', text)
    if not keep_stopwords:
        text = ' '.join([w for w in text.split(' ') if w.lower() not in stopwords.words('english')])
    return text


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scramble up text into a poem')
    parser.add_argument('filename', help='enter the file with the text')
    parser.add_argument('--min', type=int, help='fewest words you want in a line')
    parser.add_argument('--max', type=int, help='most words you want in a line')
    parser.add_argument('--stop', action='store_const', const='stop')
    args = parser.parse_args()
    with open(args.filename) as f:
        text = f.read()
    if args.stop:
        formatted = format_text(text)
    else:
        formatted = format_text(text, keep_stopwords=True)
    word_list = formatted.split(' ')
    print(main(word_list, min_line_length=args.min, max_line_length=args.max))