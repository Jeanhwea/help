#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time

here = os.getcwd()
article = 'article'

def getinfo(dir):
  orgfiles = []
  for root, dirs, files in os.walk(dir):
    for file in files:
      if file.endswith('.org'):
        filepath = os.path.join(root, file)
        title = ''
        date = ''
        with open(filepath, 'r') as f:
          for line in f:
            if line.startswith('#+TITLE:'):
              title = line.replace('#+TITLE:', '').strip()
            if line.startswith('#+DATE:'):
              date = line.replace('#+DATE:', '').strip()
        orgfiles.append((filepath, title, date))
  return orgfiles

def genindex(infos):
  index = ''
  i = 1
  for path, title, date in infos:
    index += '{i}. [[{path}][{title}]] {date}\n'.format(
      i=i, path=path, title=title, date=date
    )
    i += 1
  return index

def writereadme(index):
  content = ''
  with open('readme.org', 'r') as f:
    for line in f:
      content += line
      if line.startswith('*'):
        break
  content += '\n'
  content += index
  with open('readme.org', 'w') as f:
    f.write(content)

infos = getinfo(article)
index = genindex(infos)
writereadme(index)
