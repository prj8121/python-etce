#
# Copyright (c) 2017 - Adjacent Link LLC, Bridgewater, New Jersey
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in
#   the documentation and/or other materials provided with the
#   distribution.
# * Neither the name of Adjacent Link LLC nor the names of its
#   contributors may be used to endorse or promote products derived
#   from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#

import os
import re


class PseuedoTestDirectoryError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)


class PseudoTestDirectory(object):
    '''
    PseudoTestDirectory is used 
    '''
    def __init__(self, configfiledoc, nodename):
        self._configfile = configfiledoc
        self._nodename = nodename


    def name(self):
        return 'wrappertest'


    def nodename(self):
        return self._nodename


    def nodeid(self):
        regex = re.compile(r'(\d+)')

        match = regex.search(self._nodename)

        if match:
            return int(match.group(1))
        else:
            message = 'The wrapper tried to access a numeric ' \
                      'node ID, but the nodename "%s" does not ' \
                      'contain any numeral from which it can be ' \
                      'derived.' % self._nodename
            raise PseuedoTestDirectoryError(message)


    def getfile(self, name):
        for entry in os.listdir('.'):
            if entry == name:
                if os.path.isfile(entry):
                    return name

        print 'File "%s" not found.' % name
        
        return None


    def hasconfig(self, wrappername, paramname):
        return self._configfile.hasconfig(wrappername, paramname)


    def getconfig(self, wrappername, paramname, default):
        return self._configfile.getconfig(wrappername, paramname, default)
