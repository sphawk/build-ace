@echo off

call clone_repository.bat
call sync_repository.bat
call build_openssl.bat
call build_zlib.bat
call make_ace_sln.bat
call build_ace.bat
