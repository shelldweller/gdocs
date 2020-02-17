from ._helpers import _paragraph, _table


class Doc:
    def __init__(self, doc:dict):
        self._doc = doc


    @property
    def text(self) -> str:
        return ''.join([text for text,_ in self])


    @property
    def word_count(self) -> int:
        count = 0
        for chunk in self:
            count += len(chunk[0].split())
        return count


    def __iter__(self):
        # Doc content structure: https://developers.google.com/docs/api/concepts/structure
        for item in self._doc['body']['content']:
            if 'paragraph' in item:
                for text, formatting in _paragraph(item['paragraph']):
                    yield text, formatting
            if 'table' in item:
                for text, formatting in _table(item['table']):
                    yield text, formatting
