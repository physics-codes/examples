import randphys as rp 

class Quark(object):
  def __init__(self):
    phys = rp.RandomPhysics()
    self.color_ = phys.color()
    self.flavor_ = phys.flavor()
  def join_trio(self,brother, sister):
    self.friends_ = [brother, sister]
  def friends(self):
    return self.friends_
  def color(self):
    return self.color_
  def flavor(self):
    return self.flavor_
