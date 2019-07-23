#!/bin/bash

JSPKGS=js-*

for jspkg in $JSPKGS
do
    pkgfullpath=`pwd`$jspkg
    PYTHONPATH=$PYTHONPATH:$pkgfullpath
done

pdoc3 jumpscale --html --output-dir docs/api --overwrite