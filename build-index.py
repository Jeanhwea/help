#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time

here = os.getcwd()
article = 'article'

def getinfo(dir):
  orgfiles = []
  prefix = '#+TITLE:'
  for root, dirs, files in os.walk(dir):
    for file in files:
      if file.endswith('.org'):
        filepath = os.path.join(root, file)
        update = time.strftime('<%Y-%m-%d %a>', time.localtime(os.path.getmtime(filepath)))
        title = ''
        with open(filepath, 'r') as f:
          for line in f:
            if line.startswith(prefix):
              title = line.replace(prefix, '').strip()
        orgfiles.append((filepath, title, update))
  return orgfiles

def genindex(infos):
  index = ''
  i = 1
  for path, title, update in infos:
    index += '{i}. [[{path}][{title} {update}]]\n'.format(
      i=i, path=path, title=title, update=update
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
  content += index
  with open('readme.org', 'w') as f:
    f.write(content)

infos = getinfo(article)
index = genindex(infos)
writereadme(index)
