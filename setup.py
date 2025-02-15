#!/usr/bin/env python3
from setuptools import setup

PLUGIN_ENTRY_POINT = 'ovos-phal-mk1=ovos_PHAL_plugin_mk1:MycroftMark1'
setup(
    name='ovos-PHAL-plugin-mk1',
    version='0.0.1a3',
    description='A PHAL plugin for mycroft',
    url='https://github.com/OpenVoiceOS/ovos-PHAL-plugin-mk1',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    packages=['ovos_PHAL_plugin_mk1'],
    install_requires=["ovos-plugin-manager>=0.0.24a2",
                      "ovos-bus-client",
                      "pyserial~=3.0"],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={'ovos.plugin.phal': PLUGIN_ENTRY_POINT}
)
