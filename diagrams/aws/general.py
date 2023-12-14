# This module is automatically generated by autogen.sh. DO NOT EDIT.

from . import _AWS


class _General(_AWS):
    _type = "general"
    _icon_dir = "resources/aws/general"


class Client(_General):
    _icon = "client.png"


class Disk(_General):
    _icon = "disk.png"


class Forums(_General):
    _icon = "forums.png"


class General(_General):
    _icon = "general.png"


class GenericDatabase(_General):
    _icon = "generic-database.png"


class GenericFirewall(_General):
    _icon = "generic-firewall.png"


class GenericOfficeBuilding(_General):
    _icon = "generic-office-building.png"


class GenericSamlToken(_General):
    _icon = "generic-saml-token.png"


class GenericSDK(_General):
    _icon = "generic-sdk.png"


class InternetAlt1(_General):
    _icon = "internet-alt1.png"


class InternetAlt2(_General):
    _icon = "internet-alt2.png"


class InternetGateway(_General):
    _icon = "internet-gateway.png"


class Marketplace(_General):
    _icon = "marketplace.png"


class MobileClient(_General):
    _icon = "mobile-client.png"


class Multimedia(_General):
    _icon = "multimedia.png"


class OfficeBuilding(_General):
    _icon = "office-building.png"


class SamlToken(_General):
    _icon = "saml-token.png"


class SDK(_General):
    _icon = "sdk.png"


class SslPadlock(_General):
    _icon = "ssl-padlock.png"


class TapeStorage(_General):
    _icon = "tape-storage.png"


class Toolkit(_General):
    _icon = "toolkit.png"


class TraditionalServer(_General):
    _icon = "traditional-server.png"


class User(_General):
    _icon = "user.png"


class Users(_General):
    _icon = "users.png"


class Cloud(_General):
    _icon = "aws-cloud.png"


class Account(_General):
    _icon = "aws-account.png"


class Region(_General):
    _icon = "region.png"


# Aliases

OfficeBuilding = GenericOfficeBuilding

# Cluster

from diagrams import Cluster


class ClusterCloud(Cluster):
    _icon_node = Cloud
    _graph_attr = {
        "bgcolor": "white",
        "pencolor": "#F78E04",
    }

    def __init__(
        self,
        label: str = "cloud",
        direction: str = "LR",
    ):
        super().__init__(label, direction, icon_node=self._icon_node, graph_attr=self._graph_attr)


class ClusterAccount(Cluster):
    _icon_node = Account
    _graph_attr = {
        "bgcolor": "white",
        "pencolor": "#CD2264",
    }

    def __init__(
        self,
        label: str = "account",
        direction: str = "LR",
    ):
        super().__init__(label, direction, icon_node=self._icon_node, graph_attr=self._graph_attr)


class ClusterRegion(Cluster):
    _icon_node = Region
    _graph_attr = {"bgcolor": "white", "pencolor": "#147EBA", "style": "rounded,dashed"}

    def __init__(
        self,
        label: str = "region",
        direction: str = "LR",
    ):
        super().__init__(label, direction, icon_node=self._icon_node, graph_attr=self._graph_attr)
