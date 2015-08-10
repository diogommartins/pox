# coding=utf-8
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
from pox.openflow import PacketIn


class ConnectionsController(object):
    def __init__(self):
        self.connections = set()
        core.openflow.addListeners(self)

    def _handle_ConnectionUp(self, event):
        self.connections.add(event.connection)

    def _handle_ConnectionDown(self, event):
        self.connections.remove(event.connection)

    def _handle_PacketIn(self, event):
        """
        Método é chamado quando a controladora recebe uma mensagem do tipo ofp_packet_in / OFPT_PACKET_IN de um switch,
        que significa que um pacote recebido por um switch não existe em sua tabela ou uma entrada que existe na tabela
        possui uma informação que especifica que a mensagem deve ser encaminhada para a controladora

        :type event: PacketIn
        """
        packet = event.parsed
        if packet.type == packet.ARP_TYPE:
            pass

    def _handle_PortStatus(self, event):
        """
        Método é chamado quando a controladora recebe uma mensagem do tipo ofp_port_status de um switch, que significa
        que alguma porta mudou
        """
        pass

class SmartRoamingSwitch(EventMixin):
    # Listen to dependencies
    def __init__(self):
        self.connections_controller = ConnectionsController()

        def startup():
            core.openflow.addListeners(self)
            core.openflow_discovery.addListeners(self)

        core.call_when_ready(startup, ('openflow', 'openflow_discovery'))

    def _handle_LinkEvent(self, event):
        pass