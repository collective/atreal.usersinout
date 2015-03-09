from setuptools import find_packages
from setuptools import setup

version = '1.2.2'

setup(
    name='atreal.usersinout',
    version=version,
    description="Import / export users via CSV files",
    long_description="%s%s" % (
        open("README.rst").read(),
        "\n",
        open("CHANGES.rst").read()
    ),
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='zope plone atreal users import export csv',
    author='atReal',
    author_email='contact@atreal.net',
    url='http://www.atreal.net',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['atreal'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
