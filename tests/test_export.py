import unittest

from widgets.export import export_csv
from widgets.invoices import Invoice


class ExportCsvTest(unittest.TestCase):
    def test_writes_a_header_and_one_row_per_invoice(self) -> None:
        csv_text = export_csv([Invoice("A-1", "Octocat Ltd", 10.0, "NL")])
        self.assertEqual(csv_text, "number,customer,net,country\nA-1,Octocat Ltd,10.00,NL\n")
