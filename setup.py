from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'pythum',
    packages = ['pythum'],
    version = 'v1.0.0',  # Ideally should be same as your GitHub release tag varsion
    description = 'Simple minimalist quantum computing simalation for python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'metadeta96',
    author_email = 'metadeta96@gmail.com',
    url = 'https://github.com/metadeta96/pythum',
    download_url = 'https://github.com/metadeta96/pythum',
    keywords = ['quantum', 'python', 'pythum', 'computing', 'simulator', 'simulation'],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)