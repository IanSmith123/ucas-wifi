# Created by Les1ie on 2019/9/9.
# Email: me@les1ie.com

import setuptools
import platform
import os

system = platform.system()


def set_require():
    return ['requests']


with open("README.md", 'r', encoding='utf8') as f:
    long_description = f.read()

setuptools.setup(
    name="ucas-wifi",
    version="1.0.1",
    author="Les1ie",
    author_email="me@les1ie.com",
    description="login ucas wifi in terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/iansmith123/ucas-wifi',
    packages=setuptools.find_packages(),
    license="GPL v3",
    install_requires=set_require(),
#    scripts=set_scripts(),
    entry_points={
        'console_scripts': ['ucas-wifi=script.ucas_wifi:main']}
)
