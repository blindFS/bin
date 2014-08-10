#!/usr/bin/env python2
import gnupg

gpg = gnupg.GPG(gnupghome='/home/farseer/.gnupg')
with open('/home/farseer/.mutt/.gmail.gpg', 'rb') as f:
    data = gpg.decrypt_file(f)
    print str(data).split('\n')[0].split('"')[1]
