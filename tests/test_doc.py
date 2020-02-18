def test_text(doc_from_file):
    text = doc_from_file('doc.json').text
    assert 'Can I \nhaz\nnested\ntables?' in text # from nested tables
    assert 'I like colours' in text # text across formatted content chunks


def test_word_count(doc_from_file):
    # In word-format.json formatting is applied at character level
    doc = doc_from_file('word-format.json')
    assert doc.text == 'Discerning deipnosophist\n'
    assert doc.word_count == 2


def test_iterator(doc_from_file):
    doc = doc_from_file('doc.json')
    for text, formatting in doc:
        assert type(text) is str
        assert type(formatting) is dict
        assert text # text should never be empty
