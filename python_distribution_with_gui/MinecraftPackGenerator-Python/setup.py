#!/usr/bin/env python3
"""
Minecraft Pack Generator - セットアップスクリプト
"""

from setuptools import setup, find_packages
import os

# READMEファイルを読み込み
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), "README.txt")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            return f.read()
    return "MinecraftのResourcePackとDataPackを自動生成するツール"

# requirements.txtを読み込み
def read_requirements():
    requirements_path = os.path.join(os.path.dirname(__file__), "requirements.txt")
    if os.path.exists(requirements_path):
        with open(requirements_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return []

setup(
    name="minecraft-pack-generator",
    version="1.0.0",
    author="けんすけ",
    author_email="",
    description="MinecraftのResourcePackとDataPackを自動生成するツール",
    long_description=read_readme(),
    long_description_content_type="text/plain",
    url="",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Games/Entertainment",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pyinstaller>=5.0.0",
        ],
        "full": [
            "colorama>=0.4.0",
            "tqdm>=4.64.0",
            "jsonschema>=4.0.0",
            "Pillow>=9.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "minecraft-pack-generator=pack_generator:main",
            "mpg=pack_generator:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.json", "*.txt", "*.bat"],
    },
    keywords="minecraft, datapack, resourcepack, generator, automation",
    project_urls={
        "Bug Reports": "",
        "Source": "",
        "Documentation": "",
    },
) 