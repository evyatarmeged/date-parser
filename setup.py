from distutils.core import setup
setup(
  name='date-parser',
  packages=['date-parser'],  # this must be the same as the name above
  version='0.1',
  description='Parse different date strings into YYYY-MM-DD format',
  author='Evyatar Meged',
  author_email='evyatarmeged@gmail.com',
  url='https://github.com/evyatarmeged/date-parser',  # use the URL to the github repo
  download_url='https://github.com/peterldowns/mypackage/archive/0.1.tar.gz',  # I'll explain this in a second
  keywords=['testing', 'logging', 'example'],  # arbitrary keywords
  classifiers=[], requires=['python-dateutil']
)