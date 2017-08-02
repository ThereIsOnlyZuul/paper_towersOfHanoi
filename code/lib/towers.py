##### This module provides a model for playing the Towers of Hanoi


### Tower - a tower for the disks to stand on 
class Tower:

    def __init__(self,disks):
        self._disks = disks

### The disks that must be moved from tower to tower
class Disk:

    ## the size of the disk is returned (Object Oriented Design)
    def size(self):
        return self._size
    
    ## disks should be moved one at a time
    def move(self,owner,target):
        self._moveCount += 1;
        owner._disks.remove(self);
        target._disks.append(self);

    ## each disk keeps track of the number of moves it has made
    def moveCount(self):
        return self._moveCount;

    def __init__(self,size):
        self._size = size
        self._moveCount = 0;
