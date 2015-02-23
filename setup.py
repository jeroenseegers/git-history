import os

from setuptools import setup


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


setup(
    name='git-history',
    version='0.0.1',
    description='Keep a history of all your git commands.',
    long_description=(read('README.md')),
    url='http://github.com/jeroenseegers/git-history/',
    license='MIT',
    author='Jeroen Seegers',
    author_email='jeroen.seegers+githistory@gmail.com',
    py_modules=['git-history'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Version Control',
        'Topic :: Utilities',
    ],
    entry_points={
        'console_scripts': [
            'git-history = git_history:track_history',
        ]
    },
)
