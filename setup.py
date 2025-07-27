from setuptools import setup, find_packages

setup(
    name='imop_lcs',
    version='1.0.0',
    description='First known general-purpose LCS optimizer using Index Mapping + Ordered Projection (IMOP) and LIS',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Dongjoon Kim (keithape73)',
    author_email='keithape73@gmail.com',  
    url='https://github.com/keithape73/IMOP_LCS',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
    python_requires='>=3.6',
)
