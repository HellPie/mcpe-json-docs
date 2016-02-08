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

import argparse
import os


def setup_args(desc: str = 'Utility scripts to manage JSON files in MC: PE/W10/EDU.') -> str:
	parser = argparse.ArgumentParser(description=desc)
	parser.add_argument('assets', help='Minecraft: Pocket Edition\'s assets folder path')
	assets = parser.parse_args().assets
	if os.path.isdir(assets) and os.path.isfile(assets + '/ui/_ui_defs.json'):
		return assets
	else:
		quit('Error: \'{}\' is not a valid MC:PE assets dir.'.format(assets))


def get_clean_json(file: str = None) -> str:
	if file is None or file is '':
		quit('Error: Unable to clean JSON because no file was specified.')
	elif not os.path.isfile(file):
		quit('Error: Unable to clean JSON in \'{}\' because it is not a valid JSON file.')
	else:
		final_json = ''
		with open(file) as json:
			cutting = False
			for line in json:
				if '/*' in line and not cutting:
					cutting = True
					if '*/\n' in line:
						cutting = False
				elif '//' in line and not cutting and 'http://' not in line:
					final_json += line.split('//')[0] + '\n'
				elif '*/\n' in line and cutting:
					cutting = False
				elif not cutting:
					final_json += line
		return final_json
