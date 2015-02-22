# coding=utf8
"""
resolve.py
module by https://github.com/deadbits

reverse DNS resolution
"""
from __future__ import unicode_literals

from willie.module import commands
import socket
import re

def host2ip(host):
    try:
        result = socket.gethostbyaddr(host)[0]
        return result
    except socket.gaierror, err:
        return None

def ip2host(host):
    try:
        result = socket.gethostbyname(host)
        return result
    except socket.gaierror, err:
        return None

@commands('dns')
def resolve(bot, trigger):
    """reverse dns resolution"""
    host = trigger.group(2)
    if not host:
        return bot.reply("you must specify an IP address or hostname")
    ipv4_re = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    if ipv4_re.match(host):
        result = ip2host(host)
        if result is not None:
            bot.say('%s resolved to %s' % (host, host2ip(host)))
        else:
            bot.say('failed to resolve %s' % host)
    elif host2ip(host) is not None:
        bot.say('%s resolved to %s' % (host, ip2host(host)))
    else:
        bot.say('failed to resolve %s' % host)
