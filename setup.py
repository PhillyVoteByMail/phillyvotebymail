from setuptools import setup, find_packages

setup(
    name="pavotebymail", 
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pavotebymail=pavotebymail.cli:cli'
        ]
    }
)
