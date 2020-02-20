import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="beat_orm",
    version="0.0.2",
    author="Ningzi",
    author_email="ningzi0610@gmail.com",
    description="beat's orm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NingziSlay/beat_orm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
