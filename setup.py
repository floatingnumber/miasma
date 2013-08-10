#!/usr/bin/env python

from distutils.core import setup

readme_md_file = open('README.md', 'r')

setup(
	name = 'miasma',
	version = '0.0.1',
        packages = ['miasma'],
	scripts = ['scripts/miasma'],
	description = 'Binary file editor',
	author = 'Mario Mercaldi',
	author_email = 'mario.mercaldi@gmail.com',
	url = 'https://www.github.com/batteryshark/miasma',
	keywords = ['binary', 'reverse engineering'],
	classifiers = [
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Intended Audience :: Developers',
		'Operating System :: Windows NT / UNIX',
	],
	long_description = readme_md_file.read()
)
readme_md_file.close()
