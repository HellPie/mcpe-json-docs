# Special Keys

Special keys are JSON keys that are only used in certain, specific, unique locations in the `.json` files.
So far only two keys are implemented in the MC:PE JSON Format:
- [`namespace`](#namespace)
- [`ui_defs`](#ui-defs)

## ui_defs:
The `ui_defs` key seems to only appear in `_ui_defs.json` file and only be expected there.
It is a `JSON array` containing the paths, as a `string`, of the other `.json` files to load.

## namespace:
The `namespace` is a key of type `string`, found once in each `.json` file, as its first key. It represents the namespace to where the key should be applied.

The `namespace` key **MUST be defined at the top of the file**, as first key in it, as the parser scrolls through the file searching for that specific key before reading the other objects

So far the known, meaningful namespaces are:
- `anvil`
- `brewing_stand`
- `chest`
- `common`
- `common-classic`
- `crafting`
- `enchanting`
- `furnace`
- `gamepad_layout`
- `language_choice`
- `pauseTrial`
- `play`
- `pocket_redstone`
- `redstone`
- `start`
- `test`
- `trialUpsell`
- `xbl_login`

Some of this namespaces are dependent on the version of Minecraft that's being ran: `xbl_login` is for example only used in the Windows 10 Edition.

The only `namespace` that is so far confirmed to be unused in MC:PE's code is `test`.
