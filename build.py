#!/usr/bin/python3

# build ace, openssl, zlib

import os
import sys
import platform
from os.path import join as pjoin
from utils import Command, get_options, run

def check_prerequisite():
    options = get_options(None)
    commands = []

    system = platform.system()
    if 'Windows' == system:
        commands.extend([
            Command(None, '${GIT} --version', True),
            Command(None, '${PERL} --version', True),
            Command(None, '${MSBUILD} /version', True),
            Command(None, '${MAKE} /?', True),
            Command(None, '${NASM} -v', True),
        ])
    elif 'Linux' == system:
        commands.extend([
            Command(None, '${GIT} --version', True),
            Command(None, '${PERL} --version', True),
            Command(None, '${GCC} --version', True),
            Command(None, '${G++} --version', True),
            Command(None, '${MAKE} --version', True),
        ])
        pass
    else:
        raise Exception('unknown platform {0}, cannot build!'.format(system))
   
    run(commands, options)


def build_zlib(bits):
    options = get_options(bits)
    commands = [ 
        Command('${ZLIB_SRC}', '${GIT} checkout ${ZLIB_VERSION}', True),
    ]
    system = platform.system()
    if 'Windows' == system:
        if '32bit' == bits:
            commands.append(Command('${ZLIB_SRC}', '${MAKE} -f win32/Makefile.msc LOC="-DASMV -DASMINF" OBJA="inffas32.obj match686.obj"', True))
        elif '64bit' == bits:
            commands.append(Command('${ZLIB_SRC}', '${MAKE} -f win32/Makefile.msc AS=ml64 LOC="-DASMV -DASMINF -I." OBJA="inffasx64.obj gvmat64.obj inffas8664.obj"', True))
        else:
            raise Exception("unknown bits! {0}".format(bits))
        commands.extend([
            Command(None, '${RMDIR} ${ZLIB_ROOT}/include', False),
            Command(None, '${RMDIR} ${ZLIB_ROOT}/lib', False),
            Command(None, '${RMDIR} ${ZLIB_ROOT}/bin', False),
            Command(None, '${MKDIR} ${ZLIB_ROOT}/include/zlib', False),
            Command(None, '${MKDIR} ${ZLIB_ROOT}/lib', False),
            Command(None, '${MKDIR} ${ZLIB_ROOT}/bin', False),
            Command(None, '${COPY} ${ZLIB_SRC}/zconf.h ${ZLIB_ROOT}/include/zlib', True),
            Command(None, '${COPY} ${ZLIB_SRC}/zlib.h  ${ZLIB_ROOT}/include/zlib', True),
            Command(None, '${COPY} ${ZLIB_SRC}/zlib.lib  ${ZLIB_ROOT}/lib', True),
            Command(None, '${COPY} ${ZLIB_SRC}/zlib.map  ${ZLIB_ROOT}/lib', True),
            Command(None, '${COPY} ${ZLIB_SRC}/zlib.pdb  ${ZLIB_ROOT}/lib', True),
            Command(None, '${COPY} ${ZLIB_SRC}/zdll.exp  ${ZLIB_ROOT}/lib', True),
            Command(None, '${COPY} ${ZLIB_SRC}/zdll.lib  ${ZLIB_ROOT}/lib', True),
            Command(None, '${COPY} ${ZLIB_SRC}/zlib1.dll ${ZLIB_ROOT}/bin', True),
            Command(None, '${COPY} ${ZLIB_SRC}/zlib1.pdb ${ZLIB_ROOT}/bin', True),
        ])
    elif 'Linux' == system:
        if '32bit' == bits:
            cflags = 'CFLAGS="-m32"'
        elif '64bit' == bits:
            cflags = 'CFLAGS="-m64"'
        else:
            raise Exception("unknown bits! {0}".format(bits))
        commands.extend([
            Command('${ZLIB_SRC}', '${RMDIR} ${ZLIB_ROOT}', False),
            Command('${ZLIB_SRC}', '{0} ./configure --prefix=${ZLIB_ROOT}'.format(cflags), True),
            Command('${ZLIB_SRC}', '${MAKE}', True),
            Command('${ZLIB_SRC}', '${MAKE} install', True),
        ])
    else:
        raise Exception('unknown platform {0}, cannot build!'.format(system))

    run(commands, options)

