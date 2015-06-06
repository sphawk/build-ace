@echo off

@mkdir source
@mkdir library

pushd source

git clone https://github.com/sphawk/ATCD.git
git clone https://github.com/sphawk/openssl.git
git clone https://github.com/sphawk/zlib.git

pushd ATCD\ACE
git clone https://github.com/DOCGroup/MPC.git
popd

pushd ATCD
git remote add upstream https://github.com/DOCGroup/ATCD.git
popd

pushd openssl
git remote add upstream https://github.com/openssl/openssl.git
popd

pushd zlib
git remote add upstream https://github.com/madler/zlib.git
popd

popd