#! /usr/bin/env python
# coding:utf-8
"""
Author: zhiying
关注志颖博客(www.zhouzying.cn),一起探讨爬虫技术！
Date: 20-1-22 下午10:16
Description: package setup

"""
from setuptools import setup


def read_description():
    with open('./README.md') as readme:
        return readme.read()


setup(
    name='pdfBookmark',
    version='1.0.0beta8',
    description='Build bookmarks for PDF documents automatically.',
    long_description=read_description(),
    author='zhiying zhou',
    author_email='zhiyingstatham@qq.com',
    url='https://github.com/zyingzhou/pdfBookmark',
    license='GNU Affero General Public License v3.0',
    install_requires="pymupdf",

    py_modules=['pdfBookmark', 'fitz'],
    tests_require=['pytest'],
    entry_points={'console_scripts': ['pdfBookmark = pdfBookmark:main']}

)