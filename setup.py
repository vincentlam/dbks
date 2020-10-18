import setuptools

# with open('README.md', 'r') as fh:
#     long_description = fh.read()

setuptools.setup(
    name="dbks",
    version="0.0.1",
    author="Vincent Lam",
    author_email="vincent@lam.is",
    description="Databricks API client",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/vincentlam/dbks",
    packages=setuptools.find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
