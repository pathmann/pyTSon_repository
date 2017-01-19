# pyTSon_repository

This is the "official" repository for [pyTSon's](https://github.com/pathmann/pyTSon) plugins.

How to add a script
-------------------
Just open a [pull request](https://github.com/pathmann/pyTSon_repository/compare) with your scriptfile and your metadata included in https://github.com/pathmann/pyTSon_repository/blob/master/repository.json. If you push something to this repository, your code has to be compatible with the GNU GPLv3.

URLs
-----
You may want to predict URLs from https://cdn.rawgit.com, if you are not sure about the tag, just use the current date (preferable in format yyyy-MM-dd) or simply come up with some cool name. But make sure, it is unique in https://github.com/pathmann/pyTSon_repository/tags.

Wanna keep it updated yourself?
--------------------------------
This repository is currently always included by default in every pyTSon installation, but users may add their own "local" repositories. Todo that, publish your repository.json and your scriptfiles online and spread your repository link.

JSON-Format
-----------
pyTSon will download your repository file including the meta data of your plugins. This file needs to contain a JSON string (and only that!), comprising a list of objects. An example can be found in [repository.json](https://github.com/pathmann/pyTSon_repository/blob/master/repository.json).

These objects need to contain at least the keys "name", "author", "version", "apiVersion", "description" and "url" (all string variables) describing your plugin.

The url can link either to a pythoncode file or a ZIP-package.

The keys "platforms" and "dependencies" are optional.

If present, the value of platforms has to be a list of strings, containing the supported platforms (possible values are "Mac", "Windows-32bit", "Windows-64bit", "Linux-32bit" and "Linux-64bit"). If the key platforms is not present, pyTSon will presume, that all platforms are supported.

If present, the value of dependencies is interpreted as object, which can contain a key for each platform (possible values are "Mac", "Windows-32bit", "Windows-64bit", "Linux-32bit" and "Linux-64bit"), whose value has to be a list of strings.
Each strings represents a python package name from the [Python Package Index](https://pypi.python.org/pypi) and will be installed automatically during the installation process. (The strings are directly processed with the local pip installation, so you can restrict a package to a version number: pip==9.0.1 would install pip in version 9.0.1)

