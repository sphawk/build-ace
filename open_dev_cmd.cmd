@echo off

if defined VS140COMNTOOLS goto VS140
if defined VS120COMNTOOLS goto VS120
if defined VS110COMNTOOLS goto VS110
if defined VS100COMNTOOLS goto VS100
if defined VS90COMNTOOLS goto VS90
if defined VS80COMNTOOLS goto VS80

echo cannot find visual studio.
goto EXIT

:VS140
call "%VS140COMNTOOLS%\..\..\VC\vcvarsall.bat" x86_amd64
goto EXIT

:VS120
call "%VS120COMNTOOLS%\..\..\VC\vcvarsall.bat" x86_amd64
goto EXIT

:VS110
echo VS110
call "%VS110COMNTOOLS%\..\..\VC\vcvarsall.bat" x86_amd64
goto EXIT

:VS100
call "%VS100COMNTOOLS%\..\..\VC\vcvarsall.bat" x86_amd64
goto EXIT

:VS90
call "%VS90COMNTOOLS%\..\..\VC\vcvarsall.bat" x86_amd64
goto EXIT

:VS80
call "%VS80COMNTOOLS%\..\..\VC\vcvarsall.bat" x86_amd64
goto EXIT

:EXIT
pushd %1
