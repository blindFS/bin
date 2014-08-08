#!/usr/bin/env python2

# -*- coding: utf-8 -*-
# @Author: nubes
# @Date:   2014-06-05 21:22:11
# @Last Modified by: farseer
# @Last Modified time: 2014-07-03 14:46:13

from bencode import bdecode, bencode
import platform
import sys
import argparse
import os
import glob

filter_list = ['.mkv', '.mp4', '.wmv', '.avi',
               '.rmvb', '.rm', '.jpg', '.jpeg', '.mpg']


def meta_random(torrentfile, setting=None):
    meta_file = open(torrentfile, 'rb')
    metainfo = bdecode(meta_file.read())
    meta_file = open(torrentfile, 'wb')
    files = metainfo['info']['files']
    try:
        iter(files)
    except TypeError:
        files = [files]

    if 'encoding' in metainfo:
        code = metainfo['encoding']
    else:
        code = 'GBK'
    print 'encoding: %s' % str(code)
    for f in files:
        filename, suffix = os.path.splitext(f['path'][-1].decode(code))
        change_name = None

        if setting == 'random' or suffix not in filter_list:
            change_name = ''.join(
                map(lambda xx: (hex(ord(xx))[2:]), os.urandom(16))) + suffix
        elif setting == 'invert':
            change_name = filename[::-1] + suffix
            # change_name = '_'.join(filename) + suffix
        if change_name is not None:
            print "changeing from %s to %s" % (filename, change_name)
            f['path'] = [change_name.encode(code)]
            f['path.utf-8'] = [change_name.encode('utf-8')]

    random_name = ''.join(map(lambda xx: (hex(ord(xx))[2:]), os.urandom(16)))
    metainfo['info']['name'] = random_name.encode(code)
    if setting == 'invert' and 'name.utf-8' in metainfo['info']:
        t_name = metainfo['info']['name.utf-8']
        metainfo['info'][
            'name.utf-8'] = t_name.decode('utf-8')[::-1].encode('utf-8')
    elif setting == 'random':
        metainfo['info']['name.utf-8'] = random_name.encode('utf-8')
    meta_file.write(bencode(metainfo))
    meta_file.close()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.argv.append('--help')
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--level', metavar=('LEVEL'),
                        help=('Random level random/invert'))
    parser.add_argument('directory', metavar=('DIR'),
                        help=('Directory'))
    args = parser.parse_args()

    setting = str(args.level)
    path = str(args.directory)

    if platform.system == 'Windows':
        flist = glob.glob(path + '\\*.' + 'torrent')
    else:
        flist = glob.glob(path + '/*.' + 'torrent')

    for file in flist:
        print 'file: %s' % file
        meta_random(file, setting)
        print 'done'
