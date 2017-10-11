#!/usr/bin/python3

import os, shutil

os.path.exists('oops.txt')

print(os.path.exists('.'))

print(os.path.isfile('17-os.py'))

print(os.path.isdir('17-os.py'))

print(os.path.isabs('/big/fake/name'))

print(os.path.isabs('big/fake/name/without/a/leading/slash'))



# shutil.copy('oops.txt', 'ohno.txt')
# shutil.move()

# os.link('oops.txt', 'yikes.txt')
# os.path.isfile('yikes.txt')
#True

# os.path.islink('yikes.txt')
#False

# os.symlink('oops.txt', 'jeepers.txt')
# os.path.islink('jeepers.txt')
#True
# os.path.realpath('jeepers.txt')
#/usr/gaberlunzie/oops.txt

# os.chmod('oops.txt', 0o400)

# import stat
# os.chmod('oops.txt', stat.S_IRUSR)

# uid = 5
# gid = 22
# os.chown('oops', uid, gid)

print(os.path.abspath('17-os.py'))

# os.remove('oops.txt')

os.mkdir('poems')
print(os.path.exists('poems'))
print(os.listdir('poems'))

os.mkdir('poems/mcintyre')
print(os.listdir('poems'))
os.chdir('poems')
os.chdir('..')

# print(os.rmdir('poems')) - empty directory
print(shutil.rmtree('poems'))

