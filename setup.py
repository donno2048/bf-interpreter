from setuptools import setup,find_packages
setup(
    name='clibf',
    version='1.0.0',
    description='CLI tool to execute Brainfuck code from files and strings',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/donno2048/bf-interpreter',
    packages=find_packages(),
    license='MIT',
    author='Elisha Hollander',
    classifiers=['Programming Language :: Python :: 3']
)
