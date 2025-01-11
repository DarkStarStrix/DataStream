import os
from setuptools import setup, find_packages

# Check if README.md exists
readme = "README.md"
if os.path.exists(readme):
    with open(readme, "r") as fh:
        long_description = fh.read()
else:
    long_description = ""

setup(
    name="DataVolt",
    version="0.0.1",
    author="Allan",
    author_email="allanw.mk@gmail.com",
    description="A resuable workflow for data engineering piplines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DarkStarStrix/DataVolt",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9+',
)
