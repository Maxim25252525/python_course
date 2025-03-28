from hw8.tasks.task1 import get_length
import pytest


@pytest.mark.parametrize(('words', 'result'), [('hello', 1), ('hello world', 2), ('Hello world! How are you? ', 5), (' ', 0)])
def test_get_length(words, result):
    assert get_length(words) == result
