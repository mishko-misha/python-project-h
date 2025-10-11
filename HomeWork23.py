def popular_words(text: str, words: list[str]) -> dict[str, int]:
    """
    :param text: put text
    :param words: search for words in a text
    :return: dict {key:str value:int}
    """
    text = text.lower()
    result = {}
    for word in words:
        result[word.lower()] = text.split().count(word)
    return result


# assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
#                      ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
