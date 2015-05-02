#!/usr/bin/env python3
from mutagenx.easyid3 import EasyID3
import platform
import sys
import argparse
import glob


def tag_fix(file):
    try:
        tag = EasyID3(file)
        tag['artist'] = tag.get('artist', tag.get('performer', 'Unknown'))
        tag.save()
        print('Added artist tag of %s to %s' % (tag['artist'], file))
    except:
        print('Failed for %s' % file)
        pass


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.argv.append('--help')
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', metavar=('DIR'),
                        help=('Directory'))
    args = parser.parse_args()

    path = str(args.directory)

    if platform.system == 'Windows':
        flist = glob.glob(path + '\\*.' + 'mp3')
    else:
        flist = glob.glob(path + '/*.' + 'mp3')
    for file in flist:
        tag_fix(file)
