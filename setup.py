from setuptools import setup
import sys

# dependencies
reqs = ['python-dateutil', 'icalendar', 'requests', 'beautifulsoup4']
extras = {}

# oh yeah, python 3
if sys.version_info < (3,):
    sys.stderr.write("Python 3 is required\n")
    sys.exit(1)

# http://stackoverflow.com/a/7071358/735926
import re
VERSIONFILE = 'higdon.py'
verstrline = open(VERSIONFILE, 'rt').read()
VSRE = r'^__version__\s+=\s+[\'"]([^\'"]+)[\'"]'
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % VERSIONFILE)

with open('README.rst') as f:
    readme = f.read()

setup(name='higdon',
      version=verstr,
      description='Generate calendar files from Hal Higdon training plans.',
      long_description=readme,
      url='https://github.com/baldwint/higdon',
      author='Tom Baldwin',
      author_email='tbaldwin@uoregon.edu',
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Topic :: Utilities',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3 :: Only',
          'Programming Language :: Python :: 3.4',
      ],
      install_requires=reqs,
      extras_require=extras,
      py_modules=['higdon', ],
      entry_points = {
          'console_scripts': ['higdon=higdon:cli'],
      },
      )
