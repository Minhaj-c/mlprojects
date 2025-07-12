from setuptools import find_packages,setup
from typing import List

hyphen_e='-e .'

def get_requirments(file_path:str)->List[str]:
    requirments=[]
    with open(file_path) as obj_file:
        requirments=obj_file.readlines()
        requirments=[req.replace("\n","") for req in requirments]
        
        if hyphen_e in requirments:
            requirments.remove(hyphen_e)
    
    return requirments        
    

setup(
    name='mlproject',
    version='0.0.1',
    author='Minhaj',
    author_email='minhajc415@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments('requirments.txt')
    
)