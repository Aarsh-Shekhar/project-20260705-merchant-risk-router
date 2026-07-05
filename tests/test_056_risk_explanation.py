import unittest

from merchant_risk_router.models import Record
from merchant_risk_router.scoring import score_record


class DepthCheck56(unittest.TestCase):
    def test_056_risk_explanation(self):
        record = Record(id="merchant-056", exposure=30772, signal=0.642, urgency=5)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
