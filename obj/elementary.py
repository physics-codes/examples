from particle import Particle
import numpy

class ElementaryParticle(Particle):
  def __init__(self, spin):
    self.s = spin
    self.isFermion = bool(spin%1.0)
    self.isBoson = not self.isFermion
    self.constituents = None
