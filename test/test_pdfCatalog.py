#! /usr/bin/env python
# coding:utf-8
"""
Author: zhiying
关注志颖博客(www.zhouzying.cn),一起探讨爬虫技术！
Date: 20-1-19 下午1:58
Description: test file.

"""
import fitz
from pdfCatalog import read_file
from pdfCatalog import parse_file
from pdfCatalog import check_bookmark
from pdfCatalog import _check_first_bookmark_level

path = '../pdfs/catalog.txt'
file = '../pdfs/现代通信网.pdf'
offset = 0


def test_read_file():

    for line in read_file(path):
        assert len(line.strip()) >= 1


def test_parse_file():
    catalog = []
    for line in read_file(path):
        title, book_mark_level, page_number = parse_file(line)
        catalog.append([book_mark_level, title, page_number + offset])
        assert len(title) != 0
        assert book_mark_level is '1' or '2'
        assert type(page_number) is int
    assert _check_first_bookmark_level(catalog) is False


def test_check_bookmark():
    doc = fitz.open(file)
    bookmark_list = check_bookmark(doc)
    assert type(bookmark_list) is list

