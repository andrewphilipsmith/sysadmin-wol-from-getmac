#!python3.3
from distutils.core import setup
import sys

import pip
pip.main(['install', 'wakeonlan'])
pip.main(['install', 'py2exe'])
import py2exe

sys.argv.append('py2exe')

py2exe_options = dict(excludes=['_ssl',  # Exclude _ssl
                                'pyreadline', 'difflib', 'doctest',
                                'optparse', 'pickle', 'calendar'],  # Exclude standard library
                      dll_excludes=['msvcr71.dll'],  # Exclude msvcr71
                      bundle_files=1,
                      compressed=True,
                      )

wrapper_scripts = [('', ['wake_laptops_even_numbers.cmd', 'wake_laptops_odd_numbers.cmd'])]

setup(
    options={'py2exe': py2exe_options},
    zipfile=None,
    name='sysadmin-wol-from-getmac',
    version='1.0.0',
    url='www.mapaction.org',
    data_files=wrapper_scripts,
    license='',
    author='asmith',
    author_email='asmith@mapaction.org',
    description='',
    console=['wol4getmac.py']
)
