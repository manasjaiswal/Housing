from setuptools import setup,find_packages
from typing import List

def get_requirements_list()->List[str]:
    with open('requirements.txt') as req_file:
        return req_file.readlines().remove("-e .)

PROJECT_NAME="housing-predictor"
AUTHOR="ManasJaiswal"
Description="This is a first project based on CI/CD pipelines"

setup(
name=PROJECT_NAME,
author=AUTHOR,
description=Description,
packages=find_packages(),
install_requires=get_requirements_list()

)
