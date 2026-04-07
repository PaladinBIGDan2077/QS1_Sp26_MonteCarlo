import numpy as np

class BitString:
    """
    Simple class to implement a config of bits
    """
    def __init__(self, N):
        self.N = N
        self.config = np.zeros(N, dtype=int) 

    def __repr__(self):
        out = ""
        for i in self.config:
            out += str(i)
        return out

    def __eq__(self, other):        
        return all(self.config == other.config)
    
    def __len__(self):
        return len(self.config)

    def on(self):
        on_bits = 0
        for x in range(self.N):
            if self.config[x] == 1:
                on_bits += 1
        return on_bits
        
    def off(self):
        off_bits = 0
        for x in range(self.N):
            if self.config[x] == 0:
                off_bits += 1
        return off_bits

    def flip_site(self,i):
        if self.config[i] == 1:
            self.config[i] = 0
        else:
            self.config[i] = 1
        return self.config

    def integer(self):
        result = 0
        for i, bit in enumerate(self.config):
            result = (result << 1) | bit
        return result

    def set_config(self, s:list[int]):
        self.config = s
        return self.config

    def set_integer_config(self, dec:int):
        for i in range(self.N):
            self.config[self.N - 1 - i] = (dec >> i) & 1
        return self.config