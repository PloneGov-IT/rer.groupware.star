from setuptools import setup, find_packages
import os

version = '2.0.1.dev0'

setup(name='rer.groupware.star',
      version=version,
      description="The RER Groupware suite",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 5.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
      ],
      keywords='plone plonegov groupware rer',
      author='RedTurtle Technology',
      author_email='sviluppoplone@redturtle.it',
      url='https://github.com/PloneGov-IT/rer.groupware.star',
      license='GPL',
      namespace_packages=['rer', 'rer.groupware'],
      include_package_data=True,
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      zip_safe=False,
      install_requires=[
          'setuptools',
          'rer.groupware.core',
          'rer.groupware.room',
          'rer.groupware.security',
          'rer.groupware.workflow',
          'rer.groupware.notify',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
