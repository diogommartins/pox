from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.recoco import Timer
from collections import defaultdict
from pox.openflow.discovery import Discovery
from pox.lib.util import dpid_to_str
import time
import random
from pox.lib.addresses import IPAddr, EthAddr
import pox.lib.packet as pkt


class SmartRoamingSwitch(EventMixin):
    # Listen to dependencies
    def __init__(self):
        def startup():
            core.openflow.addListeners(self, priority=0)
            core.openflow_discovery.addListeners(self)

        core.call_when_ready(startup, ('openflow', 'openflow_discovery'))