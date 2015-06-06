@echo off

pushd source\zlib
nmake -f win32/Makefile.msc AS=ml64 LOC="-DASMV -DASMINF -I." OBJA="inffasx64.obj gvmat64.obj inffas8664.obj"
nmake -f win32/Makefile.msc test
nmake -f win32/Makefile.msc testdll
popd

set ZLIB_ROOT=%~dp0\library\zlib
set ZLIB_SRC=%~dp0\source\zlib

@mkdir %ZLIB_ROOT%\include
@mkdir %ZLIB_ROOT%\lib

xcopy /y /q %ZLIB_SRC%\zconf.h %ZLIB_ROOT%\include\
xcopy /y /q %ZLIB_SRC%\zlib.h  %ZLIB_ROOT%\include\
xcopy /y /q %ZLIB_SRC%\zlib.pdb %ZLIB_ROOT%\lib\
xcopy /y /q %ZLIB_SRC%\zlib.lib %ZLIB_ROOT%\lib\

