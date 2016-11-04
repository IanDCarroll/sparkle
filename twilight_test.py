from nose.tools import *
import twilight

def test_red_is_red():
    assert twilight.sparkle.red == '\033[91m'
