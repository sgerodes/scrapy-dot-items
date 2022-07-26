from setuptools import setup
import subprocess


version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)


with open('README.md', 'r') as fh:
    long_description = fh.read()


setup(
    name='scrapy-dot-items',
    packages=['scrapy_dot_items',],
    version=version,
    description='A Scrapy addon that allows to access arguments via the dot',
    url='https://github.com/sgerodes/scrapy-items',
    author='Sergey Gerodes',
    author_email='sgerodes@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['some_module'],
    package_dir={'': 'src'},
    keywords=['python', 'scrapy', 'scrapy-items', 'dot-items', 'dot'],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    install_requires=[]
)
