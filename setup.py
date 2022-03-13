"""Install packages as defined in this file into the Python environment."""
from setuptools import setup, find_namespace_packages

setup(
    name="space_adventure_text_game",
    author="Eric Slutz",
    author_email="eric.slutz@icloud.com",
    url="https://github.com/eslutz/Space-Adventure-Text-Game",
    description="A small text based game.",
    version="1.0.0",
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src", exclude=["tests"]),
    install_requires=[
        "setuptools>=45.0",
    ],
    entry_points={
        "console_scripts": [
            "space_adventure_text_game=space_adventure_text_game.__main__:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Environment :: Console",
    ],
)
