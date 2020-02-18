import os.path

from .doc import Doc
from .loader import Loader

with open(os.path.join(os.path.dirname(__file__), 'VERSION')) as f:
    __version__ = f.read().strip()
