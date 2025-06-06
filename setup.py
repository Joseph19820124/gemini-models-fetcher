#!/usr/bin/env python3

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="gemini-models-fetcher",
    version="1.0.0",
    author="Joseph19820124",
    author_email="164839249+Joseph19820124@users.noreply.github.com",
    description="A Python script to fetch the latest Google Gemini models information via API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Joseph19820124/gemini-models-fetcher",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "flake8>=3.8",
            "black>=21.0",
            "isort>=5.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "gemini-models-fetcher=gemini_models_fetcher:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/Joseph19820124/gemini-models-fetcher/issues",
        "Source": "https://github.com/Joseph19820124/gemini-models-fetcher",
        "Documentation": "https://github.com/Joseph19820124/gemini-models-fetcher#readme",
        "Changelog": "https://github.com/Joseph19820124/gemini-models-fetcher/blob/main/CHANGELOG.md",
    },
    keywords="google gemini ai models api fetch machine-learning artificial-intelligence",
    include_package_data=True,
    zip_safe=False,
)