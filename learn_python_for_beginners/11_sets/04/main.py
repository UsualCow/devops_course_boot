def find_missing_ids(first_ids, second_ids):
    first_set = set(first_ids)
    second_set = set(second_ids)
    return first_set - second_set
