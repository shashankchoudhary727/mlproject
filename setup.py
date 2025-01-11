from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
# To fix the warning, we need to specify the packages explicitly
def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.1',
    author='Shashank',
    author_email='shashankchoudhry727@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=get_requirements('requirements.txt'),
)