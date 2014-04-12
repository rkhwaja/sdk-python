from distutils.core import setup

setup(
    name='edmunds',
    version='0.1.2',
    author='Michael Bock',
    author_email='api@edmunds.com',
    packages=['edmunds'],
    url='https://github.com/EdmundsAPI/sdk-python',
    license='LICENSE',
    description='This is an awesome Python 2 wrapper for the Edmunds.com API.',
    long_description=open('README.md').read(),
    install_requires=[
        "requests>=0.8.6",
    ],
)
