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

from monitoring_utils.UFWStatus import UFWStatus

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check ufw status and rules')

    parser.add_argument('-s', '--status', dest='status', default='active',
                        help='Status of ufw')
    parser.add_argument('--warn-inactive', dest='warninactive', default='on',
                        help='Warn on inactive UFW')
    parser.add_argument('-l', '--logging', dest='logging', default='on',
                        help='Status of logging')
    parser.add_argument('-L', '--logging-policy', dest='loggingpolicy',
                        default='low', help='Status of logging level')
    parser.add_argument('-I', '--in', dest='incoming', default='deny',
                        help='Default incoming policy')
    parser.add_argument('-O', '--out', dest='outgoing',
                        default='allow', help='Default outgoing policy')
    parser.add_argument('-R', '--routing', dest='routing',
                        default='disabled', help='Default routing policy')
    parser.add_argument('-r', '--rule', dest='rule', action='append',
                        help='Firewall rule from,to,action', default=[])

    args = parser.parse_args()

    UFWStatus(
        args.status,
        args.warninactive,
        args.logging,
        args.loggingpolicy,
        args.incoming,
        args.outgoing,
        args.routing,
        args.rule
    ).main()
