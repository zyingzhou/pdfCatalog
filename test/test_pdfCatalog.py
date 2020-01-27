#! /usr/bin/env python
# coding:utf-8
"""
Author: zhiying
关注志颖博客(www.zhouzying.cn),一起探讨爬虫技术！
Date: 20-1-19 下午1:58
Description: test file.

"""
import re
import fitz
import time

path = '../pdfs/catalog.txt'
file = '../pdfs/现代通信网.pdf'


def read_file(path):
    with open(path, 'rt') as f:
        for line in f.readlines():
            # print(line.split(' '))
            # ignore blank line
            if len(line.strip()) > 0:
                # strip the space behind the page-number
                yield line.strip()
            else:
                continue


def parse_file(line):
    regex = re.compile(r'(.*?)(\s*)(\d+$)')
    try:
        result = regex.search(line)
        title = result.group(1).strip()
        page_number = int(result.group(3).strip())
        if '第' in line and '章' in line:
            book_mark_level = 1
        elif '附录' in line:
            book_mark_level = 1
        elif '参考文献' in line:
            book_mark_level = 1
        else:
            book_mark_level = 2
        return title, book_mark_level, page_number

    except:
        with open('./pdfCatalog_error_log.txt', 'a', encoding='utf-8') as log:
            print('Error: This line"{}" lacks page number.'.format(line))
            log.write('{}: This line may be have wrong: {}\n'.format(time.asctime(), line))
            log.close()


# check the completeness of a pdf catalog
def check_bookmark(doc):
    toc = doc.getToC()
    i = 0
    for item in toc:
        if str(item[1]).isdigit():
            break
        else:
            i += 1

    return toc[:i]


def test_read_file():

    for line in read_file(path):
        assert len(line.strip()) >= 1


def test_parse_file():
    for line in read_file(path):
        title, book_mark_level, page_number = parse_file(line)
        assert len(title) != 0
        assert book_mark_level is '1' or '2'
        assert type(page_number) is int


def test_check_bookmark():
    doc = fitz.open(file)
    bookmark_list = check_bookmark(doc)
    assert type(bookmark_list) is list
