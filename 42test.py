import urllib

__author__ = 'Alan'

import unittest
from BeautifulSoup import *

soup = BeautifulSoup(urllib.urlopen("http://www.dublinbus.ie/en/RTPI/Sources-of-Real-Time-Information/?searchtype=view&searchquery=42"))

stop_num=soup.find(id="ctl00_FullRegion_MainRegion_ContentColumns_holder_RealTimeStopInformation1_lblStopNumber")

print(stop_num.contents)
