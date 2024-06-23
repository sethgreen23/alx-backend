#!/usr/bin/env python3
"""" Return start and end index for pagination """

import typing


def index_range(page: int, page_size: int) -> typing.Tuple[int, int]:
    """ Return start and end index for pagination """
    return ((page - 1) * page_size, (page - 1) * page_size + page_size)
