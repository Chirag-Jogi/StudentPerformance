from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requriements
    '''
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n","") for req in requirments]
        '''when we read the requirements the new line also it read
           replace it blank'''

        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)
    return requirments

        
setup(
name='mlproject',
version='0.0.1',
author='Chirag',
author_email='chiragjogi97@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')    
)