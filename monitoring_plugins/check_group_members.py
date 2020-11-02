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

from monitoring_utils.GroupMembers import GroupMembers

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check group members')

    parser.add_argument('-g', '--group', dest='group', default='sudo', help='Group to check the members')
    parser.add_argument('-u', '--user', dest='users', action='append', default=[], help='User, who should be in group')

    args = parser.parse_args()
    GroupMembers(args.group, args.users).main()