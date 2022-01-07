from setuptools import setup,find_packages
setup(
    name='clibf',
    version='1.0.4',
    description='CLI tool to execute Brainfuck code from files and strings',
    long_description=open('README.md').read().replace('my_bf_string', open('example.b').read()),
    long_description_content_type="text/markdown",
    url='https://github.com/donno2048/bf-interpreter',
    packages=find_packages(),
    license='MIT',
    install_requires=['questionary>=1.10.0'],
    author='Elisha Hollander',
    classifiers=['Programming Language :: Python :: 3'],
    entry_points={ 'console_scripts': [ 'clibf=clibf.__main__:main' ] }
)
