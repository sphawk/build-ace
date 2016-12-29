#!/usr/bin/python3

# sync local and myself from origin
import os
import subprocess
from string import Template
from collections import namedtuple

Command = namedtuple('Command', ['path', 'command'])
FILE_DIR = os.path.dirname(os.path.realpath(__file__))
ACCOUNT_NAME = 'sphawk'

param = dict(GIT='git', 
    ATCD_MYSELF='https://github.com/{0}/ACE_TAO.git'.format(ACCOUNT_NAME),
    OPENSSL_MYSELF='https://github.com/{0}/openssl.git'.format(ACCOUNT_NAME),
    ZLIB_MYSELF='https://github.com/{0}/zlib.git'.format(ACCOUNT_NAME),
    ACE_SRC=os.path.join(FILE_DIR, 'source', 'ACE_TAO'),
    OPENSSL_SRC=os.path.join(FILE_DIR, 'source', 'openssl'),
    ZLIB_SRC=os.path.join(FILE_DIR, 'source', 'zlib'),
)

commands = [ 
    Command('${ACE_SRC}', '${GIT} remote add myself ${ATCD_MYSELF}'),
    Command('${OPENSSL_SRC}', '${GIT} remote add myself ${OPENSSL_MYSELF}'),
    Command('${ZLIB_SRC}', '${GIT} remote add myself ${ZLIB_MYSELF}'),
    Command('${ACE_SRC}', '${GIT} fetch --tags origin'),
    Command('${ACE_SRC}', '${GIT} checkout master'),
    Command('${ACE_SRC}', '${GIT} merge origin/master'),
    Command('${ACE_SRC}', '${GIT} push --tags --force myself master'),
    Command('${ACE_SRC}/ACE/MPC', '${GIT} fetch --tags origin'),
    Command('${ACE_SRC}/ACE/MPC', '${GIT} checkout master'),
    Command('${ACE_SRC}/ACE/MPC', '${GIT} merge origin/master'),
    Command('${OPENSSL_SRC}', '${GIT} fetch --tags origin'),
    Command('${OPENSSL_SRC}', '${GIT} checkout master'),
    Command('${OPENSSL_SRC}', '${GIT} merge origin/master'),
    Command('${OPENSSL_SRC}', '${GIT} push --tags --force myself master'),
    Command('${ZLIB_SRC}', '${GIT} fetch --tags origin'),
    Command('${ZLIB_SRC}', '${GIT} checkout master'),
    Command('${ZLIB_SRC}', '${GIT} merge origin/master'),
    Command('${ZLIB_SRC}', '${GIT} push --tags --force myself master'),
]

for item in commands:
    cmd = Template(item.command).substitute(param)
    path = Template(item.path).substitute(param)
    print(os.path.join(path, cmd))
    subprocess.call(cmd, cwd=path)
