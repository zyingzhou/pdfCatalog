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
    with open('./README.rst') as readme:
        return readme.read()


setup(
    name='pdfCatalog',
    version='1.0.1',
    description='Build catalogs for PDF documents automatically.',
    long_description=read_description(),
    long_description_content_type='text/x-rst',
    author='zhiying zhou',
    author_email='zhiyingstatham@qq.com',
    url='https://github.com/zyingzhou/pdfCatalog',
    license='GNU Affero General Public License v3.0',
    install_requires="pymupdf",

    py_modules=['pdfCatalog', 'fitz'],
    tests_require=['pytest'],
    entry_points={'console_scripts': ['pdfCatalog = pdfCatalog:main']},
    classifiers=[
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]

)
