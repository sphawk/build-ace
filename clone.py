#!/usr/bin/python3

# build ace, openssl, zlib

from utils import Command, get_options, run

options = get_options(None)
commands = [ 
    Command(None, '${MKDIR} ${SOURCE}', False),
    Command(None, '${MKDIR} ${LIBRARY}', False),
    Command('${SOURCE}', '${GIT} clone --depth 1 ${ATCD_UPSTREAM} ${ACE_SRC}', True),
    Command('${SOURCE}', '${GIT} clone ${OPENSSL_UPSTREAM} ${OPENSSL_SRC}', True),
    Command('${SOURCE}', '${GIT} clone --depth 1 ${ZLIB_UPSTREAM} ${ZLIB_SRC}', True),
    Command('${SOURCE}', '${GIT} clone --depth 1 ${MPC_UPSTREAM} ${MPC_ROOT}', True),
]

run(commands, options)
