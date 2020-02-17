import json
import os

import pytest

from gdocs import Doc


DOC_ROOT = os.path.join(
    os.path.dirname(__file__),
    'samples'
)

@pytest.fixture
def doc_from_file():
    def _doc_from_file(name):
        path = os.path.join(DOC_ROOT, name)
        with open(path) as f:
            return Doc(json.load(f))
    return _doc_from_file
