import unittest

from merchant_risk_router.models import Record
from merchant_risk_router.scoring import score_record


class DepthCheck59(unittest.TestCase):
    def test_059_reporting_view(self):
        record = Record(id="merchant-059", exposure=54571, signal=0.584, urgency=4)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
