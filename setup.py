import sys
from setuptools import setup

if sys.version_info < (3,9):
    sys.exit('Sorry, Python < 3.9 is not supported')

setup(
    name="fasticule",
    version="0.0.1",
    install_requires=[
        "fastapi ~= 0.86.0",
        "uvicorn ~= 0.19.0",
    ]
)