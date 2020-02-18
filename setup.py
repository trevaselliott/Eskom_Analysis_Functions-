from setuptools import setup, find_packages

setup(
    name = 'mypackage',
    vesion = '0,1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA Eskom Project',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<mokgobukatlego7-hub>/<mypackage>',
    author='<Mokgobu Katlego>',
    author_email='<mokgobukatlego7@gmail.com>'
)