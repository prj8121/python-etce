#
# Copyright (c) 2015-2018 - Adjacent Link LLC, Bridgewater, New Jersey
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


from etce.wrapper import Wrapper


class ARPCache(Wrapper):
    """
    The utils.arpcache wrapper populates the arp
    table based on the entries in the input file. 
    The input file takes 1 entry/line in format:

    <interface> <ipaddress> <ethaddress>

    For example: 

    emane0 172.30.1.2 02:02:00:00:00:02
    """

    def register(self, registrar):
        registrar.register_infile_name('arpcache.script')

        registrar.register_outfile_name('arpcache.log')


    def run(self, ctx):
        if not ctx.args.infile:
            return

        for line in open(ctx.args.infile):
            line = line.strip()

            if len(line) == 0:
                continue

            if line[0] == '#':
                continue
            
            interface,ipaddress,ethaddress = line.split()
            # arp -i emane0 -s 172.30.1.2 02:02:00:00:00:02

            argstr = '-i %s -s %s %s' % (interface, ipaddress, ethaddress)

            ctx.run('arp', argstr, genpidfile=False)

            
    def stop(self, ctx):
        pass
