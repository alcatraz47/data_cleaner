import os
import re
import spacy
import numpy as np
import pandas as pd

def keep_alphanumeric(sentence: str) -> list:
    """cleaning text by extracting alphabets and
    then splitting into word list for each sentence

    Args:
        sentence (str): sentence string

    Returns:
        list: list of words.
    """
    pattern = re.compile(r"[A-Za-z]+")
    return re.findall(pattern=pattern, string=sentence)

def change_case(word_list: list, case: str="lower") -> list:
    """case changing of all contents in each list
    of words

    Args:
        word_list (list): list of words with alphabets only texts

    Returns:
        word_list (list): list of words with lowercase transformation
    """
    temp_list = []
    for i, word in enumerate(word_list):
        if case=="lower":
            temp_list.append(word.lower())
        else:
            temp_list.append(word.upper())
    word_list = temp_list[:]
    return word_list

def remove_stopwords(list_of_words: list) -> list:
    """removing stop words from list of words by matching
    English stop words and extracting those out

    Args:
        list_of_words (list): list of words with stop words

    Returns:
        list: stop word free list of words
    """
    stopword_list = stopwords.words("english")

    return [word for word in list_of_words if word not in stopword_list]

def extract_word_lemma(list_of_words: list) -> list:
    """lemmatization of words from list of words
    using NLTK WordNetLemmatizer class

    Args:
        list_of_list_words (list): list of words inside a list

    Returns:
        list: lemmatized list of list of words
    """
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in list_of_words]

def clean_text() -> pd.DataFrame: