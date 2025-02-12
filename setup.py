from setuptools import setup
"""
This is a file that pip automatically looks for when installing a package and contains file data
"""
setup(name='DistributionPyPackage',
      version = '0.1',
      description = "contains gaussian distribution model",
      packages = ['DistributionPyPackage'],
      author = 'Nathan Shaw',
      zip_safe=False)#prevents package from being run in a zip file