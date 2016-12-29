build-ace
==================

build script for ace/openssl/zlib

### default version
* ace: master
* zlib: master
* openssl: 1.0.2-stable

## Windows

### Pre-requisites
* Visual Studio 2015 Community Edition
* [git](http://git-scm.com/), use recent version (must support shallow clone)
* [perl](http://www.activestate.com/activeperl), for build OpenSSL
* do not use space in directory name
* add PATH variable for git, perl

### Usage
go to build-ace directory, input command below
```
nmake -f build_ace.msc clone zlib-install openssl-install ace-install
```

## Linux

### Pre-requisites
* gcc/g++
* perl
* git

### Usage
go to build-ace directory, input command below
```
make -f build_ace.linux clone zlib-install openssl-install ace-install
```
