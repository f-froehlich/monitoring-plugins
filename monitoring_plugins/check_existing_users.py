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

from monitoring_utils.ExistingUsers import ExistingUsers

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check Users on the system')

    parser.add_argument('-m', '--uid-min', dest='minuid', default=-1, type=int, help='Minimum userid')
    parser.add_argument('-M', '--uid-max', dest='maxuid', default=-1, type=int, help='Maximum userid')
    parser.add_argument('-u', '--user', dest='users', action='append', default=[],
                        help='Normal not sudoer user. USERNAME')
    parser.add_argument('-S', '--filter-shell', dest='shellfilter', action='append', default=[],
                        help='Excluded list of shells')

    args = parser.parse_args()
    ExistingUsers(
        uid_min=args.minuid,
        uid_max=args.maxuid,
        users=args.users,
        shell_filter=args.shellfilter
    ).main()
