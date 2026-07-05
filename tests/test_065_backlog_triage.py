import unittest

from merchant_risk_router.models import Record
from merchant_risk_router.scoring import score_record


class DepthCheck65(unittest.TestCase):
    def test_065_backlog_triage(self):
        record = Record(id="merchant-065", exposure=70016, signal=0.346, urgency=6)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
