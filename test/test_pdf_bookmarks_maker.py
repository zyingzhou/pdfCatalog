#! /usr/bin/env python
# coding:utf-8
"""
Author: zhiying
关注志颖博客(www.zhouzying.cn),一起探讨爬虫技术！
Date: 20-1-19 下午1:58
Description: test file.

"""
import pytest
import re
import fitz


def read_file(path):
    with open(path, 'rt') as f:
        for line in f.readlines():
            # print(line.split(' '))
            yield line


def parse_file(line):
    # items = line.split(' ')
    pattern = "\d+"
    page_number = int(re.findall(pattern, line)[-1])
    # 中文目录
    """
    目录格式
    BookmarkBegin
    BookmarkTitle: title
    BookmarkLevel: 1
    BookmarkPageNumber: 1
    """
    if '第' in line:
        book_mark_level = 1
    else:
        book_mark_level = 2
    # title = str(line).replace(str(page_number), '')
    title = line
    return title, book_mark_level, page_number


path = '../pdfs/现代通信网_书签.txt'


def test_read_file():

    for line in read_file(path):
        assert list(line).count('\n') == 1


def test_parse_file():
    for line in read_file(path):
        title, book_mark_level, page_number = parse_file(line)
        assert len(title) != 0
        assert book_mark_level is '1' or '2'
        assert type(page_number) is int

