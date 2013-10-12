#!/usr/bin/python
# -*- coding: utf-8 -*-
# (c) 2013, Cristobal Rosa <cristobalrosa@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


DOCUMENTATION = '''
---
module: nmap
short_description: Runs NMAP using the given parameters.
description:
    - This module allows you to perform a port scans using the 
    given parameters. 
author: Cristobal Rosa <cristobalrosa@gmail.com>
requirements: ['python-nmap']
options:
    target:
        description: 
            Target on which you want to perform the  port scan.
        requiered: True
        default: Null
    ports:
        description:
            Port list you want to analyze
        required: False
        default: Null
    arguments:
        description:
            NMAP scan options. Read nmap doc for more information
        requiered: False
        default: "-sV"
'''

EXAMPLES = '''

# Scan version all hosts in the net
    -nmap: target=192.168.1.1/8
# Scan for a individual port
    -nmap: target=192.168.1.1 ports=80
# OS version detection
    -nmap: target=192.168.1.1/24 arguments=-A"
# Fast port scan
    -nmap: target=192.168.1.1/24 arguments=-T5
'''
NMAP_FOUND = True
try:
    import nmap
except ImportError:
    NMAP_FOUND = False

def main():
    # Default arguments: -sV.
    # Version Detection: http://nmap.org/book/man-version-detection.html
    module = AnsibleModule(
        argument_spec = dict(
            target =    dict(required = True,  default = None),
            ports =     dict(required = False,  default = None),
            arguments = dict(required = False, default = "-sV")
            )
        )
    if not NMAP_FOUND:
        module.fail_json("msg=NMAP module not found.NMPA module is requiered."
                " You can install it by running 'pip install python-nmap'")
    target = module.params['target']
    ports = module.params['ports']
    arguments = module.params['arguments']
    scanner = nmap.PortScanner()
    scan_data = scanner.scan(hosts=target, ports=ports, arguments=arguments)
    module.exit_json(scan_result = scan_data)

######################################################################
# this is magic, see lib/ansible/module_common.py
#<<INCLUDE_ANSIBLE_MODULE_COMMON>>
main()
