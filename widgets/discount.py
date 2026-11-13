from widgets.invoices import Invoice


def discounted(invoice: Invoice, percent: float) -> Invoice:
    net = round(invoice.net * (1 - percent / 100), 2)
    return Invoice(invoice.number, invoice.customer, net, invoice.country)


def discounted_all(invoices: list[Invoice], percent: float) -> list[Invoice]:
    return [discounted(invoice, percent) for invoice in invoices]
