from setuptools import setup
import subprocess
import os

scrapy_dot_items_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

assert os.path.isfile("cf_remote/version.py")
with open("scrapy_dot_items/VERSION", "w", encoding="utf-8") as fh:
    fh.write("%s\n" % scrapy_dot_items_version)


with open('README.md', 'r') as fh:
    long_description = fh.read()


setup(
    name='scrapy-dot-items',
    packages=['scrapy_dot_items',
              ],
    # version='0.1.1',
    version=scrapy_dot_items_version,
    description='A Scrapy addon that allows to access arguments via the dot',
    url='https://github.com/sgerodes/scrapy-items',
    author='Sergey Gerodes',
    author_email='sgerodes@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['some_module'],
    package_dir={'': 'src'},
    package_data={"scrapy_dot_items": ["VERSION"]},
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
