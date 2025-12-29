from setuptools import find_packages, setup

setup(
    name="mcqgenerator",
    version="0.0.2",
    author="Prem Manchina",
    author_email="premmanchina33@gmail.com",  # fixed invalid email domain
    description="An intelligent MCQ generator using LangChain and Gemini AI",
    packages=find_packages(),
    install_requires=[
        "openai>=1.0.0",
        "langchain==0.3.7",
        "langchain-community==0.3.7",
        "python-dotenv>=1.0.0",
        "streamlit>=1.28.0",
        "PyPDF2>=3.0.0",
        "google-generativeai==0.8.3"
    ],
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ],
)
