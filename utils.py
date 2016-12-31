#!/usr/bin/python3

import os
import sys
import subprocess
import platform
from string import Template
from collections import namedtuple

FILE_DIR = os.path.dirname(os.path.realpath(__file__))
ACCOUNT_NAME = 'sphawk'

Command = namedtuple('Command', ['path', 'command', 'stop_if_failed'])

def get_options(bits):
    """get options for run. bits means 32bit or 64bit"""
    options = {
        # tools
        'GIT':'git', 
        'PERL':'perl',
        'MSBUILD':'msbuild',
        'NASM':'nasm',
        'GCC':'gcc',
        'G++':'g++',
        # checkout versions
        'ACE_VERSION':'master',
        'OPENSSL_VERSION':'OpenSSL_1_0_2-stable',
        'ZLIB_VERSION':'master',
        # origin (my own repository, forked from upstream)
        'ATCD_ORIGIN':'https://github.com/{0}/ACE_TAO.git'.format(ACCOUNT_NAME),
        'OPENSSL_ORIGIN':'https://github.com/{0}/openssl.git'.format(ACCOUNT_NAME),
        'ZLIB_ORIGIN':'https://github.com/{0}/zlib.git'.format(ACCOUNT_NAME),
        # upstream
        'ATCD_UPSTREAM':'https://github.com/DOCGroup/ACE_TAO.git',
        'MPC_UPSTREAM':'https://github.com/DOCGroup/MPC.git',
        'OPENSSL_UPSTREAM':'https://github.com/openssl/openssl.git',
        'ZLIB_UPSTREAM':'https://github.com/madler/zlib.git',    
        # base location
        'CURRENT':FILE_DIR,
        'SOURCE':os.path.join(FILE_DIR, 'source'),
        # source location
        'ACE_SRC':os.path.join(FILE_DIR, 'source', 'ACE_TAO'),
        'ACE_ROOT':os.path.join(FILE_DIR, 'source', 'ACE_TAO', 'ACE'),
        'TAO_ROOT':os.path.join(FILE_DIR, 'source', 'ACE_TAO', 'TAO'),
        'MPC_ROOT':os.path.join(FILE_DIR, 'source', 'MPC'),
        'OPENSSL_SRC':os.path.join(FILE_DIR, 'source', 'openssl'),
        'ZLIB_SRC':os.path.join(FILE_DIR, 'source', 'zlib'),    
    }

    if '32bit' == bits:
        # destination location
        options['LIBRARY']=os.path.join(FILE_DIR, 'lib32'),
        options['ACE_DST']=os.path.join(FILE_DIR, 'lib32', 'ace'),
        options['OPENSSL_DST']=os.path.join(FILE_DIR, 'lib32', 'openssl'),
        options['ZLIB_DST']=os.path.join(FILE_DIR, 'lib32', 'zlib'),
    elif '64bit' == bits:
        # destination location
        options['LIBRARY']=os.path.join(FILE_DIR, 'lib64'),
        options['ACE_DST']=os.path.join(FILE_DIR, 'lib64', 'ace'),
        options['OPENSSL_DST']=os.path.join(FILE_DIR, 'lib64', 'openssl'),
        options['ZLIB_DST']=os.path.join(FILE_DIR, 'lib64', 'zlib'),
    else:
        # bits required when build
        pass

    system = platform.system()
    if 'Windows' == system:
        options['MKDIR']='mkdir'
        options['RMDIR']='rmdir /s /q'
        options['COPY']='copy /y /b'
        options['MAKE']='nmake'
    elif 'Linux' == system:
        options['MKDIR']='mkdir -p'
        options['RMDIR']='rm -rf'
        options['MAKE']='make'
    else:
        raise Exception("unknown system! {0}".format(system))

    return options

def run(commands, options, env = None):
    for item in commands:
        cmd = Template(item.command).substitute(options)
        if item.path is not None:
            path = Template(item.path).substitute(options)
            print(os.path.join(path, cmd))
        else:
            path = None
            print(cmd)

        ret = subprocess.call(cmd, cwd=path, env=env, shell=True)
        if 0 != ret and item.stop_if_failed:
            raise Exception("process failed, return code {0}".format(ret))
