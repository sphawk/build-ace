#!/usr/bin/python3

# sync local and origin from upstream. 
# following convention from https://github.com/DOCGroup/ACE_TAO/blob/master/README.md
#
# local : repository on my local hdd
# origin : GitHub repository on my account. forked from upstream
# upstream : GitHub repository 

from utils import Command, get_options, run

options = get_options(None)
commands = [ 
    Command('${ACE_SRC}', '${GIT} remote rm upstream', False),
    Command('${ACE_SRC}', '${GIT} remote rm origin', False),
    Command('${ACE_SRC}', '${GIT} remote add upstream ${ATCD_UPSTREAM}', False),
    Command('${ACE_SRC}', '${GIT} remote add origin ${ATCD_ORIGIN}', False),
    Command('${OPENSSL_SRC}', '${GIT} remote rm upstream', False),
    Command('${OPENSSL_SRC}', '${GIT} remote rm origin ', False),
    Command('${OPENSSL_SRC}', '${GIT} remote add upstream ${OPENSSL_UPSTREAM}', False),
    Command('${OPENSSL_SRC}', '${GIT} remote add origin ${OPENSSL_ORIGIN}', False),
    Command('${ZLIB_SRC}', '${GIT} remote rm upstream', False),
    Command('${ZLIB_SRC}', '${GIT} remote rm origin', False),
    Command('${ZLIB_SRC}', '${GIT} remote add upstream ${ZLIB_UPSTREAM}', False),
    Command('${ZLIB_SRC}', '${GIT} remote add origin ${ZLIB_ORIGIN}', False),
    Command('${ACE_SRC}', '${GIT} fetch --tags upstream', False),
    Command('${ACE_SRC}', '${GIT} checkout master', False),
    Command('${ACE_SRC}', '${GIT} merge upstream/master', False),
    Command('${ACE_SRC}', '${GIT} push --tags --force origin master', False),
    Command('${OPENSSL_SRC}', '${GIT} fetch --tags upstream', False),
    Command('${OPENSSL_SRC}', '${GIT} checkout master', False),
    Command('${OPENSSL_SRC}', '${GIT} merge upstream/master', False),
    Command('${OPENSSL_SRC}', '${GIT} push --tags --force origin master', False),
    Command('${ZLIB_SRC}', '${GIT} fetch --tags upstream', False),
    Command('${ZLIB_SRC}', '${GIT} checkout master', False),
    Command('${ZLIB_SRC}', '${GIT} merge upstream/master', False),
    Command('${ZLIB_SRC}', '${GIT} push --tags --force origin master', False),
]

run(commands, options)