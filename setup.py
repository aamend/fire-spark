import setuptools
from setuptools import find_packages

setuptools.setup(
    name='firespark',
    version='1.0',
    author='Antoine Amend',
    author_email='antoine.amend@gmail.com',
    description='Mapping fire model into spark operations',
    long_description_content_type='text/markdown',
    url='https://github.com/aamend/fire-spark',
    packages=find_packages(where=".", include=["fire"]),
    extras_require=dict(tests=["pytest"]),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
)