import codecs
import os

from setuptools import find_packages, setup

main_ns = {}
ver_path = os.path.normcase('chainbreaker/version.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)


dependencies = [
    'argparse',
    'pycryptodome',
]

setup(
    name='chainbreaker',
    version=main_ns['__version__'],
    author='n0fate',
    author_email=codecs.encode('80008322+TvatreTrarfgr@hfref.abercyl.tvguho.pbz', 'rot-13'),
    license='GPL-2.0',
    url='https://github.com/GingerGeneste/chainbreaker',
    description='Extract information from OSX keychain files',
    packages=find_packages(exclude=['tests']),
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    entry_points={
        'console_scripts': ['chainbreaker=chainbreaker:main'],
    },
    install_requires=dependencies,
)
