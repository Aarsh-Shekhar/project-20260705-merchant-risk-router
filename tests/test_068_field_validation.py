import unittest

from merchant_risk_router.models import Record
from merchant_risk_router.scoring import score_record


class DepthCheck68(unittest.TestCase):
    def test_068_field_validation(self):
        record = Record(id="merchant-068", exposure=48281, signal=0.509, urgency=5)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
