#!/usr/bin/env python3
"""
Hypermedia pagination module
"""

import csv
import math
from typing import List


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_csv(self, filename: str =
                '0-simple_helper_function.py') -> List[List]:
        """function to convert csv into python list"""
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            csv_list = []

        for row in csv_reader:
            csv_list.append(row)
        return csv_list

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """function to get list of results according to indexes
        """
        assert isinstance(page, int) and isinstance(page_size, int), "[]"
        assert page > 0 and page_size > 0, "[]"

        with open('Popular_Baby_Names.csv', 'r') as file:
            csv_reader = csv.reader(file)
            csv_list = []

            for row in csv_reader:
                csv_list.append(row)
                # print(csv_list[9:10])

        page_index = index_range(page, page_size)
        # print(page_index)
        start_index = page_index[0] + 1
        end_index = page_index[1] + 1
        # print(start_index)
        # print(end_index)
        page_items = csv_list[start_index:end_index]
        return page_items

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns dictionary representation of content retrieved
        """
        data = self.get_page(page, page_size)

        if 19418 % page_size == 0:
            total_pgs = int(19418 / page_size)
        else:
            total_pgs = int((19418 / page_size) + 1)

        if page >= total_pgs:
            nxt_pg = None
        else:
            nxt_pg = page + 1

        if page <= 1:
            prev_pg = None
        else:
            prev_pg = page - 1

        hyper_dict = {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": nxt_pg,
            "prev_page": prev_pg,
            "total_pages": total_pgs
        }

        return hyper_dict
