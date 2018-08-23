from setuptools import setup, find_packages


setup(
    name="pdu_python_api",
    packages=find_packages(),
    package_data={'raritan': ['resources/*']},
    author='Neeba Chandy',
    author_email='nechandy@cisco.com',
    install_requires=[],
    # the following makes a plugin available to pytest
    # entry_points={
    #
    # },
    url="http://d3b2us605ptvk2.cloudfront.net/download/px2/version-3.0.4/pdu-json-rpc-sdk-030004-41800.tgz",
#    long_description=read('README.rst'),
    # custom PyPI classifier for pytest plugins
    classifiers=[
        "Framework :: Pytest",
    ],
)
