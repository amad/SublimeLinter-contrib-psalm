SublimeLinter-contrib-psalm
================================

[![Build Status](https://travis-ci.org/amad/SublimeLinter-contrib-psalm.svg?branch=master)](https://travis-ci.org/amad/SublimeLinter-contrib-psalm)

![SublimeLinter-contrib-psalm screen shot](screenshot.png?raw=true)

This linter plugin for [SublimeLinter][docs] provides an interface to [vimeo/psalm][psalm].

### Linter configuration
In order for `psalm` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `psalm`, you can proceed to install the `SublimeLinter-contrib-psalm` plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

### Linter installation steps
Make sure [vimeo/psalm][psalm] is installed [globally][composer-global] and ensure composer bin directory is already pushed into PATH.

```
composer global req vimeo/psalm
```

> Note: In case you want to use the `vendor/bin` directory, you should update the linter configuration as well.

The psalm config file (`psalm.xml`) is required in the project's root directory.
You can create it using the following command:
```
psalm --init
```


## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.

Thank you for helping out!


[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
[psalm]: https://github.com/vimeo/psalm
[composer-global]: https://getcomposer.org/doc/03-cli.md#global
