from src.masks import get_mask_card_number, get_mask_account
import pytest


@pytest.mark.parametrize("number, expected", [
    ('7000792289606361', '7000 79** **** 6361'),
    ('700079228960636', ''),
    ('a00079228960636', '')])
def test_get_mask_card_number(number, expected):
    assert get_mask_card_number(number) == expected


def test_get_mask_account():
    assert get_mask_account('73654108430135874305') == '**4305'
