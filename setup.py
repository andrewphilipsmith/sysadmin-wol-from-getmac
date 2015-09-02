from distutils.core import setup
import sys
import py2exe

sys.argv.append('py2exe')

setup(
    options={'py2exe': {'bundle_files': 1, 'compressed': True}},
    zipfile=None,
    name='sysadmin-wol-from-getmac',
    version='1.0.0',
    url='www.mapaction.org',
    install_requires=['wakeonlan>=0.2.2'],
    license='',
    author='asmith',
    author_email='asmith@mapaction.org',
    description='',
    console=['wol4getmac.py']
)
