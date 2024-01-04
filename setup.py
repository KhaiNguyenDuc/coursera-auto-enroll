from setuptools import setup, find_packages

setup(
    name='coursera-auto-enroll',
    version='0.1.0',
    author='Nguyễn Đức Khải',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
