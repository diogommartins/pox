from pox.forwarding.l2_multi import WaitingPath

__author__ = 'Roberto Barros'

from barros.roaming import SmartRoamingSwitch
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

log = core.getLogger()

# How long is allowable to set up a path?
PATH_SETUP_TIME = 4

def launch():
    core.registerNew(SmartRoamingSwitch)

    timeout = min(max(PATH_SETUP_TIME, 5) * 2, 15)
    Timer(timeout, WaitingPath.expire_waiting_paths, recurring=True)
