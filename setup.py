from setuptools import setup, find_packages

with open('README.md') as readme:
    readme_content = readme.read()

setup(
    name="Shiprocket-sdk",
    version="1.0.2",
    description="This is the python client for the shiprocket",
    long_description=readme_content,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    author="Aniket Singh",
    author_email="singh7509811123@gmail.com",  # Added author email
    url="https://github.com/singhAnike/shiprocket.git",  # Added project URL
    keywords="python client for the uses of the shiprocket",
    include_package_data=True,
    install_requires=[
        'cachetools==5.2.1',
    ],
)