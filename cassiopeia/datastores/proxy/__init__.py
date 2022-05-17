from typing import Iterable, Set

from datapipelines import CompositeDataSource
from .common import ProxySource


def _default_services(server_url: str) -> Set[ProxySource]:
    from ..common import HTTPClient
    from ..image import ImageDataSource
    from .champion import ChampionAPI
    from .summoner import SummonerAPI
    from .championmastery import ChampionMasteryAPI
    from .match import MatchAPI
    from .spectator import SpectatorAPI
    from .status import StatusAPI
    from .leagues import LeaguesAPI
    from .thirdpartycode import ThirdPartyCodeAPI

    client = HTTPClient()
    services = {
        ImageDataSource(client),
        ChampionAPI(server_url=server_url, http_client=client),
        SummonerAPI(server_url=server_url, http_client=client),
        ChampionMasteryAPI(server_url=server_url, http_client=client),
        MatchAPI(server_url=server_url, http_client=client),
        SpectatorAPI(server_url=server_url, http_client=client),
        StatusAPI(server_url=server_url, http_client=client),
        LeaguesAPI(server_url=server_url, http_client=client),
        ThirdPartyCodeAPI(server_url=server_url, http_client=client),
    }

    return services


class Proxy(CompositeDataSource):
    def __init__(
        self, url: str, services: Iterable[ProxySource] = None
    ) -> None:

        if services is None:
            services = _default_services(server_url=url)

        super().__init__(services)

    def set_server_url_and_port(self, server_url: str):
        for sources in self._sources.values():
            for source in sources:
                if isinstance(source, ProxySource):
                    source._server_url = server_url
