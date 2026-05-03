#!/usr/bin/env python3
"""
🚀 Co-founder GPT v11 & v12 - Complete Installation Setup

Setup script for both Co-founder v11 and v12 systems.
Provides easy installation and dependency management.
"""

from setuptools import setup, find_packages
import os

# Read README for long description
def read_readme():
    """Read README file for long description"""
    try:
        with open("README.md", "r", encoding="utf-8") as fh:
            return fh.read()
    except FileNotFoundError:
        return "Co-founder GPT - AI Business Intelligence Systems"

# Read requirements
def read_requirements():
    """Read requirements.txt file"""
    try:
        with open("requirements.txt", "r", encoding="utf-8") as fh:
            lines = fh.readlines()
            # Filter out comments and empty lines
            requirements = []
            for line in lines:
                line = line.strip()
                if line and not line.startswith("#") and not line.startswith("python>="):
                    requirements.append(line)
            return requirements
    except FileNotFoundError:
        return [
            "asyncio>=3.9.0",
            "aiohttp>=3.8.0", 
            "typing-extensions>=4.0.0",
            "python-dateutil>=2.8.0",
            "requests>=2.28.0",
            "pandas>=1.4.0",
            "numpy>=1.21.0"
        ]

setup(
    # Package metadata
    name="cofounder-gpt",
    version="12.0.0",
    author="Co-founder GPT Development Team",
    author_email="dev@cofounder-gpt.com",
    description="Revolutionary AI Business Intelligence Systems - Context Engineering v12 & Complete v11",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/soheiloliaei/Cofounder_v12",
    project_urls={
        "Bug Tracker": "https://github.com/soheiloliaei/Cofounder_v12/issues",
        "Documentation": "https://github.com/soheiloliaei/Cofounder_v12/blob/main/README.md",
        "Source Code": "https://github.com/soheiloliaei/Cofounder_v12",
        "Co-founder v11": "https://github.com/Donsoleil/Cofounder_v11"
    },
    
    # Package discovery
    packages=find_packages(),
    include_package_data=True,
    
    # Dependencies
    install_requires=read_requirements(),
    
    # Python version requirement
    python_requires=">=3.7",
    
    # Package classification
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Business",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Office/Business :: Financial",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8", 
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    
    # Keywords for discovery
    keywords=[
        "ai", "business-intelligence", "context-engineering", "startup", 
        "entrepreneurship", "business-strategy", "analytics", "automation",
        "chatgpt", "agents", "cofounder", "business-advisor"
    ],
    
    # Entry points for command-line tools
    entry_points={
        "console_scripts": [
            "cofounder-v11=Cofounder_v11.ChatGPT_10_Files.cofounder_main_orchestrator:main",
            "cofounder-v12=Co-founder_v12.Context_Engineering_Core.context_orchestrator_v12:main",
            "cofounder=Co-founder_v12.Context_Engineering_Core.context_orchestrator_v12:main",  # Default to v12
        ],
    },
    
    # Extra dependencies for optional features
    extras_require={
        "full": [
            "plotly>=5.0.0",
            "matplotlib>=3.5.0",
            "fastapi>=0.75.0",
            "uvicorn>=0.17.0",
            "sqlalchemy>=1.4.0",
            "stripe>=5.0.0"
        ],
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "mypy>=0.950",
            "flake8>=4.0.0"
        ],
        "docs": [
            "mkdocs>=1.4.0",
            "mkdocs-material>=8.0.0"
        ],
        "api": [
            "stripe>=5.0.0",
            "google-analytics-reporting-api>=4.0.0", 
            "mixpanel>=4.0.0"
        ]
    },
    
    # Package data
    package_data={
        "": [
            "*.md",
            "*.txt", 
            "*.yml",
            "*.yaml",
            "*.json",
            "*.sh"
        ],
    },
    
    # Zip safe
    zip_safe=False,
) 