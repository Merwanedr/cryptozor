import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cryptozor",
    version="1.0.0",
    author="Merwane Draï",
    author_email="merwanedr@gmail.com",
    description="A Python Cryptocurrency converter.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/merwanedr/cryptozor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)