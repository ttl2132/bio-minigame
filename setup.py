#!/usr/bin/env python

"""
Install piglatin package. To install locally use:
    'pip install -e ."
"""

from setuptools import setup

setup(
    name="bio-minigame",
    version="0.0.1",
    install_requires=["pandas", "numpy", "kivy", "fastapi", "uvicorn",
                      "loguru", "PyGithub"],
    packages=[],
    setup_requires=['setuptools_scm'],
    include_package_data=True,
    entry_points={
        "console_scripts": ["bio-minigame = minigame.__main__:run_program"]
    }
)
