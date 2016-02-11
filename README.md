build-ace
==================

build script for ace/openssl/zlib

### Windows

## Pre-requisites
* Visual Studio 2015 Community Edition
* [perl](http://www.activestate.com/activeperl)
* [git](http://git-scm.com/)
* do not use space in directory name
* run from console commandline and check git, perl version (do not use cygwin perl or git...)

## Usage
go to build-ace directory, input command below
```
nmake -f build_ace.msc clone zlib-install openssl-install ace-install
```

### Linux

## Pre-requisites
* gcc/g++
* perl
* git

## Usage
go to build-ace directory, input command below
```
make -f build_ace.linux clone zlib-install openssl-install ace-install
```
