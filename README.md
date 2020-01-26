# pdfBookmark

## Overview
pdfBookmark is a lightweight library which can build bookmarks for pdf documents  automatically. 

## Requirements
* Python 3.x
* Works on Linux, Windows, Mac OSX

## Install
The quick way:
```bash
pip install pdfBookmark
```

## User Guide
### 1.On the Linux 
* a. Open the terminal, come the working directory.
```bash
cd pdf-file-path/
```
* b. Use pdfBookmark command. 
```bash
pdfBookmark -f pdf-file-name.pdf -c bookmark.txt -s your offset -o ./ -i 1
```
#### Argument: 
Arguments | Description
--------- | ------------
-h | for help information. 
-f | (required) Specify the path of pdf file you want to import bookmark in. 
-c | (required) Specify the path of the bookmark. 
-o | (required) Specify the path to save output pdf file. 
-s | (optional) Number, default is 0.The offset of PDF document compared with Bookmark.
-i | (optional) Value is 1 or 0, default is 1. 1 means ignoring the old bookmark in the PDF document

### 2.On the Windows 
win + R open the terminal, the next steps are the same as on the Linux.

## Releases
v1.0.0: First release. Build bookmarks for pdf documents automatically.