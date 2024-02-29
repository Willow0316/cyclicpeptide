from setuptools import setup, find_packages

setup(
    name='cyclicpeptide',
    version='0.1',
    packages=find_packages(),
    description='A simple example package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='http://github.com/yourusername/my_package',
    author='Your Name',
    author_email='your.email@example.com',
    python_requires='>=3.8',  # Python 版本要求
    license='MIT',
    install_requires=[
        'ipython>=8.12.3',
        'matplotlib>=3.7.5',
        'networkx>=3.1',
        'numpy>=1.24.4',
        'pandas>=2.0.3',
        'rdkit>=2023.9.5',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ]
)