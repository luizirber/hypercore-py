import hypercore

def test_feed():
    feed = hypercore.lib.new_feed()
    assert feed is not None
