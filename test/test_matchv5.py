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

    def test_matchv5(self):
        summoner = cassiopeia.get_summoner(name="rdκ", region="EUNE")

        matches = cassiopeia.get_match_history(
            continent=Continent.europe,
            puuid=summoner.puuid,
            # start_time=arrow.now().shift(days=-2),
            # end_time=1653773677,  # arrow.now().shift(hours=-2),
            # count=10,
            # queue=Queue.ranked_solo_fives,
        )

        print(len(matches))

        for m in matches:
            print(m)
            for p in m.participants:
                print(f"{p.summoner.name} {p.champion.name}")
            print()


if __name__ == "__main__":
    unittest.main()
