import unittest

from merchant_risk_router.models import Record
from merchant_risk_router.scoring import score_record


class DepthCheck62(unittest.TestCase):
    def test_062_operator_handoff(self):
        record = Record(id="merchant-062", exposure=73434, signal=0.635, urgency=4)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
