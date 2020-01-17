#! /usr/bin/env python
# coding='utf-8'
"""
PDF文档书签制作
Author: zhiying
URL: www.zhouzying.cn
Data: 2020.01.17
Description: make bookmarks text.
    bookmark like this:
    BookmarkBegin
    BookmarkTitle: title
    BookmarkLevel: 1
    BookmarkPageNumber: 1

"""


def read_file(path):
    with open(path, 'rt') as f:
        for line in f.readlines():
            # print(line.split(' '))
            yield line


def parse_file(line):
    items = line.split(' ')
    # 中文目录
    """
    目录格式
    BookmarkBegin
    BookmarkTitle: title
    BookmarkLevel: 1
    BookmarkPageNumber: 1
    """
    if '第' in items[0]:
        book_mark_level = 1
    else:
        book_mark_level = 2
    title = str(line).replace(items[-1], '')
    page_number = int(str(items[-1]).strip())
    return title, book_mark_level, page_number


def main():
    path = './file.txt'
    offset = 8
    with open('./bookmark.txt', 'a', encoding='utf-8') as file:
        for line in read_file(path):
            title, book_mark_level, page_number = parse_file(line)
            file.write('BookmarkBegin\nBookmarkTitle: {}\nBookmarkLevel: {}\nBookmarkPageNumber: {}\n'.format(title, book_mark_level, page_number + offset))
        file.close()


if __name__ == "__main__":
    main()









