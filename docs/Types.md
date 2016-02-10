# Types

> **Warning**:
> This doc page also talks about `C++`!

These are all the `C++` objects MC:PE generates from the `JSON` keys:
- [control's name](#Control-name)
- [control's tree](#Control-tree)
- [`AnimatedProperty`](#AnimatedProperty)
- [`Binding`](#Binding)
- [`ClipDirection`](#ClipDirection)
- [`ClipOffset`](#ClipOffset)
- [`Color`](#Color)
- [`Draggable`](#Draggable)
- [`FontSize`](#FontSize)
- [`GridRescalingType`](#GridRescalingType)
- [`GridSize`](#GridSize)
- [`LayoutAxis`](#LayoutAxis)
- [`LayoutOffset`](#LayoutOffset)
- [`PropertyBag`](#PropertyBag)
- [`SliceSize`](#SliceSize)
- [`UV`](#UV)
- [`UVSize`](#UVSize)

## Control name:
A control's name resolves a control. (See `UIControl::_registerControlNameResolver` in MC:PE's code)

## Control tree:
(See `UIControlFactory::createControlTree` in MC:PE's code)

## AnimatedProperty:
(See `AnimatedProperty<T>` in MC:PE's code)

## Binding:
Bindings can be defined of four types:
- `global` (0 in MC:PE's code)
- `collection` (1 in MC:PE's code)
- `collection_details` (2 in MC:PE's code)
- `view` (4 in MC:PE's code)

Bindings are `JSON` objects named under the `bindings` tag, they have various sub-properties, like:
- `binding_collection`
- `binding_condition`
- `binding_name`
- `binding_name_override`

All these keys take a `variable` name, of type `string`, except for `binding_condition`, which can be one of:
- `none` (0 in MC:PE's code)
- `once` (1 in MC:PE's code)
- `visible` (2 in MC:PE's code)

## ClipDirection:
The C++ object `ClipDirection` can assume 5 main values, all `string`, in the JSON files:
- `center`
- `down`
- `left`
- `right`
- `up`

## ClipOffset:
The C++ object `ClipOffset` is represented in the JSON files as a `[float, float]` array.

## Color:
The C++ object `Color` is represented in the JSON files as a `[float, float, float, float]` array (most likely as `ARGB`).

## Draggable:
The draggability of an object is defined using the `draggable` key, which can assume any of these values:
- `not_draggable` (0 in MC:PE's code)
- `horizontal` (1 in MC:PE's code)
- `vertical` (2 in MC:PE's code)
- `both` (3 in MC:PE's code)

## FontSize:
The C++ object `FontSize` can only have value `small` in the JSON files, if defined.

## GridRescalingType:
The C++ object `GridRescalingType` is defined by the `grid_rescaling_type` key in the JSON files and can assume any of this values:
- `horizontal` (0 in MC:PE's code)
- `vertical` (1 in MC:PE's code)
- `none` (2 in MC:PE's code)

## GridSize:
The C++ object `GridSize` is represented in the JSON files as a `[int, int]` array.

## LayoutAxis:
The C++ object 'LayoutAxis' is represented in the JSON files as either a `float` or as a `string`, as in `"100%"`, `"50px"` or even `"100%-50px"`.
It can also be set to `"x"` or `"y"`, or sizes relatives to the other axis, for example, in the case of the LayoutAxis for X: `"50%y"`.

## LayoutOffset:
This object can be defined as an array of two [`LayoutAxis`](#LayoutAxis)

## PropertyBag:
The C++ object `PropertyBag` is a JSON object defined by the `property_bag` key in an element, it can contain different, customizable keys that will later be transformed into `variables`.

## SliceSize:
The C++ object `SliceSize` can be defined as either a `[float, float, float, float]` array or just a `float`.

## UV:
The C++ object `UV` can be defined as a `[float, float]` array and it is used to define at which coordinates in a `texture` the element's graphics starts.

## UVSize:
The C++ object `UVSize` is represented as a `[float, float]` array, distinguished by the `uv_size` key in an element. It represents the size of the element's graphic in the specified `texture` key, starting from the [`uv`](#UV) key's defined offset.
