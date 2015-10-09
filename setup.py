from setuptools import setup

VERSION = '0.1'


setup(
    name='home-generator',
    version=VERSION,
    py_modules=['gen_home_dir'],
    entry_points={
        'console_scripts': [
            'gen_home_dir = gen_home_dir:run'
        ]
    },
    install_requires=[
        'Flask',
        'tornado',
    ],
)
