from setuptools import find_packages, setup
from typing import List

hyphen = '-e .'
def get_requirements(file:str)->List[str] :
    """ 
    Do not be afraid, this function just takes the requirements.txt file
    and edits and removes the next line tags and other extra unnecessary things
    
    """
    requirements = []
    with open(file) as file_obj:
        requirements = file_obj.readlines()
        requirements=[reqs.replace('\n',"") for reqs in requirements]
        if hyphen in requirements:
            requirements.remove(hyphen)
    return requirements

# Now the below code just simple information, and last two line are finding and installing packages
# DO NOT BE INTIMIDATED BY ANYHTING!!!
# REMEMBER THE ROOSEVELT LINE- "Only thing we have to fear, is fear itself"
setup(
    name='mlp',
    version='0.0.1',
    author='Kanu',
    author_email='madhuramacharya26@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)
