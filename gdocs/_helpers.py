def _paragraph(paragraph:dict):
    # generator function for processing paragraphs
    for element in paragraph.get('elements', []):
        text_run = element.get('textRun', {})
        if 'content' in text_run:
            yield text_run['content'], text_run.get('textStyle', {})


def _table(table:dict):
    # recursive generator function for processing tables
    for row in table.get('tableRows', []):
        for cell in row.get('tableCells', []):
            for content in cell.get('content', []):
                if 'paragraph' in content:
                    for x in _paragraph(content['paragraph']):
                        yield x
                elif 'table' in content:
                    for x in _table(content['table']):
                        yield x
