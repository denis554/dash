from setuptools import setup

setup(
    name='dash.ly',
    version='0.12.0',
    author='chris p',
    author_email='chris@plot.ly',
    packages=['dash', 'dash/development'],
    license='MIT',
    description='',
    long_description=open('README.md').read(),
    install_requires=['flask', 'plotly', 'flask-cors']
)
