import sys
from distutils.core import setup
from cx_Freeze import setup,Executable
import py2exe

setup(
    console=['Menu.py'],
    name='VacationDates',
    version='0.1',
    packages=[''],
    url='',
    license='ADNAP',
    author='Christian Farley',
    author_email='cfarley95@gmail.com',
    description='',
    executables = [Executable("Menu.py")],
)
