from setuptools import setup
from singularity_pipeline import __version__

setup(
    name='singularity-pipeline',
    version=__version__,
    description='A runner script for pipelines using Singularity containers',
    url='https://github.com/kav2k/singularity-pipeline',
    author='Alexander Kashev',
    author_email='alexander.kashev@math.unibe.ch',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ],
    keywords='singularity container runner',
    packages=['singularity_pipeline'],
    install_requires=['PyYAML>=3.12', 'argparse>=1.4.0', 'colorama>=0.3'],
    entry_points={
        'console_scripts': [
            'singularity-pipeline = singularity_pipeline.__main__:__main'
        ]
    }
)
