def test_text(doc_from_file):
    text = doc_from_file('doc.json').text
    assert 'Can I \nhaz\nnested\ntables?' in text # from nested tables
    assert 'I like colours' in text # text across formatted content chunks


def test_word_count(doc_from_file):
    assert doc_from_file('doc.json').word_count > 0


def test_iterator(doc_from_file):
    doc = doc_from_file('doc.json')
    for text, formatting in doc:
        assert type(text) is str
        assert type(formatting) is dict
        assert text # text should never be empty
