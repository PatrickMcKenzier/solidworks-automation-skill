"""
SolidWorks Automation Python helper package.
"""

from .sw_connect import connect_solidworks, deg, mm, new_document, open_document, save_document
from .sw_session import SolidWorksSession, session

__all__ = [
    "SolidWorksSession",
    "connect_solidworks",
    "deg",
    "mm",
    "new_document",
    "open_document",
    "save_document",
    "session",
]

