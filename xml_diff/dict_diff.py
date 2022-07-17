def make_dict_diff(node1, node2):
    tree = {}
    common_keys = set(node1.keys()) & set(node2.keys())
    removed = set(node1.keys()) - common_keys
    added = set(node2.keys()) - common_keys
    return_itinerary = "Return_itinerary"
    if return_itinerary in removed:
        removed.remove(return_itinerary)
        tree.update({return_itinerary: f"removed {node1[return_itinerary]}"})
        tree.update({'Pricing': "The price can't be compared because of the absence of return itinerary"})
        common_keys.remove('Pricing')
    if return_itinerary in added:
        added.remove(return_itinerary)
        tree.update({return_itinerary: f"added {node2[return_itinerary]} The price can't be compared"})
        tree.update({'Pricing': "The price can't be compared because of the absence of onward itinerary"})
        common_keys.remove('Pricing')
    tree.update({key: f'removed {node1[key]}' for key in removed})
    tree.update({key: f'added {node2[key]}' for key in added})
    for key in common_keys:
        if isinstance(node1[key], dict) and isinstance(node2[key], dict):
            tree[key] = make_dict_diff(node1[key], node2[key])
            continue
        tree[key] = 'unchanged' if node1[key] == node2[key] else f'updated from {node1[key]} to {node2[key]}'
    return tree
