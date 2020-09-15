from setuptools import find_packages, setup


setup(
    name='jsonfield',
    version='1.0.0',
    license='MIT',
    include_package_data=True,
    author='W Innovation',
    author_email='innovation@webranking.it',
    maintainer='None',
    maintainer_email='',
    url='https://github.com/WRinnovation/django-jsonfield',
    description='Repo forked from https://bitbucket.org/schinckel/django-jsonfield/get/tip.zip because of unavailability',
    long_description='',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['Django'],
    python_requires='>=3.6',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ],
)
