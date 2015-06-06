@echo off

SET ZLIB_ROOT=%~dp0\library\zlib
SET SSL_ROOT=%~dp0\library\openssl
SET ACE_ROOT=%~dp0\source\ATCD\ACE

echo ZLIB_ROOT : %ZLIB_ROOT%
echo SSL_ROOT : %SSL_ROOT%
echo ACE_ROOT : %ACE_ROOT%

pushd source\ATCD\ACE
msbuild /p:Configuration=Debug /p:Platform=x64 /t:Build /maxcpucount ace\ACE.sln
msbuild /p:Configuration=Release /p:Platform=x64 /t:Build /maxcpucount ace\ACE.sln 

msbuild /p:Configuration=Debug /p:Platform=x64 /t:Build /maxcpucount ace\ACE_Static.sln
msbuild /p:Configuration=Release /p:Platform=x64 /t:Build /maxcpucount ace\ACE_Static.sln

msbuild /p:Configuration=Debug /p:Platform=x64 /t:Build /maxcpucount tests\tests.sln
msbuild /p:Configuration=Debug /p:Platform=x64 /t:Build /maxcpucount examples\examples.sln

pushd tests
xcopy /q /y ..\lib\ACEd.* .\ 
run_test.pl
popd

popd