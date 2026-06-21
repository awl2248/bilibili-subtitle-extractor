#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup script for B站字幕提取器
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="bilibili-subtitle-extractor",
    version="1.0.0",
    author="awl2248",
    description="一个简单易用的Windows图形界面工具，用于从B站视频自动提取字幕并生成格式化的Markdown文稿",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/awl2248/bilibili-subtitle-extractor",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "bilibili-extractor=main:main",
        ],
    },
)
