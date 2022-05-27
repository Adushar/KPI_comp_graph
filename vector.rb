class Vector
  attr_reader :x, :y, :z
  def initialize(x, y, z)
    @x = x
    @y = y
    @z = z
  end

  def +(vec)
    Vector.new(x+vec.x, y+vec.y, z+vec.z)
  end

  def -(vec)
    Vector.new(x-vec.x, y-vec.y, z-vec.z)
  end

  def cross(vec)
    Vector.new(
      (y*vec.z) - (z*vec.y),
      (z*vec.x) - (x*vec.z),
      (x*vec.y) - (y*vec.x)
    )
  end

  def dot(vec)
    x * vec.x + y * vec.y + z * vec.z
  end
end
