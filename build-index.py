#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


class IndexManager(object):

  def __init__(self):
    self._readme = 'readme.org'

  def getmeta(self, fullpath):
    info = {'fullpath': fullpath}
    with open(fullpath, 'r') as f:
      for line in f:
        if line.startswith('#+TITLE:'):
          info['title'] = line.replace('#+TITLE:', '').strip()
        if line.startswith('#+DATE:'):
          info['date'] = line.replace('#+DATE:', '').strip()
    return info

  def getinfos(self, dir):
    infos = []
    for root, dirs, files in os.walk(dir):
      for file in files:
        if file.endswith('.org'):
          fullpath = os.path.join(root, file)
          infos.append(self.getmeta(fullpath))
    return infos

  def infos2text(self, infos):
    return '\n'.join(map(
        lambda x, i: '{i}. [[{path}][{title}]] {date}'.format(
            i=i, path=x['fullpath'], title=x['title'], date=x['date']
        ), infos
    ))

  def readheader(self):
    header = ''
    with open(self._readme, 'r') as f:
      for line in f:
        header += line
        if line.startswith('*'):
          break
        header += '\n'

  def writereadme(self, infos):
    article_infos = self.getinfos('article')
    python_infos = self.getinfos('python')

    content = self.readheader()
    with open(self._readme, 'w', encoding='utf-8') as f:
      f.write(content)
