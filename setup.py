import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='cowexcept',
    version='1.2.2',
    author='James Finnie-Ansley',
    description='Spice up those exceptions with cowexcept!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/James-Ansley/cowexcept',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Topic :: Utilities',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=setuptools.find_packages(
        where='src',
    ),
    package_dir={'': 'src'},
    python_requires='>=3.8',
    install_requires=[
        'python-cowsay',
    ],
)
