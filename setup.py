import os
from setuptools import setup, find_packages

setup(
    name='centipede',
    version='0.1',
    description="Document processing system",
    long_description="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    keywords='',
    author='Marcos Vanetta, Friedrich Lindenberg',
    author_email='',
    url='http://opennews.org',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points={
    },
    tests_require=[]
)