def build_openssl_102(bits):
    options = get_options(bits)
    commands = [
        Command('${OPENSSL_SRC}', '${GIT} checkout ${OPENSSL_VERSION}', True),
    ]

    system = platform.system()
    if 'Windows' == system:
        if '32bit' == bits:
            commands.extend([
                Command('${OPENSSL_SRC}', '${PERL} Configure VC-WIN32 --prefix="${OPENSSL_DST}" enable-static-engine', True),
                Command('${OPENSSL_SRC}', 'ms/do_nasm.bat', True),
            ])            
        elif '64bit' == bits:
            commands.extend([
                Command('${OPENSSL_SRC}', '${PERL} Configure VC-WIN64A --prefix="${OPENSSL_DST}" enable-static-engine', True),
                Command('${OPENSSL_SRC}', 'ms/do_win64a.bat', True),
            ])
        else:
            raise Exception("unknown bits! {0}".format(bits))
        commands.extend([
            Command('${OPENSSL_SRC}', '${MAKE} -f ms/nt.mak clean', True),
            Command('${OPENSSL_SRC}', '${MAKE} -f ms/ntdll.mak clean', True),
            Command('${OPENSSL_SRC}', '${MAKE} -f ms/nt.mak', True),
            Command('${OPENSSL_SRC}', '${MAKE} -f ms/ntdll.mak', True),
            Command(None, '${MKDIR} ${OPENSSL_DST}/bin', False),
            Command(None, '${MKDIR} ${OPENSSL_DST}/lib', False),
            Command(None, '${MKDIR} ${OPENSSL_DST}/include/openssl', False),
            Command('${OPENSSL_SRC}', '${MAKE} -f ms/ntdll.mak install', True),
            Command(None, '${COPY} ${OPENSSL_SRC}/out32dll/ssleay32.pdb ${OPENSSL_DST}/bin', True),
            Command(None, '${COPY} ${OPENSSL_SRC}/out32dll/libeay32.pdb ${OPENSSL_DST}/bin', True),
            Command(None, '${COPY} ${OPENSSL_SRC}/out32dll/openssl.pdb ${OPENSSL_DST}/bin', True),
            Command(None, '${COPY} ${OPENSSL_SRC}/out32dll/ssleay32.exp ${OPENSSL_DST}/lib', True),
            Command(None, '${COPY} ${OPENSSL_SRC}/out32dll/libeay32.exp ${OPENSSL_DST}/lib', True),
            Command(None, '${COPY} ${OPENSSL_SRC}/out32/ssleay32.lib ${OPENSSL_DST}/lib/ssleay32s.lib', True),
            Command(None, '${COPY} ${OPENSSL_SRC}/out32/libeay32.lib ${OPENSSL_DST}/lib/libeay32s.lib', True),
        ])        
    elif 'Linux' == system:
        if '32bit' == bits:
            arch = 'i386'
            bits = '-m32'
        elif '64bit' == bits:
            arch = 'x86_64'
            bits = '-m64'
        else:
            raise Exception("unknown bits! {0}".format(bits))            
        commands.extend([
            Command('${OPENSSL_SRC}', '${RMDIR} ${OPENSSL_ROOT}', False),
            Command('${OPENSSL_SRC}', 'setarch {0} ./config {1} shared --prefix=${OPENSSL_ROOT}'.format(arch, bits), True),
            Command('${OPENSSL_SRC}', '${MAKE} clean', True),
            Command('${OPENSSL_SRC}', '${MAKE}', True),
            Command('${OPENSSL_SRC}', '${MAKE} install', True),
        ])
    else:
        raise Exception('unknown platform {0}, cannot build!'.format(system))

    run(commands, options)

