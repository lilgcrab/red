#From https://stackoverflow.com/questions/7505988/importing-from-a-relative-path-in-python

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'my_module'))
from red_functions import start, stop_and_rest, witch_house, go_inside, to_grandmas

#start first function
start()
