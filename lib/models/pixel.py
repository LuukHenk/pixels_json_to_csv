"""Simplified pixel datamodel"""

from dataclasses import dataclass, field
from typing import List

@dataclass
class Tag():
    """A pixel tag"""
    name: str
    value: str

@dataclass
class Pixel():
    """Our flattened pixel object"""
    tags: List[Tag] = field(default_factory=list)
