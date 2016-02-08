Thanks to [**@MCMrARM**](https://github.com/MCMrARM) for providing these informations! :+1:

This is pretty much everything the code in MC:PE was able to reveal so far about the new JSON format used to define GUI elements in the game.
Popular behalf is that the JSON format is made using custom tools at Microsoft Studios, since it only started appearing after Microsoft bought Minecraft and assigned a new team of developers to the MC:PE Mojang team.
The idea this is made using custom graphical tools comes from the fact that the way the JSON format works is so bad, ugly and unreadable that nobody except a program coded by Microsoft could generate it.

### Special keys:
- `namespace`
- `ui_defs` (seems to be only allowed in `_ui_defs.json`, contains the list of .json files to load)

### Types:
| Type                   | Description                                                           |
| ---------------------- | --------------------------------------------------------------------- |
| `ClipOffset`           | Can be defined as a `[float, float]` array.                           |
| `PropertyBag`          | It is a JSON object.                                                  |
| `control name`         | Resolves a control (see: [`UIControl::_registerControlNameResolver`](#uicontrol_registercontentresolver).  |
| `Binding`              | See [`Bindings`](#bindings)                                           |
| `Draggable`            | See [`Draggable`](#draggable)                                         |
| `AnimatedProperty<T>`  |                                                                       |
| `LayoutOffset`         | Can be defined as an array of two LayoutAxis                          |
| `LayoutAxis`           | Can be defined as a `float`, but also as a `string` as in "100%", "100px", "100%-100px". It seems it can also be set to "x" or "y", but this need some verifications tho.  |


### Bindings:
##### Bindindable Properties:
- [`binding_type`](#binding-types)
- `binding_name`
- `binding_name_override`
- `binding_collection`
- [`binding_condition`](#binding-conditions)

##### Binding Types:
| binding_type  |                     |
| ------------- | ------------------- |
| `0`           | global              |
| `1`           | collection          |
| `2`           | collection_details  |
| `4`           | view                |

##### Binding Conditions:
| binding_condition  |         |
| ------------------ | ------- |
| `0`                | none    |
| `1`                | once    |
| `2`                | visible |

### Draggable:
| Value | Description    |
| ----- | -------------- |
| `0`   | not_draggable  |
| `1`   | horizontal     |
| `2`   | vertical       |
| `3`   | both           |

### Base properties:
##### `control`:
| Value             | Type                           |
| ----------------- | ------------------------------ |
| `visible`         | `bool`                         |
| `layer`           | `int`                          |
| `clips_children`  | `bool`                         |
| `clip_offset`     | [`ClipOffset`](#clipoffset)    |
| `allow_clipping`  | `bool`                         |
| `property_bag`    | [`PropertyBag`](#propertybag)  |

##### `button`:
| Value              | Type                           | State                                      |
| ------------------ | ------------------------------ | ------------------------------------------ |
| `default_control`  | [`control name`](#types)       | Default, just rendered on screen normally. |
| `hover_control`    | [`control name`](#types)       | Hovered, selected, not yet clicked.        |
| `pressed_control`  | [`control name`](#types)       | Pressed.                                   |

##### `dataBinding`:
| Value              | Type                           |
| ------------------ | ------------------------------ |
| `bindings`         | [`Binding`](#bindings)         |

### Allowed types (see [`defTypeFromString`](#defTypeFromString)):
| Type | Description                                                                                  |
| ---- | -------------------------------------------------------------------------------------------- |
| `0`  | [`button`](#button)                                                                          |
| `1`  | [`carousel_label`](#carousel_label)                                                          |
| `2`  | custom                                                                                       |
| `3`  | [`edit_box`](#edit_box)                                                                      |
| `4`  | [`grid`](#grid)                                                                              |
| `5`  | [`grid_item`](#grid_item)                                                                    |
| `6`  | [`image`](#image)                                                                            |
| `7`  | [`input_panel`](#input_panel)                                                                |
| `8`  | [`label`](#label)                                                                            |
| `9`  | [`panel`](#panel)                                                                            |
| `10` | [`screen`](#screen)                                                                          |
| `11` | [`scrollbar`](#scrollbar)                                                                    |
| `12` | [`scrollbar_box`](#scrollbar_box)                                                            |
| `13` | [`tab` (`control`, `button`, `dataBinding`, `input`, `layout`, `sound`, `component`)](#tab)  |
| `14` | no type                                                                                      |
