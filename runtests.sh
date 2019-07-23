#!/bin/bash

JSPKGS=js-*

for jspkg in $JSPKGS
do
    pkgfullpath=`pwd`$jspkg
    PYTHONPATH=$PYTHONPATH:$pkgfullpath
done

echo "PYTHONPATH: $PYTHONPATH"
for jspkg in js-*
do
    echo $jspkg 
    pushd $jspkg
        echo "running tests for  $jspkg"
        pytest tests
    popd
done
