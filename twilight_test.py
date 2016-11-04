from nose.tools import *
import twilight

def test_red_is_red():
    assert twilight.sparkle.red == '\033[91m'

def test_yellow_is_yellow():
    assert twilight.sparkle.yellow == '\033[93m'

def test_green_is_green():
    assert twilight.sparkle.green == '\033[92m'

def test_blue_is_blue():
    assert twilight.sparkle.blue == '\033[94m'

def test_reset_resets():
    assert twilight.sparkle.reset == '\033[0m'
