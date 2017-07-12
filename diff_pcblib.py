#!/usr/bin/env python3
import olefile
import git
import urllib.request
import os.path
import tempfile
import shutil
from termcolor import colored, cprint

GITHUB_REPO = 'https://github.com/uw-midsun/hardware.git'
GITHUB_RAW = 'https://raw.githubusercontent.com/uw-midsun/hardware/{0}/altium-lib/{1}'

def compare_pcblib(original, new):
  ole_org = olefile.OleFileIO(original)
  ole_new = olefile.OleFileIO(new)
  sources = [ole_org, ole_new]

  parts = [[] for x in range(len(sources) + 1)]

  streams = sorted([list(x) for x in set(tuple(x) for x in ole_org.listdir() + ole_new.listdir()
                                         if 'UniqueIDPrimitiveInformation' in x and 'Data' in x)])
  for x in streams:
    data = []
    for i, s in enumerate(sources):
      try:
        data.append(s.openstream(x).read())
      except IOError:
        parts[i].append(x[0])
        continue

    if len(set(data)) != 1:
      parts[-1].append(x[0])

  return parts

def print_diff(parts):
  names = [
    colored('New', 'green', attrs=['bold']),
    colored('Removed', 'red', attrs=['bold']),
    colored('Modified', 'yellow', attrs=['bold'])
  ]

  for i, part_list in enumerate(parts):
    print(names[i])
    for p in part_list:
      print('- {0}'.format(p))

def download_lib(branch, filename, dest_dir):
  g = git.cmd.Git()

  full_hash = None

  try:
    full_hash = g.rev_parse('{0}^{{commit}}'.format(branch))
  except git.exc.GitCommandError:
    for ref in g.ls_remote(GITHUB_REPO).split('\n'):
      if branch in ref:
        full_hash = ref.split('\t')[0]
        break

  if not full_hash:
    raise LookupError('Commit or branch {0} not found!'.format(branch))

  target_filename = os.path.join(dest_dir, '{0}{1}'.format(full_hash, os.path.splitext(filename)[1]))
  print(GITHUB_RAW.format(full_hash, filename))
  urllib.request.urlretrieve(GITHUB_RAW.format(full_hash, filename), target_filename)
  return target_filename

if __name__ == '__main__':
  import argparse

  parser = argparse.ArgumentParser('Diff Altium PcbLib - may have false positives')
  parser.add_argument('original')
  parser.add_argument('new')
  args = parser.parse_args()

  dirpath = tempfile.mkdtemp()

  org = download_lib(args.original, 'Footprints.PcbLib', dirpath)
  new = download_lib(args.new, 'Footprints.PcbLib', dirpath)

  print_diff(compare_pcblib(org, new))

  shutil.rmtree(dirpath)
