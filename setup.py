from setuptools import setup
setup(
        name='sucrack',
        version='1.0',
        install_requires=['pexpect'],
        entry_points={"console_scripts": ["sucrack=sucrack.main:main"]},
        url="https://github.com/winter1245/sucrack",
      )
