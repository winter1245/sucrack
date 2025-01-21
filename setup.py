from setuptools import setup
setup(name='sucrack',
      version='1.0',
      py_modules=['sucrack'],
      install_requires=['pexpect'],
      entry_points={"console_scripts": ["sucrack=sucrack.main:main"]},
      )
