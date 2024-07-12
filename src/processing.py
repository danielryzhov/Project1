from typing import Iterable

EXECUTED = 'EXECUTED'

def filter_by_state(filter_state: Iterable[str])-> None and Iterable:
    new_filter_state = []

    for dictionary_state in filter_state:
        if dictionary_state['state'] == EXECUTED:
            new_filter_state.append(dictionary_state)

    return new_filter_state


