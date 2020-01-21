#! /usr/bin/env python
# coding='utf-8'
"""
PDF文档书签制作
Author: zhiying
URL: www.zhouzying.cn
Data: 2020.01.17
Description: make bookmarks with pymupdf.
"""
# for Ubuntu 18.04.3 LTS you can try those commands to install pymupdf on your computer.
# sudo -H pip3 install --upgrade pip
# sudo -H python3.6 -m pip install -U pymupdf
import fitz
import re


def read_file(path):
    with open(path, 'rt') as f:
        for line in f.readlines():
            # print(line.split(' '))
            # ignore blank line
            if len(line.strip()) > 0:
                yield line
            else:
                continue


def parse_file(line):
    # add Escape character
    pattern = "\\d+"
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
    elif '附录' in line:
        book_mark_level = 1
    elif '参考文献' in line:
        book_mark_level = 1
    else:
        book_mark_level = 2
    # title = str(line).replace(str(page_number), '')
    title = line
    return title, book_mark_level, page_number


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


def main():
    path = '../pdfs/现代通信网_书签.txt'
    offset = 9
    doc = fitz.open('../pdfs/现代通信网.pdf')
    catalog = []
    if len(check_bookmark(doc)) != 0:
        items = check_bookmark(doc)
        catalog += items
    for line in read_file(path):
        title, book_mark_level, page_number = parse_file(line)
        catalog.append([book_mark_level, title, page_number + offset])
    doc.setToC(catalog)
    doc.save('../pdfs/现代通信网_已添加书签.pdf')


if __name__ == "__main__":
    print('beginning adding bookmarks into pdf files\n')
    main()
    print('Adding bookmarks successfully.\n')










