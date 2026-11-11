import unittest

from widgets.invoices import Invoice, total


class TotalTest(unittest.TestCase):
    def test_sums_the_net_amounts(self) -> None:
        invoices = [Invoice("A-1", "Octocat Ltd", 10.0, "NL"),
                    Invoice("A-2", "Octocat Ltd", 5.5, "DE")]
        self.assertEqual(total(invoices), 15.5)
