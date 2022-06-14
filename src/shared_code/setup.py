from setuptools import setup, find_packages

setup(
    name="lib_hello",
    version="0.1",
    description="Minimal sample Python module",
    url="file:///.",
    author="",
    maintainer="",
    install_requires=[
        "autopep8",
    ],
    author_email="",
    package_dir={'': 'src'},
    packages=['lib_hello'],
    zip_safe=False,
)
