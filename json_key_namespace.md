# Namespace
The `namespace` is a key of type `string`, found once in each `.json` file, as its first key. It represents the namespace to where the key should be applied.

The `namespace` key **MUST be defined at the top of the file**, as first key in it, as the parser scrolls through the file searching for that specific key before reading the other objects

So far the known, valid, namespaces are:
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

Some of this namespaces are dependent on the version of Minecraft that's being ran: `xbl_login` is for example only used in the Windows 10 Editiion.

The only `namespace` that is so far confirmed to be unused in MC:PE is `test`.
