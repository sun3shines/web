#!/usr/bin/python
# Copyright (c) 2012 Red Hat, Inc.
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

name = 'cloudweb'


setup(
    name=name,
    version='1.1',
    description='cloud console',
    license='xx',
    author='sss',
    author_email='zhu__feng014@163.com',
    url='https://org/',
    packages=find_packages(exclude=['test', 'bin']),
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6',
        'Environment :: No Input/Output (Daemon)',
        ],
    install_requires=[],  # removed for better compat
    scripts=[
        'bin/cloud-web-server',
        'bin/cloud-monitor-server',
    ],
    entry_points={
        'paste.app_factory': [
            'webserver = cloudserver.web-server:app_factory',
            'monitorserver = cloudserver.monitor-server:app_factory',
#            'object=cloud.swift.obj.server:app_factory',
#            'container=cloud.swift.container.server:app_factory',
#            'account=cloud.swift.account.server:app_factory',
            ],
#        'paste.filter_factory': [
#            'gluster=cloud.swift.common.middleware.cloud:filter_factory',
#            'direr = cloud.swift.direr.server:filter_factory',
#            'link = cloud.swift.link.server:filter_factory',
#            'slo = swift.common.middleware.slo:filter_factory',
#            'account_quotas = swift.common.middleware.account_quotas:filter_factory',
#            'batch = swift.common.middleware.batch:filter_factory',
#            'userinit = swift.common.middleware.userinit:filter_factory',
#            'apis = swift.common.middleware.apis:filter_factory',
#            'userop = swift.common.middleware.userop:filter_factory',
#
#            ],
        },
    )
