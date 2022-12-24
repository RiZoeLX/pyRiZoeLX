
import re
from setuptools import setup

with open('RiZoeLX/version.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements = ['pyrogram', 'telethon', 'py-tgcalls']

setup(
    name='pyRiZoeLX',
    author='MrRiZoeL',
    author_email='xrizoel@gmail.com',
    version=version,
    description='',
    long_description=,
    url='https://github.com/RiZoeLX/pyRiZoeLX',
    packages=['pyRiZoeLX'],
    license='GNU General Public License v3.0',
    classifiers=[
        "Framework :: AsyncIO",
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        "Natural Language :: English",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.7',
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Build Tools",

    ],
    include_package_data=True,
    keywords=['telegram', 'pyRiZoeLX', 'RiZoeLX', 'pyrogram', 'functions', 'py-RiZoeLX'],
    install_requires=requirements,
    python_requires=">3.7, <3.11",
)
