import unittest

from merchant_risk_router.models import Record
from merchant_risk_router.scoring import score_record


class DepthCheck26(unittest.TestCase):
    def test_026_risk_explanation(self):
        record = Record(id="merchant-026", exposure=32383, signal=0.580, urgency=6)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
