"""xrcat - setup.py"""
from setuptools import setup

LONG_DESC = open('README.md').read()
setup(
    name="xrcat",
    version="1.0.0",
    author="HolmDev",
    author_email="fredholm.xyz@protonmail.com",
    description="A small tool for retriving resources from Xresources",
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    url="https://github.com/HolmDev/xrcat",
    keywords="xrcat, xrdb, xorg, xresources",
    license="GPLv3",
    classifiers=[
        "Environment :: X11 Applications",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
    ],
    python_requires=">=3.6, <4",
    install_requires=[
        "python-xlib"
    ],
    include_package_data=False,
    entry_points={
        "runners": [
            "xrcat=xrcat:main"
        ],
        "console_scripts": [
            'xrcat = xrcat.__main__:main'
        ],
    }
)
