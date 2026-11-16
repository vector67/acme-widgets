def widget_count(widgets):
    return len(widgets)


def widget_total(widgets):
    return sum(w.price for w in widgets)
