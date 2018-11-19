from setuptools import find_packages, setup

__version__ = "2.3.0"

setup(
    name="spawningtool",
    description="Build order parser for StarCraft 2 replays",
    long_description=open("README.md").read()+"\n\n"+open("CHANGELOG.md").read(),
    version=__version__,
    url="https://github.com/StoicLoofah/spawningtool",
    author="Kevin Leung",
    author_email="kkleung89@gmail.com",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Topic :: Games/Entertainment",
        "Topic :: Games/Entertainment :: Real Time Strategy",
    ],
    entry_points={
        'console_scripts': [
            "spawningtool = spawningtool.__main__:main",
        ],
    },
    install_requires=[
        'argparse',
        'sc2reader==1.3.0',
    ],
    packages=find_packages(exclude=['tests']),
)
