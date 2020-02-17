import os

import pytest

from gdocs import Loader, Doc


def test_loader(secret_file, token_file, raw_doc_from_file):
    if not os.path.exists(secret_file):
        pytest.skip('Secret file does not exist. Add %s to run this test.' % secret_file)

    # NOTE: if token file does not exist, user will be prompted to go through the whole OAuth setup.

    raw_doc = raw_doc_from_file('doc.json')
    loader = Loader.from_json_files(secret_file, token_file)
    doc = loader.get_doc(raw_doc['documentId'])

    assert isinstance(doc, Doc)
    assert os.path.exists(token_file)
