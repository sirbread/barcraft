from ursina import *

def oscSim(self):
    self.t += time.dt
    self.planet.x = math.cos(self.t) + self.position.x
    self.planet.y = self.position.y
    self.planet.z = math.sin(self.t) + self.position.z

