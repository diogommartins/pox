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

def launch():
    core.registerNew(SmartRoamingSwitch)

    timeout = min(max(PATH_SETUP_TIME, 5) * 2, 15)
    Timer(timeout, WaitingPath.expire_waiting_paths, recurring=True)
