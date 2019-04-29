import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="embl-ebi-person",
    version="0.0.1",
    author="Chris Sam",
    author_email="chris.sam@example.com",
    description="A client which generates Person entities as JSON and XML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chrissam/embl-ebi-person.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
