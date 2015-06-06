@echo off

set MPC_TEMP_WORKER=%~dp0\temp\ace
set ACE_ROOT=%~dp0\source\ATCD\ACE

rmdir /s /q "%MPC_TEMP_WORKER%"
mkdir "%MPC_TEMP_WORKER%"

pushd source\ATCD\ACE
bin\mwc.pl -type vc12 -features "qos=1,ssl=1,zlib=1" -value_template "multiprocessorcompilation=true" ace\ACE.mwc
bin\mwc.pl -type vc12 -features "qos=1,ssl=1,zlib=1" -static -name_modifier *_Static -value_template "multiprocessorcompilation=true" ace\ACE.mwc
bin\mwc.pl -type vc12 -features "qos=1,ssl=1,zlib=1" -workers 4 -workers_dir "%MPC_TEMP_WORKER%" -value_template "multiprocessorcompilation=true" examples\examples.mwc
bin\mwc.pl -type vc12 -features "qos=1,ssl=1,zlib=1" -static -name_modifier *_Static -workers 16 -workers_dir "%MPC_TEMP_WORKER%" -value_template "multiprocessorcompilation=true" examples\examples.mwc
bin\mwc.pl -type vc12 -features "qos=1,ssl=1,zlib=1" -workers 4 -workers_dir "%MPC_TEMP_WORKER%" -value_template "multiprocessorcompilation=true" tests\tests.mwc
bin\mwc.pl -type vc12 -features "qos=1,ssl=1,zlib=1" -static -name_modifier *_Static -workers 16 -workers_dir "%MPC_TEMP_WORKER%" -value_template "multiprocessorcompilation=true" tests\tests.mwc

echo #include "config-win32.h" > ace\config.h
rmdir /s /q "%MPC_TEMP_WORKER%"
popd