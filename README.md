# xrcat

This is a small package for getting resources from Xresources. It can be used as a python module or as a CLI tool.

## Usage

In the command line:

```
$ xrcat "dwm.background"
#1d2021
```

As a python module:

```
from xrcat import xrcat

# Load current resources into xrcat
xrcat.updateResources()

# Get the resource
print(xrcat.getResource("dwm.background"))
# Output: '#1d2021'
```

## Wildcards

xrcat also supports wildcards matching. This means that if you for example want `dwm.background` and the value is None, xrcat will match it to `*.background`. Matches are prioritized based on length so for the example above `*.background` will be choosen instead of `*background` even though both are matches. This behavior is implemented to ensure that program specific resources are selected before general resources.

## Contributing

I am very new to making packages, so if you know anything that needs polishing or fixing, I am all ears. All help appreciated!

## License

This project is under the GNU General Public License v3 (GPLv3) - See LICENSE for details
