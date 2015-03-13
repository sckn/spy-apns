#!/usr/bin/python
# -*- coding:utf-8 -*-
import ssl
import json
import socket
import struct
import binascii
import argparse

"""
SPY-APNS - sckn.org python apns client
Author : Seçkin ALAN - seckinalan@gmail.com
Description: This library send push notification with apns.

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
MA 02110-1301, USA.
"""

#------------------------------------------------------------------------------
def get_args():
    parser =  argparse.ArgumentParser()
    parser.add_argument('-c','--cert-file', required=True,
            help='Certificate file full path')
    parser.add_argument('-a','--alert', required=True,
            help="Send message")
    parser.add_argument('-d','--device-token', required=True,
            help="Device token")
    result = parser.parse_args()

    return result

#-----------------------------------------------------------------------------
def init_payload(alert):
    payload = {
            'aps': {
                'alert':alert,
                'sound':'default',
                'badge':1,
                },
            }
    data = json.dumps(payload)
    return data
    pass

#-----------------------------------------------------------------------------
def send(cert, payload, token):

    byte_token = binascii.unhexlify(token)
    send_format = '!BH32sH%ds' % len(payload)
    notification = struct.pack(send_format, 0, 32, byte_token,
            len(payload), payload)

    ssl_sock = ssl.wrap_socket(socket.socket(socket.AF_INET,
         socket.SOCK_STREAM), certfile = cert)
    ssl_sock.connect(('gateway.sandbox.push.apple.com', 2195))
    ssl_sock.write(notification)
    ssl_sock.close()

#-----------------------------------------------------------------------------
if __name__ == "__main__":
    args = get_args();
    payload = init_payload(args.alert);
    try:
        send(args.cert_file, payload, args.device_token)
        result = 0
    except:
        result = 1
        raise

