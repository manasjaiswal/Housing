from setuptools import setup
from typing import List

def get_requirements_list()->List[str]:
    with open('requirements.txt') as req_file:
        return req_file.readlines()

PROJECT_NAME="housing-predictor"
AUTHOR="ManasJaiswal"
Description="This is a first project based on CI/CD pipelines"
Packages=["Housing"]

setup(
name=PROJECT_NAME,
author=AUTHOR,
description=Description,
packages=Packages,
install_requires=get_requirements_list()

)
