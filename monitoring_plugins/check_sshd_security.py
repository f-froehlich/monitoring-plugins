#!/usr/bin/python3
# -*- coding: utf-8

#  monitoring-plugins
#
#  monitoring-plugins are the check plugins for monitoring
#
#  Copyright (c) 2020 Fabian Fröhlich <mail@confgen.org> https://icinga2.confgen.org
#
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  For all license terms see README.md and LICENSE Files in root directory of this Project.

import argparse

from monitoring_utils.SSHDSecurity import SSHDSecurity

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check sshd config')

    parser.add_argument('-r', '--permit-root-login', dest='permitrootlogin',
                        choices=['yes', 'no', 'without-password', 'forced-commands-only'], default='no',
                        help='Permit root login')
    parser.add_argument('-k', '--public-key-auth', dest='pubkeyauthentication', choices=['yes', 'no'], default='yes',
                        help='Public key authentication')
    parser.add_argument('-P', '--password-auth', dest='passwordauthentication', choices=['yes', 'no'], default='no',
                        help='Password authentication')
    parser.add_argument('--permit-empty-passwords', dest='permitemptypasswords', choices=['yes', 'no'], default='no',
                        help='Permit empty passwords')
    parser.add_argument('-H', '--fingerprint-hash', dest='fingerprinthash', default='SHA256',
                        help='Fingerprint Hash function')
    parser.add_argument('-p', '--port', dest='port', type=int, default=22, help='Listen port')
    parser.add_argument('-C', '--config', dest='config', action='append', default=[],
                        help='Other config values to check. Format: OPTION=VALUE_1|VALUE_2|...|VALUE_N')

    args = parser.parse_args()
    SSHDSecurity(
        permitrootlogin=args.permitrootlogin,
        pubkeyauthentication=args.pubkeyauthentication,
        passwordauthentication=args.passwordauthentication,
        permitemptypasswords=args.permitemptypasswords,
        fingerprinthash=args.fingerprinthash,
        port=args.port,
        config=args.config
    ).main()
