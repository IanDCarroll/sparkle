from nose.tools import *
import twilight

def test_reset():
    assert twilight.sparkle.reset == '\033[0m'

def test_charcoal():
    assert twilight.sparkle.charcoal == '\033[0m\033[30m'

def test_grey():
    assert twilight.sparkle.grey == '\033[0m\033[90m'

def test_wine():
    assert twilight.sparkle.wine == '\033[0m\033[31m\033[2m'

def test_red():
    assert twilight.sparkle.red == '\033[0m\033[31m'

def test_cherry():
    assert twilight.sparkle.cherry == '\033[0m\033[91m'

def test_bronze():
    assert twilight.sparkle.bronze == '\033[0m\033[33m\033[2m'

def test_gold():
    assert twilight.sparkle.gold == '\033[0m\033[33m'

def test_yellow():
    assert twilight.sparkle.yellow == '\033[0m\033[93m'

def test_grass():
    assert twilight.sparkle.grass == '\033[0m\033[92m'

def test_green():
    assert twilight.sparkle.green == '\033[0m\033[32m'

def test_forest():
    assert twilight.sparkle.forest == '\033[0m\033[32m\033[2m'

def test_teal():
    assert twilight.sparkle.teal == '\033[0m\033[36m\033[2m'

def test_cyan():
    assert twilight.sparkle.cyan == '\033[0m\033[36m'

def test_sky():
    assert twilight.sparkle.sky == '\033[0m\033[96m'

def test_baby():
    assert twilight.sparkle.baby == '\033[0m\033[94m'

def test_blue():
    assert twilight.sparkle.blue == '\033[0m\033[34m'

def test_royal():
    assert twilight.sparkle.royal == '\033[0m\033[34m\033[2m'

def test_magenta():
    assert twilight.sparkle.magenta == '\033[0m\033[35m\033[2m'

def test_purple():
    assert twilight.sparkle.purple == '\033[0m\033[35m'

def test_violet():
    assert twilight.sparkle.violet == '\033[0m\033[95m'

def test_light():
    assert twilight.sparkle.light == '\033[0m\033[37m'

def test_white():
    assert twilight.sparkle.white == '\033[0m\033[97m'
