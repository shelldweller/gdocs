## Installation

If document is fetched via some other means and you only need to work with Google Doc [JSON format](https://developers.google.com/docs/api/concepts/structure): `pip install gdocs`.

To be able to fetch Google Docs via OAuth2: `pip install gdocs[auth]`


## Usage

```python
from gdocs import Doc

gdoc_data = {
    'title': 'My document',
    'contents': []
}

doc = Doc(gdoc_data)
for text, _format in doc:
    print text

```
