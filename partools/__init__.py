from .parmap import map 
from .pandas_util import groupby_apply, series_apply

__all__ = ['map', 'groupby_apply', 'series_apply']

__version__ = '0.1.1'

def _readme():
    from os import path
    from codecs import open
    here = path.dirname(path.abspath(path.dirname(__file__)))
    with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        return f.read()

# __doc__ = _readme()
