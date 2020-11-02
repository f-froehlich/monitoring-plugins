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

from monitoring_utils.PageContent import PageContent

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check Page Content')

    parser.add_argument('-w', '--warning-content', dest='warningcontent', action='append', default=[],
                        help='Warning content. Return warning state if at least one matched and no Critical content match')
    parser.add_argument('-c', '--critical-content', dest='criticalcontent', action='append', default=[],
                        help='Critical content. Return critical state if at least one matched')
    parser.add_argument('-o', '--ok-content', dest='okcontent', action='append', default=[],
                        help='OK content. Return OK state if at least one matched and no warning or critical content match')
    parser.add_argument('-H', '--header', dest='header', action='append', default=[],
                        help='Header for request. Format: NAME=VALUE')
    parser.add_argument('-u', '--uri', dest='uri', type=str, help='URI to fetch', default='/')
    parser.add_argument('-d', '--domain', dest='domain', type=str, help='Domain to fetch', required=True)
    parser.add_argument('-p', '--port', dest='port', type=int, help='Port to fetch')
    parser.add_argument('-s', '--ssl', dest='ssl', help='Use https', action='store_true')
    parser.add_argument('--client-cert', dest='clientcert', type=str, help='Path to client certificate')
    parser.add_argument('--client-key', dest='clientkey', type=str, help='Path to client certificate key file')

    args = parser.parse_args()
    PageContent(
        ok_content=args.okcontent,
        warning_content=args.warningcontent,
        critical_content=args.criticalcontent,
        uri=args.uri,
        domain=args.domain,
        port=args.port,
        ssl=args.ssl,
        header=args.header,
        client_key=args.clientkey,
        clinet_cert=args.clientcert,
    ).main()
