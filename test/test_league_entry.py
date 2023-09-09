import os
import unittest
import arrow

import cassiopeia
from cassiopeia.data import Continent, Queue

from .constants import SUMMONER_NAME, UNKNOWN_SUMMONER_NAME


class TestSummoner(unittest.TestCase):
    def setUp(self):
        cassiopeia.apply_settings(cassiopeia.get_default_config())
        cassiopeia.set_riot_api_key(os.environ.get("RIOT_API_KEY"))

    def test_league_entry(self):
        summoners = [ "JEROME36", "Fisielowsky", "Árya", "Wlodzimierz Kuc" ]

        for s in summoners:
            summoner = cassiopeia.get_summoner(name=s, region="EUNE")

            for e in summoner.league_entries:
                print(e)

            if Queue.ranked_flex_fives in summoner.league_entries:
                print("b")


if __name__ == "__main__":
    unittest.main()
