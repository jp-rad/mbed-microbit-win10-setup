from setuptools import setup, find_packages

setup(
    name="mbedubitwin10",
	version="1.0.0",
    author='jp-rad',
    author_email='jp.rad@outlook.jp',
    license='MIT',
    packages=find_packages(),
    package_data={'': ['*.patch']},
    entry_points={
        'console_scripts': [
            'mbedubitwin10=mbedubitwin10:main',
        ],
    },
    install_requires=[
        'patch',
        'jsonschema',
        'pyelftools',
    ]
)