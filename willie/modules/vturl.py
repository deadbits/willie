# coding=utf8
"""
vturl.py
module by https://github.com/deadbits

check virustotal for scanned url
"""
from __future__ import unicode_literals

from willie.module import commands
import urllib
import urllib2
import simplejson
import datetime

api_key = ''

def searchvt(bot, check):
    url = 'https://www.virustotal.com/vtapi/v2/url/report'
    parameters = {'resource': check, 'apikey': api_key}
    data = urllib.urlencode(parameters)
    try:
        request = urllib2.Request(url, data)
        response = urllib2.urlopen(request)
        result = response.read()
        report = simplejson.loads(result)
        date = report['scan_date'].split(' ')[0]
        bot.say('scan date: %s' % datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%b %d %Y"))
        bot.say('total scans: %s' % report['total'])
        bot.say('detected: %s' % report['positives'])
    except Exception, msg:
        bot.say('failed to check virustotal for url %s (%s)' % (check, msg))



@commands('vturl')
def vturl(bot, trigger):
    """check virustotal for by url"""
    input_url = trigger.group(2)
    if api_key == '':
        bot.say('please enter your VirusTotal API key in modules/vturl.py')
    else:
        searchvt(bot, input_url)
