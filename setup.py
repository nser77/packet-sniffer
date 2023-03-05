import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    long_description = f.read()

setup(
    name="packet-sniffer",
    version="0.0.1",
    description="Pure Python packet sniffer for academic purposes that streams packets to message brokers.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords="packet-sniffer python",
    author="nser77",
    author_email="",
    python_requires=">=3.8.0",
    url="https://github.com/nser77/keepalived-wrapper",
    packages=find_packages(),
    install_requires=["redis[hiredis]"],
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
