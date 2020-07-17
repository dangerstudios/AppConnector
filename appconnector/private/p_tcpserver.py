from ..qt import QtNetwork, QtCore
from .p_server import Server


class TcpServer(QtNetwork.QTcpServer, metaclass=Server):

    def __init__(self, *args, **kwargs):

        """
        initialise server
        """

        QtNetwork.QTcpServer.__init__(self, *args, **kwargs)
