from setuptools import setup, find_packages, Extension
from os.path import join
setup(
    name='clibf',
    version='1.1.3',
    description='CLI tool to execute Brainfuck code from files and strings',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/donno2048/bf-interpreter',
    ext_modules=[Extension('_clibf', [join('clibf', '__init__.c')])],
    packages=find_packages(),
    license='MIT',
    install_requires=['questionary>=1.10.0'],
    author='Elisha Hollander',
    classifiers=['Programming Language :: Python :: 3'],
    entry_points={ 'console_scripts': [ 'clibf=clibf.__main__:main' ] },
    zip_safe = False,
    include_package_data=True
)
