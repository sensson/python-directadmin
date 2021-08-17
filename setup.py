from setuptools import setup

setup(name='directadmin-client',
      version='0.0.1',
      description='A Python interface to the DirectAdmin API',
      url='https://github.com/sensson/python-directadmin',
      author='Sensson',
      author_email='info@sensson.net',
      packages=['directadmin'],
      install_requires=[
          'requests',
          'simplejson',
      ],
      zip_safe=False)
