## Installation

IF you don't need to fetch documents and only need to process Google Doc [JSON format](https://developers.google.com/docs/api/concepts/structure): `pip install gdocs`. This assumes documents have been fetched via some other means.

To be able to fetch Google Docs via OAuth2: `pip install gdocs[auth]`

## Usage

### Processing document content

If you have a local copy of document data:

```python
from gdocs import Doc

raw_data = {
    "title": "My document",
    "body": {
        "content": [
            {
                "startIndex": 1,
                "endIndex": 14,
                "paragraph": {
                    "elements": [
                        {
                            "startIndex": 1,
                            "endIndex": 14,
                            "textRun": {
                                "content": "Hello world!\n",
                                "textStyle": {
                                    "bold": True
                                }
                            }
                        }
                    ]
                }
            }
        ]
    },
    "documentId": "1cYJi..."
}

doc = Doc(raw_data)

# Iterating over document:
for chunk, style in doc:
    print chunk    # Hello world\n
    print style    # {'bold': True}

# Converting document to text
print(doc.text)    # Hello world\n

# Getting word count:
print(doc.word_count) # 2
```

### Fetching documents from Google Docs

NOTE: to fetch documents from Google, gdocs must be installed with `auth` extra: `pip install gdocs[auth]`.

Without token persistence:

```python
from gdocs import Loader
secrets = {
    # JSON credential file from Google
}
loader = Loader(secrets)
doc = loader.get_doc('some-doc-id') # Always triggers authentication
```

With custom token persistence:

```python
from gdocs import Loader
from somewhere import get_gdocs_credentials

def save_token(token:str):
    # save token to a db or file or whatever
    ...

secret, token = get_gdocs_credentials()

loader = Loader(secrets, token, on_new_token=save_token)
doc = loader.get_doc('some-doc-id') # If a valid token is present, no auth is required
```

With file-based token persistence (new token saved into a JSON file):
```python
from gdocs import Loader
loader = Loader.from_json_files('/path/to/secret.json', '/path/to/token.json')
doc = loader.get_doc('some-doc-id') # If a valid token is present, no auth is required.
```
