from setuptools import setup

package = "pycassos"
version = "0.0.1"

setup(name = package,
      version = version,
      description="Python Caviar Solutions Software suite",
      url='https://github.com/dicaso/pycassos',
      author = 'Christophe Van Neste',
      author_email = 'christophe.vanneste@ugent.be',
      license = 'MIT',
      packages = ['pycassos'],
      python_requires='>3.6',
      install_requires = [
          # dicaso packages
          'leopard',
          'genairics',
          'bidali[retro]',
          'pyni',
          # console packages
          'ipython',
          # server packages
          'flask',
          'flask-login',
          'flask-jsonpify',
          'flask-mongoengine',
          #'flask-sqlalchemy',
          'flask-restful',
          'mpld3'
      ],
      extras_require = {
          'development': ['twine','Sphinx']
      },
      package_data = {
      },
      include_package_data = True,
      zip_safe = False,
      entry_points = {
          'console_scripts': ['pycassos=pycassos.__main__:main'],
      },
      test_suite = 'nose.collector',
      tests_require = ['nose']
)

#To install with symlink, so that changes are immediately available:
#pip install -e .
