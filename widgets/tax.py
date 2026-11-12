from widgets.invoices import Invoice

RATES = {"DE": 0.19, "FR": 0.2, "NL": 0.21}


def tax(invoice: Invoice) -> float:
    rate = RATES[invoice.country]
    return invoice.net * rate


def gross(invoice: Invoice) -> float:
    return invoice.net + tax(invoice)
