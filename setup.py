from setuptools import setup


classifiers = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

install_requires = []
setup_requires = []
test_require = []

setup(
    name='python-social-auth-exr',
    version='0.1.0',
    author='Sviatoslav Bulbakha',
    author_email='mail@ssbb.me',
    url='https://github.com/ssbb/python-social-auth-exr/',
    description='EXR backend for python-social-auth (PSA)',
    license='MIT',
    classifiers=classifiers,
    packages=['psa_exr'],
    setup_requires=setup_requires,
    install_requires=install_requires,
    test_require=test_require,
)
