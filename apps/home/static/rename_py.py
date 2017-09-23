import os
from functools import partial

__author__ = 'cityblack1'

__doc__ = """
将目录下带'.下载'文件去掉, 并将带括号的文件删掉
"""
a = os.path.abspath('.')
join2 = partial(os.path.join, a)

dirs = [_ for _ in os.listdir('.') if _.endswith('.下载')]
r_dirs = [_[:-3] for _ in dirs if _.endswith('.下载')]
zip_dirs = list(zip(dirs, r_dirs))
for x in zip_dirs:
    os.rename(*x)


