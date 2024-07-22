#!/usr/bin/env python3
"""
Index range.
"""

def index_range(page: int, page_size: int) -> tuple[int, int]:
    """Return a tuple of size two containing a start index and an end index.
    
    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.
    
    Returns:
        tuple[int, int]: A tuple containing the start and end index.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
