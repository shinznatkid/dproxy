from setuptools import setup, find_packages

version = '0.1.0'

packages = find_packages()

setup(
    name='dproxy',
    version=version,
    description='A simple Django proxy for the Django framework.',
    author='Shinz Natkid',
    author_email='shinznatkid@gmail.com',
    url='http://django-proxy.readthedocs.org/',
    packages=find_packages(),
    install_requires=[
        'Django>=1.1',
        'requests>=0.1',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
