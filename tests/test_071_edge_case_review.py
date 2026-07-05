import unittest

from merchant_risk_router.models import Record
from merchant_risk_router.scoring import score_record


class DepthCheck71(unittest.TestCase):
    def test_071_edge_case_review(self):
        record = Record(id="merchant-071", exposure=34075, signal=0.656, urgency=3)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
