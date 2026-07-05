import unittest

from merchant_risk_router.models import Record
from merchant_risk_router.scoring import score_record


class DepthCheck35(unittest.TestCase):
    def test_035_backlog_triage(self):
        record = Record(id="merchant-035", exposure=53241, signal=0.837, urgency=2)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
