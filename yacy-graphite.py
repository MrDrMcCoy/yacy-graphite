#!/usr/bin/env python

import xml.etree.ElementTree as xmltree
import urllib2
import time
import socket
import re

# config
graphite_port = 2003
graphite_host = ''
yacy_port = 8090
yacy_host = ''
yacy_url = 'http://' + yacy_host + ':' + str(yacy_port) + '/Network.xml'
prefix = ''

# get data
timestamp = str(int(time.time()))
xml_root = xmltree.parse(urllib2.urlopen(yacy_url)).getroot()


def send_graphite(message):
    print(message)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((graphite_host, graphite_port))
    s.send(message)
    s.close()

# send data
for category in xml_root:
    for metric in category:
        # only send if metric is numeric
        if re.match('[0-9\.]+', metric.text):
            # assemble the elements of the metric line into the graphite format
            phase1 = \
                prefix + '.' + \
                re.sub('\.', '_', yacy_host) + '.' + \
                category.tag + '.' + \
                metric.tag + ' ' + \
                metric.text + ' ' + \
                timestamp
            # remove duplicate dots
            phase2 = re.sub('\.+', '.', phase1)
            # remove leading dots
            phase3 = re.sub('^\.', '', phase2)
            # send metric line
            send_graphite(phase3)
