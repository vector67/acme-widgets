from dataclasses import dataclass


@dataclass(frozen=True)
class Invoice:
    number: str
    customer: str
    net: float
    country: str


def total(invoices: list[Invoice]) -> float:
    return sum(invoice.net for invoice in invoices)
