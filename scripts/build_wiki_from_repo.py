#!/usr/bin/python3

"""
	Copyright 2016 Diego Rossi (@_HellPie)

	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at

		http://www.apache.org/licenses/LICENSE-2.0

	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.
"""

import argparse
import filecmp
import os
import shutil

parser = argparse.ArgumentParser(description='Build script to generate GiHub Wiki from the docs.')
parser.add_argument('repository', help='The path where the git wiki for this project is')
repo = parser.parse_args().repository

if not os.path.isfile(repo + '/.git/config'):
	quit('Error: No git repository found in provided \'{}\'.'.format(repo))

with open(repo + '/.git/config') as repo_config:
	found_it = False
	for line in repo_config:
		if 'url = https://github.com/HellPie/mcpe-json-docs.wiki.git' in line:
			found_it = True
	if not found_it:
		quit('Error: The given git repo is not compatible with the required Wiki.')

changes = list()
docs_files = list()

print('\nAnalyzing docs pages...\n')
for listed_file in os.listdir(os.path.abspath('../docs')):
	listed_file = '../docs/' + listed_file
	if not os.path.isfile(os.path.abspath(listed_file)):
		print('Not a file: {}'.format(listed_file))
		continue

	print('Processing \'{}\'...'.format(os.path.basename(listed_file)))
	with open(listed_file) as repo_page:
		wiki_page_name = 'Unknown Page'
		for line in repo_page:
			if '# ' in line and '## ' not in line:
				newline = line.split('# ')
				wiki_page_name = newline[len(newline) - 1].replace('\n', '')
				print('\tFound title: \'{}\''.format(wiki_page_name))
				break

		wiki_page = os.path.abspath(repo + '/' + wiki_page_name + '.md')

		print('\tChecking compatibility...')
		if os.path.exists(wiki_page):
			if filecmp.cmp(listed_file, wiki_page):
				print('Skipped already existing file: \'{}\'\n'.format(os.path.abspath(listed_file)))
				continue
			file_changed = True
			print('\nWARNING: \'{}\' is already in \'{}\''.format(wiki_page_name, wiki_page))
			answer = input('DO YOU WANT TO OVERWRITE \'{}\'? [y/N]: '.format(wiki_page_name))
			if answer.lower() is not 'y':
				print('Aborted overwrite of \'{}\'\n'.format(wiki_page_name))
				continue
			else:
				print('')
		else:
			file_changed = False

		print('\tCloning file into \'{}\''.format(wiki_page))
		shutil.copy(listed_file, wiki_page)
		print('Done: \'{}\' -> \'{}\'\n'.format(listed_file, wiki_page))

		docs_files.append(os.path.abspath(wiki_page))
		if file_changed:
			changes.append('- Changed "{}"'.format(wiki_page_name))
		else:
			changes.append('- Added "{}"'.format(wiki_page_name))

print('\nAnalyzing removed pages...\n')
for listed_file in os.listdir(repo):
	if os.path.abspath(listed_file) not in docs_files and os.path.isfile(listed_file):
		file_name = os.path.basename(listed_file)
		print('Mismatch in wiki: \'{}\' was removed from docs.'.format(file_name))
		answer = input('WARNING: DO YOU WANT TO REMOVE \'{}\'? [y/N]: '.format(file_name))
		if answer.lower() is not 'y':
			print('Aborted removal of \'{}\''.format(file_name))
			continue
		else:
			os.remove(os.path.abspath(listed_file))
			print('Removed \'{}\''.format(os.path.abspath(listed_file)))
			changes.append('- Removed "{}"'.format(file_name.split('.')[0]))

print('\nDone generating wiki.\n')

changes.sort()

print('Changelog:')
for line in changes:
	print(line)

quit('')
