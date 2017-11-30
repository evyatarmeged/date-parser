from setuptools import setup

setup(
    name='date_parser',
    packages=['date_parser'],
    license='MIT',
    version='0.1',
    description='Parse different date strings into YYYY-MM-DD format',
    author='Evyatar Meged',
    author_email='evyatarmeged@gmail.com',
    url='https://github.com/evyatarmeged/date_parser',
    keywords=['date', 'parsing', 'strings'],
    classifiers=['Programming Language :: Python :: 3'],
    install_requires=['python-dateutil>=2.6.0'],
    python_requires='>=3'
)
