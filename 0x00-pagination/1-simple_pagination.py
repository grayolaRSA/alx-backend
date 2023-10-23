#!/usr/bin/env python3
"""
Simple pagination module
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
                # print(csv_list)

        page_index = index_range(page, page_size)
        print(page_index)
        start_index = page_index[0]
        end_index = page_index[1]
        print(start_index)
        print(end_index)
        page_items = csv_list[page_index[0]:page_index[1]]
        return page_items
