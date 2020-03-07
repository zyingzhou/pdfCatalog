pdfCatalog
==========

Overview
--------

pdfCatalog is a lightweight library which can build catalogs for pdf
documents automatically.

Requirements
------------

-   Python 3.x
-   Works on Linux, Windows, Mac OSX

Install
-------

The quick way:

::

     pip install pdfCatalog


User Guide
----------

1.On the Linux

 -   a.  Open the terminal, come the working directory.


       ::

        cd pdf-file-path/

 -   b.  Use pdfCatalog command.

        ::

         pdfCatalog -f pdf-file-name.pdf -c catalog.txt -s your offset -o ./ -i 1

 - Argument:

         ==========   ==================
         Arguments    Description
         ==========   ==================
         -h           for help information.
         -f           (required) Specify the path of pdf file you want to import catalog in.
         -c           (required) Specify the path of the catalog.
         -o           (required) Specify the path to save output pdf file.
         -s           (optional) Number, default is 0.The offset of PDF document compared with catalog.
         -i           (optional) Value is 1 or 0, default is 1. 1 means ignoring the old catalog in the PDF document
         ==========   ==================


 - Catalog should like this: title + page

    ::

     前言　话说“通信”基本概念　1
     第 1章　通信发展史　9
     古代通信：信息沟通的起步　10
     近现代通信：电磁通信和数字时代的起步　11
     当代通信：移动通信和互联网时代　14
     未来通信：大融合时代　15
     第 2章　用什么实现通信　17
     电信网中的通信工具　17
     互联网的通信手段　21
     专业领域的通信工具　24
     家电中的通信工具　25
     第3章　通信到底是干嘛的　27
     第 1个问题：用什么信息格式传递给对方——编码　28
     第 2个问题：如何找到对方——寻址　30
     第3个问题：信息传递的额外要求——网络优化　31
     额外的一个问题——人性化　33

2.On the Windows

win + R open the terminal, the next steps are the same as on the Linux.

Releases
========

v1.0.2: Use utf-8 encoding text and catalog becomes more beautiful!

v1.0.1: Fixed some bugs.

v1.0.0: First release. Build catalogs for pdf documents automatically.