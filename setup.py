from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="cryptozor.py",
    version="1.0.3",
    author="Merwane Draï",
    author_email="merwanedr@gmail.com",
    description="A Python Cryptocurrency converter.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/merwanedr/cryptozor.py",
    py_modules=["cryptozor"],
    package_dir={'': 'src'},
)