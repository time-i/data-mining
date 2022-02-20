# Chap07/blogs_entities.py
from argparse import ArgumentParser

import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.chunk import ne_chunk
import wikipedia

def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--entity', default='London')
    return parser


def get_noun_phrases(pos_tagged_tokens):
    all_nouns = []
    previous_pos = None
    current_chunk = []
    for (token, pos) in pos_tagged_tokens:
        if pos.startswith('NN'):
            if pos == previous_pos:
                current_chunk.append(token)
            else:
                if current_chunk:
                    all_nouns.append((' '.join(current_chunk), previous_pos))
                current_chunk = [token]
        else:
            if current_chunk:
                all_nouns.append((' '.join(current_chunk), previous_pos))
            current_chunk = []
        previous_pos = pos
    if current_chunk:
        all_nouns.append((' '.join(current_chunk), pos))
    return all_nouns


def get_entities(tree, entity_type):
    for ne in tree.subtrees():
        if ne.label() == entity_type:
            tokens = [t[0] for t in ne.leaves()]
            yield ' '.join(tokens)

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    entity = 'China do a good job in the Space and it is in the west of the Japan.' \
             'Chinese people are  kind.' \

    tokens = word_tokenize(entity)
    tagged_tokens = pos_tag(tokens)
    chunks = ne_chunk(tagged_tokens, binary=True)

    print("-----")
    print("Description of China")
    print(entity)
    print("-----")
    print("Noun phrases in description:")
    for noun in get_noun_phrases(tagged_tokens):
        print(noun[0])  # tuple (noun, pos_tag)
    print("-----")
    print("Named entities in description:")
    for ne in get_entities(chunks,entity_type='NE'):
        print(ne)
