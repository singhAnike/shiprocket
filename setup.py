from setuptools import setup, find_packages

with open('README.md') as readme:
    readme_content = readme.read()

setup(
    name="internal_pip_package",
    version="1.0.1",
    description="This is the python client for the razorpayx and shiprocket",
    long_description=readme_content,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    author="Team Fatmug Design",
    # license="MIT",
    keywords="python client for the internal uses of the raxorpayx and shiprocket",
    include_package_data=True,
    # package_dir={'internal_pip_package': 'internal_pip_package', 'internal_pip_package.razorpayx':'internal_pip_package/razorpayx' ,'internal_pip_package.razorpayx.resources': 'internal_pip_package/razorpayx/resources', 'internal_pip_package.shiprocket': 'internal_pip_package/shiprocket' ,'internal_pip_package.shiprocket.resources': 'internal_pip_package/shiprocket/resources', 'internal_pip_package.razorpayx.constants':'internal_pip_package/razorpayx/constants'},
    # packages=['internal_pip_package', 'internal_pip_package.razorpayx', 'internal_pip_package.razorpayx.resources',  'internal_pip_package.shiprocket', 'internal_pip_package.shiprocket.resources', 'internal_pip_package.razorpayx.constants'],
    install_requires=[
    'razorpay==1.4.2',
    'cachetools==5.2.1',
    
],
package_data={
        'internal_pip_package.razorpayx': ['ca-bundle.crt'],  
    }

   
)
