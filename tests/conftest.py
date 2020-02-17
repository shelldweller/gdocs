import json
import os

import pytest

from gdocs import Doc


DOC_ROOT = os.path.join(
    os.path.dirname(__file__),
    'samples'
)

CREDENTIALS_ROOT = os.path.join(
    os.path.dirname(__file__),
    'credentials'
)

@pytest.fixture
def raw_doc_from_file():
    def _raw_doc_from_file(name):
        path = os.path.join(DOC_ROOT, name)
        with open(path) as f:
            return json.load(f)
    return _raw_doc_from_file


@pytest.fixture
def doc_from_file(raw_doc_from_file):
    return lambda name: Doc(raw_doc_from_file(name))


@pytest.fixture
def secret_file():
    return os.path.join(CREDENTIALS_ROOT, 'secret.json')


@pytest.fixture
def token_file():
    return os.path.join(CREDENTIALS_ROOT, 'token.json')
