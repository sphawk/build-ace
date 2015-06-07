build-ace
==================

build script for ace/openssl/zlib, for x64 windows

## Pre-requisites

* Visual Studio 2013 Community Edition
* ActivePerl (http://www.activestate.com/activeperl)
* Git (http://git-scm.com/)

* do not use space in directory name
* run from console commandline and check git, perl version (do not use cygwin perl or git...)

check below command runnable.

* git --version
* perl --version
* nmake
* msbuild

## Usage

go to build-ace directory, input command below

```
nmake -f build_ace.msc clone zlib-install openssl-install ace-install
```
