@echo off

pushd source

pushd ATCD
git fetch upstream
git checkout master
git merge upstream/master
git push origin master
popd

pushd ATCD\ACE\MPC
git merge origin/master
popd

pushd openssl
git fetch upstream
git checkout master
git merge upstream/master
git push origin master
popd

pushd zlib
git fetch upstream
git checkout master
git merge upstream/master
git push origin master
popd

popd