from nose.tools import *
import twilight

def test_red():
    assert twilight.sparkle.red == '\033[31m'

def test_yellow():
    assert twilight.sparkle.yellow == '\033[93m'

def test_green():
    assert twilight.sparkle.green == '\033[32m'

def test_blue():
    assert twilight.sparkle.blue == '\033[34m'

def test_reset():
    assert twilight.sparkle.reset == '\033[0m'

