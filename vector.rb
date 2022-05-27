class Vector
  attr_reader :x, :y, :z
  def initialize(x, y, z)
    @x = x
    @y = y
    @z = z
  end

  def cross(vec)
    Vector.new(
      (y*vec.z) - (z*vec.y),
      (z*vec.x) - (x*vec.z),
      (x*vec.y) - (y*vec.x)
    )
  end
end
