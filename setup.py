from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='three-commas',
    packages=['three_commas',
              'three_commas.api',
              'three_commas.api.ver1',
              'three_commas.api.v2',
              'three_commas.model',
              'three_commas.utils',
              'three_commas.streams',
              ],
    version='0.2.7',
    description='Python api wrapper for 3commas with extended functionality in the api, models, error handling',
    url='https://github.com/badass-blockchain/python-three-commas',
    author='Sergey Gerodes',
    author_email='sgerodes@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['some_module'],
    package_dir={'': 'src'},
    keywords=['python', 'scrapy', 'scrapy-items', 'dot-items', 'dot'],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    install_requires=[]
)