def build_ace(bits, build_examples = False, build_tests = False):
    options = get_options(bits)
    envs = {
        'ACE_ROOT':options.get('ACE_ROOT'),
        'SSL_ROOT':options.get('OPENSSL_ROOT'),
        'ZLIB_ROOT':options.get('ZLIB_ROOT'),
        'MPC_ROOT':options.get('MPC_ROOT'),
        'PATH':os.environ['PATH'] + os.pathsep + pjoin(options.get('ACE_ROOT'), 'lib'),
    }

    commands = [ 
        Command('${ACE_SRC}', '${GIT} checkout ${ACE_VERSION}', True),
    ]

    system = platform.system()
    if 'Windows' == system:
        
        options['ACE_CONFIGURE_OPTION'] = '-type vc14 -features "qos=1,ssl=1,zlib=1" -genins -value_template "multiprocessorcompilation=true"'
        options['ACE_CONFIGURE_STATIC'] = '-static -name_modifier *_Static'
        
        if '32bit' == bits:
            options['ACE_PLATFORM'] = 'Win32'
        elif '64bit' == bits:
            options['ACE_PLATFORM'] = 'x64'
        else:
            raise Exception("unknown bits! {0}".format(bits))            

        commands.extend([
            Command('${ACE_ROOT}', 'echo #include "config-win32.h" > ace/config.h', True),
            Command('${ACE_ROOT}', '${PERL} bin/mwc.pl ${ACE_CONFIGURE_OPTION} "${ACE_ROOT}/ace/ACE.mwc"', True),
            Command('${ACE_ROOT}', '${PERL} bin/mwc.pl ${ACE_CONFIGURE_OPTION} ${ACE_CONFIGURE_STATIC} "${ACE_ROOT}/ace/ACE.mwc"', True),
            Command('${ACE_ROOT}', '${MSBUILD} /p:Configuration=Debug /p:Platform=${ACE_PLATFORM} /t:Build /maxcpucount "${ACE_ROOT}/ace/ACE.sln"', True),
            Command('${ACE_ROOT}', '${MSBUILD} /p:Configuration=Release /p:Platform=${ACE_PLATFORM} /t:Build /maxcpucount "${ACE_ROOT}/ace/ACE.sln"', True),
            Command('${ACE_ROOT}', '${MSBUILD} /p:Configuration=Debug /p:Platform=${ACE_PLATFORM} /t:Build /maxcpucount "${ACE_ROOT}/ace/ACE_Static.sln"', True),
            Command('${ACE_ROOT}', '${MSBUILD} /p:Configuration=Release /p:Platform=${ACE_PLATFORM} /t:Build /maxcpucount "${ACE_ROOT}/ace/ACE_Static.sln"', True),            
            Command(None, '${RMDIR} ${ACE_DST}', False),
            Command(None, '${MKDIR} ${ACE_DST}/lib', False),
            Command(None, '${MKDIR} ${ACE_DST}/bin', False),
            Command('${ACE_ROOT}', '${PERL} ${MPC_ROOT}/prj_install.pl ${ACE_DST}/include ace', True),
            Command('${ACE_ROOT}', '${COPY} ./lib/*.lib ${ACE_DST}/lib', True),
            Command('${ACE_ROOT}', '${COPY} ./lib/dll ${ACE_DST}/bin', True),
            Command('${ACE_ROOT}', '${COPY} ./lib/*.pdb ${ACE_DST}/bin', True),
        ])

        if build_examples:
            commands.extend([
                Command('${ACE_ROOT}', '${PERL} bin/mwc.pl ${ACE_CONFIGURE_OPTION} examples/examples.mwc', True),
                Command('${ACE_ROOT}', '${PERL} bin/mwc.pl ${ACE_CONFIGURE_OPTION} ${ACE_CONFIGURE_STATIC} examples/examples.mwc', True),
                Command('${ACE_ROOT}', '${MSBUILD} /p:Configuration=Debug /p:Platform=${ACE_PLATFORM} /t:Build /maxcpucount examples/examples.sln', True),
                Command('${ACE_ROOT}', '${MSBUILD} /p:Configuration=Release /p:Platform=${ACE_PLATFORM} /t:Build /maxcpucount examples/examples.sln', True),
                Command('${ACE_ROOT}', '${MSBUILD} /p:Configuration=Debug /p:Platform=${ACE_PLATFORM} /t:Build /maxcpucount examples/examples_Static.sln', True),
                Command('${ACE_ROOT}', '${MSBUILD} /p:Configuration=Release /p:Platform=${ACE_PLATFORM} /t:Build /maxcpucount examples/examples_Static.sln', True),
            ])

        if build_tests:
            commands.extend([
                Command('${ACE_ROOT}', '${PERL} bin/mwc.pl ${ACE_CONFIGURE_OPTION} tests/tests.mwc', True),
                Command('${ACE_ROOT}', '${PERL} bin/mwc.pl ${ACE_CONFIGURE_OPTION} ${ACE_CONFIGURE_STATIC} tests/tests.mwc', True),
                Command('${ACE_ROOT}', '${MSBUILD} /p:Configuration=Debug /p:Platform=${ACE_PLATFORM} /t:Build /maxcpucount tests/tests.sln', True),
                Command('${ACE_ROOT}', '${MSBUILD} /p:Configuration=Release /p:Platform=${ACE_PLATFORM} /t:Build /maxcpucount tests/tests.sln', True),
                Command('${ACE_ROOT}', '${MSBUILD} /p:Configuration=Debug /p:Platform=${ACE_PLATFORM} /t:Build /maxcpucount tests/tests_Static.sln', True),
                Command('${ACE_ROOT}', '${MSBUILD} /p:Configuration=Release /p:Platform=${ACE_PLATFORM} /t:Build /maxcpucount tests/tests_Static.sln', True),
                Command('${ACE_ROOT}/tests', '${PERL} run_test.pl', True),
            ])

    elif 'Linux' == system:



        
        pass
    else:
        raise Exception('unknown platform {0}, cannot build!'.format(system))

    run(commands, options, envs)

check_prerequisite()
#build_zlib('32bit')
#build_zlib('64bit')
#build_openssl_102('32bit')
#build_openssl_102('64bit')
#build_ace('32bit')
#build_ace('64bit')
