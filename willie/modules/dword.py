▽
# coding=utf8
"""
dword.py
module by https://github.com/deadbits

convert ipv4 address to dword
"""
from __future__ import unicode_literals
from willie.module import commands


@commands('dword')
def ip2dword(bot, trigger):
    """convert ipv4 address to dword"""
    if trigger.group(2) is None:
        bot.reply('Please specify an ipv4 address. Example: .dword 10.110.1.80')
    else:
        ipv4 = trigger.group(2)
        try:
            ip = ipv4.split('.')
            dword = (((((int(ip[0])*256) + int(ip[1])) * 256) + int(ip[2])) * 256) + \
                int(ip[3])
            bot.reply('%s => %s' % (ipv4, dword))
        except Exception, msg:
            bot.reply('error: %s' % msg)
