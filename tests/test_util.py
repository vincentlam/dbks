import pytest
from dbks.util import *


@pytest.mark.parametrize(
    "src_dict, tgt_dict, result",
    [
        ({"a": "A", "num": 0}, {"a": "A", "num": 0}, True),
        ({"a": "B", "num": 0}, {"a": "A", "num": 0}, False),
        ({"a": "A", "b": "B", "num": 0}, {"a": "A", "num": 0}, False),
        ({"a": "A", "num": 0}, {"a": "A", "b": "B", "num": 0}, True),
        ({"a": "A", "num": 0}, {"b": "B", "num": 0}, False),
        (
            {"a": "A", "num": 0, "c": {"d": 1}},
            {"a": "A", "num": 0, "c": {"d": 1}},
            True,
        ),
        (
            {"a": "A", "num": 0, "c": {"d": 1}},
            {"a": "A", "num": 0, "c": {"d": 2}},
            False,
        ),
        (
            {"a": "A", "num": 0, "c": {"d": 1}},
            {"b": "B", "num": 0, "c": {"d": 1}},
            False,
        ),
        (
            {"a": "A", "num": 0, "c": {"d": 1}},
            {"b": "B", "num": 0, "c": {"d": 2}},
            False,
        ),
        (
            {"a": "A", "num": 0, "c": {"d": ["e"]}},
            {"a": "A", "num": 0, "c": {"d": ["e"]}},
            True,
        ),
        (
            {"a": "A", "num": 0, "c": {"d": ["e"]}},
            {"a": "A", "num": 0, "c": {"d": ["e", "f"]}},
            False,
        ),
        (
            {"a": "A", "num": 0, "c": {"d": ["e"]}},
            {"b": "B", "num": 0, "c": {"d": ["e"]}},
            False,
        ),
        (
            {"a": "A", "num": 0, "c": {"d": ["e"]}},
            {"b": "B", "num": 0, "c": {"d": ["e", "f"]}},
            False,
        ),
        (
            {"a": "A", "num": 0, "c": {"d": {"e": 1}}},
            {"a": "A", "num": 0, "c": {"d": {"e": 1}}},
            True,
        ),
        (
            {"a": "A", "num": 0, "c": {"d": {"e": 1}}},
            {"a": "A", "num": 0, "c": {"d": {"e": 2}}},
            False,
        ),
        (
            {"a": "A", "num": 0, "c": {"d": {"e": 1}}},
            {"b": "B", "num": 0, "c": {"d": {"e": 1}}},
            False,
        ),
        (
            {"a": "A", "num": 0, "c": {"d": {"e": 1}}},
            {"b": "B", "num": 0, "c": {"d": {"e": 2}}},
            False,
        ),
        (
            {"a": "A", "num": 0, "c": {"d": {"e": ["f"]}}},
            {"a": "A", "num": 0, "c": {"d": {"e": ["f"]}}},
            True,
        ),
        (
            {"a": "A", "num": 0, "c": {"d": {"e": ["f"]}}},
            {"a": "A", "num": 0, "c": {"d": {"e": ["f", "g"]}}},
            False,
        ),
        (
            {"a": "A", "num": 0, "c": {"d": {"e": ["f"]}}},
            {"b": "B", "num": 0, "c": {"d": {"e": ["f"]}}},
            False,
        ),
        (
            {"a": "A", "num": 0, "c": {"d": {"e": ["f"]}}},
            {"b": "B", "num": 0, "c": {"d": {"e": ["f", "g"]}}},
            False,
        ),
    ],
)
def test_util_same_as_target(src_dict, tgt_dict, result):
    assert same_as_target(src_dict, tgt_dict) == result
