# Special Keys

Special keys are JSON keys that are only used in certain, specific, unique locations in the `.json` files.
So far only two keys are implemented in the MC:PE JSON Format:
- [`namespace`](json_key_namespace#Namespace)
- [`ui_defs`](#ui-defs)

## ui_defs:
The `ui_defs` key seems to only appear in `_ui_defs.json` file and only be expected there.
It is a `JSON array` containing the paths, as a `string`, of the other `.json` files to load.
