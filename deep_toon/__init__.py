"""
Deep-TOON: Deep Token-Oriented Object Notation

Lightweight JSON compression for LLM applications.

Example:
    >>> from deep_toon import encode, decode
    >>> data = {"users": [{"name": "Alice", "age": 30}]}
    >>> compressed = encode(data)
    >>> original = decode(compressed)
"""

__version__ = "0.2.0"

from .encoder import DeepToonEncoder
from .decoder import DeepToonDecoder, DeepToonDecodeError

# Simple API
def encode(data, delimiter=","):
    """Encode data to Deep-TOON format."""
    return DeepToonEncoder(delimiter).encode(data)

def decode(deep_toon_str):
    """Decode Deep-TOON format to Python objects."""
    return DeepToonDecoder().decode(deep_toon_str)

def smart_encode(data, threshold=0.1, token_counter=None):
    """Smartly encode data to Deep-TOON only if it achieves significant savings."""
    return DeepToonEncoder().smart_encode(data, threshold, token_counter)

__all__ = ['DeepToonEncoder', 'DeepToonDecoder', 'DeepToonDecodeError', 'encode', 'decode', 'smart_encode']