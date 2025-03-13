class Node:
    def __init__(self, name, position, adj, weight=None):
        self._name = None
        self._position = None
        self._adj = None
        
    def get_name(self):
        return self._name
    
    def get_position(self):
        return self._position
    
    def get_adj(self):
        return self._adj
    
    def set_name(self, name):
        if self._name is None:
            self._name = name
            
    def set_position(self, position):
        if self._position is None:
            self._position = position
            
    def set_adj(self, adj):
        if self._adj is None:
            self._adj = adj