from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='rer.groupware.star',
      version=version,
      description="The RER Groupware suite",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Programming Language :: Python",
        ],
      keywords='plone plonegov groupware rer',
      author='RedTurtle Technology',
      author_email='sviluppoplone@redturtle.it',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      namespace_packages=['rer', 'rer.groupware'],
      include_package_data=True,
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      zip_safe=False,
      install_requires=[
          'setuptools',
          'rer.groupware.room',
          'rer.groupware.security',
          'rer.groupware.workflow',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
