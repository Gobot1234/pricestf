import re

import setuptools


with open('requirements.txt') as f:
    requirements = f.read().splitlines()
    f.close()

with open('pricestf/__init__.py') as f:
    version = re.search(r"""__version__ = (['"])(?P<version>(?:.*?))(['"])""", f.read(), re.MULTILINE).group('version')
    f.close()

with open('./README.md') as f:
    README = f.read()
    f.close()

setuptools.setup(
    author="Mark7888",
    author_email="l.mark7888@gmail.com",
    name='prices-tf',
    license="MIT",
    description="'A Python API for Nicklason's prices.tf site.'",
    version=version,
    long_description_content_type='text/markdown',
    long_description=README,
    url='https://github.com/Mark7888/pricestf',
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
