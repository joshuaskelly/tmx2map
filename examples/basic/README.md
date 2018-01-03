# Basic tmx2map Example

## Prequisites
1. [Tiled](http://www.mapeditor.org/)
2. [Quake](http://store.steampowered.com/app/2310/QUAKE/)
3. [Quake BSP Compiler](https://ericwa.github.io/ericw-tools/)
4. tmx2map

## Setup
Note: The example directory and Quake directory are referred to as `basic/` and `QUAKE/` respectively.

1. Copy `basic/` somewhere to your hard drive.
2. Copy `basic/wads/basic.wad` to `QUAKE/id1/wads/basic.wad`
3. Copy `tmx2map` to `basic/` (or optionally put it on your PATH).

## Workflow
tmx2map is intended to work alongside your existing Quake mapping workflow. It helps with the map authoring process and produces a Quake .map file. From there it can be edited, compiled, and lit to your liking.

### Example Workflow
Note: The example directory and Quake directory are referred to as `basic/` and `QUAKE/` respectively.

1. Edit `basic/basic.tmx` with Tiled.
2. From `basic/` run: `tmx2map basic.tmx mapping.json -d maps/example.map`
3. Copy `basic/maps/example.map` to `QUAKE/id1/maps/example.map`
4. From `QUAKE/id1/maps` run: `qbsp example.map`
5. From `QUAKE/` run: `quake +map example`
