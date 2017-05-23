from setuptools import setup

dependencies = ['pytest', 'pytest-cov']
extra_packages = {
    'testing': ['tox']
}

setup(
    name='mailroom',
    description="""Auto generate thank you letters""",
    version='0.1',
    author='Elyanil Liranzo-Castro, Carlos Cadena',
    author_email="yanil3500@gmail.com, cs.cadena@gmail.com",
    license="MIT",
    py_modules=['mailroom'],
    package_dir={'': 'src'},
    install_requires=dependencies,
    extras_require=extra_packages,
    entry_points={'console_scripts': ['mailroom = mailroom:thank_or_report']}
      )
