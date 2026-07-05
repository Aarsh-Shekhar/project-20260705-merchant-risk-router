import unittest

from merchant_risk_router.models import Record
from merchant_risk_router.scoring import score_record


class DepthCheck44(unittest.TestCase):
    def test_044_scenario_analysis(self):
        record = Record(id="merchant-044", exposure=55338, signal=0.817, urgency=8)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
