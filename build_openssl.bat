@echo off

rem check using ActivePerl! (do not use strawberry perl!)

set OPENSSL_INSTALL_DIR=%~dp0\library\openssl
echo install openssl to %OPENSSL_INSTALL_DIR%

pushd source\openssl
git checkout OpenSSL_1_0_2a
perl Configure VC-WIN64A --prefix="%OPENSSL_INSTALL_DIR%"
call ms\do_win64a
nmake -f ms\ntdll.mak
nmake -f ms\ntdll.mak test
nmake -f ms\ntdll.mak install 
popd
