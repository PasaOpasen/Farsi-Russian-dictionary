# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 20:38:09 2020

@author: qtckp
"""

import PyPDF2
# pdf file object
# you can find find the pdf file with complete code in below
pdfFileObj = open('vocab3000.pdf', 'rb')

# pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# number of pages in pdf
print(pdfReader.numPages)

# a page object
pageObj = pdfReader.getPage(10)


# extracting text from page.
# this will print the text you can also save that into String
print(pageObj.extractText())





import tabula

df = tabula.read_pdf("vocab3000.pdf", pages=3)














