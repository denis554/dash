from setuptools import setup, find_packages

import io
exec(open('dash/version.py').read())

setup(
    name='dash',
    version=__version__,  # noqa: F821
    author='chris p',
    author_email='chris@plot.ly',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description=('A Python framework for building reactive web-apps. '
        'Developed by Plotly.'),
    long_description=io.open('README.md', encoding='utf-8').read(),
    install_requires=[
        'Flask>=0.12',
        'flask-compress',
        'plotly'
    ],
    url='https://plot.ly/dash',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Manufacturing',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Database :: Front-Ends',
        'Topic :: Office/Business :: Financial :: Spreadsheet',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Widget Sets'
    ]
)
