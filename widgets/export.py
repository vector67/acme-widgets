import csv
import io

from widgets.invoices import Invoice

HEADER = ("number", "customer", "net", "country")


def export_csv(invoices: list[Invoice]) -> str:
    out = io.StringIO()
    writer = csv.writer(out, lineterminator="\n")
    writer.writerow(HEADER)
    for invoice in invoices:
        writer.writerow((invoice.number, invoice.customer, f"{invoice.net:.2f}", invoice.country))
    return out.getvalue()
