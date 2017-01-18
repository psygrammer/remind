import numpy as np

def test() :
	assert True

def test_new() :
	assert True

class Game(object) :
    
    def __init__(self) :
        self.state = np.zeros(9)
    
    def draw(self) :
	return '''
 | |   
-----
 | |
-----
 | |
'''
# x: 1, O:2

def test_draw() :
    g = Game()
    assert g.draw() == '''
 | |   
-----
 | |
-----
 | |
'''
    assert len(g.state) == 9
    
    pos = 1
    idx = pos - 1
    g.state[idx] = 2
    assert g.draw() == '''
0| |   
-----
 | |
-----
 | |
'''