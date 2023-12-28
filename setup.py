from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    library_needed = f.read().splitlines()

setup(
    name='ai',
    version='0.0.1',
    python_requires='>=3',
    install_requires=library_needed,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ai = script.ai:cli',
        ]
    }
)
