

set ACE_INSTALL_DIR=%~dp0\library\ace

rmdir /s /q "%ACE_INSTALL_DIR%"
mkdir "%ACE_INSTALL_DIR%"

pushd source\ATCD\ACE
mpc\prj_install.pl -a lib_output "%ACE_INSTALL_DIR%" ace
popd