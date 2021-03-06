#!/usr/bin/env python
# Copyright (c) 2015 Sudarshan Acharya
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages
import pkg_resources
import sys

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='osprofiler',
    version='0.1',
    description='OpenStack Profiler Agent',
    packages=find_packages(),
    include_package_data=True,
    license='Apache 2.0',
    #install_requires=required,
    keywords='openstack agent profiler')
