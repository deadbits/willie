# coding=utf8
"""
head.py
module by https://github.com/deadbits

perform HEAD request and show results
"""
from __future__ import unicode_literals

from willie.module import commands
import requests


def getheaders(bot, website):
    if not website.startswith('http://'):
        website = 'http://' + website
    try:
        request = requests.head(website)
        bot.say("[%s]" % website)
        for key, value in request.headers.iteritems():
            bot.say('%s => %s' % (key, value))
    except Exception, msg:
        bot.say('HEAD request failed: %s (%s)' % (website, msg))

@commands('head')
def headers(bot, trigger):
    """fetch website headers"""
    if not trigger.group(2) and trigger.group(2) is None:
        bot.reply('Please specify a website! Example: .headers http://www.google.com')
    else:
        website = trigger.group(2)
        getheaders(bot, website)
