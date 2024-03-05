from setuptools import find_packages, setup
from typing import List

HYPHEN_E = "-e ." 
def get_requirements(file_path:str)->List[str]:
    requirements= []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E in requirements:
            requirements.remove(HYPHEN_E)

    return requirements


setup(
    name ="Mlproject",
    version = "0.0.1",
    author = "Ankush",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)