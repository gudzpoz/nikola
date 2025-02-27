#!/usr/bin/env python3

from nikola import nikola
n = nikola.Nikola()
n.init_plugins()

print(""".. title: Path Handlers for Nikola
.. slug: path-handlers
.. author: The Nikola Team

.. DO NOT EDIT, this file is auto-generated by scripts/document_path_handlers.py

Nikola supports special links with the syntax ``link://kind/name``. In
templates you can also use ``_link(kind, name)``. You can add query strings
(``?key=value``) for extra arguments, or pass keyword arguments to ``_link`` in
templates (support and behavior depends on path handlers themselves). By default,
you can only link to current language's contents; in order to link to a different
language, use ``link://kind/name?lang=other_lang`` or ``_link(kind, name, lang)``.
Fragments (``#anchor``) will be appended to the transformed link.

Here are the descriptions for all the supported kinds.

.. class:: dl-horizontal
""")

for k in sorted(n.path_handlers.keys()):
    v = n.path_handlers[k]
    print(k)
    print('\n'.join('    ' + l.strip() for l in v.__doc__.splitlines()))
    print()
