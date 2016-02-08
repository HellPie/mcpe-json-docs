#!/usr/bin/python3

"""
	Copyright 2015 Diego Rossi (http://twitter.com/_HellPie)

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

import utils
import json

assets = utils.setup_args('Utility script to extract namespaces from MC: PE/W10/EDU JSON files.')

namespaces = list()

print('\nAnalyzing \'_ui_defs.json\'...\n')
ui_defs = json.loads(utils.get_clean_json(assets + 'ui/_ui_defs.json'))

for ui_file in ui_defs['ui_defs']:
	print('Analyzing \'{}\'...'.format(ui_file))
	ui_json = json.loads(utils.get_clean_json(assets + ui_file))
	namespaces.append(ui_json['namespace'])

print('\nRemoving duplicates...')
for ns in namespaces:
	i = namespaces.count(ns)
	while i > 1:
		namespaces.remove(ns)

print('\nReordering list...')
namespaces.sort()

print('\nGenerating Markdown:\n')
for ns in namespaces:
	print('- `{}`'.format(ns))

quit('')
