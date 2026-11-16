def get_item_count(item_counts, item_name):
    if item_name in item_counts:
        return item_counts[item_name]
    return 0
