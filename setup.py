from setuptools import find_packages, setup
from typing import List

hyphen = '-e .'
def get_requirements(file:str)->List[str] :
    requirements = []
    with open(file) as file_obj:
        requirements = file_obj.readlines()
        requirements=[reqs.replace('\n',"") for reqs in requirements]
        if hyphen in requirements:
            requirements.remove(hyphen)
    return requirements

setup(
    name='mlp',
    version='0.0.1',
    author='Kanu',
    author_email='madhuramacharya26@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')

)