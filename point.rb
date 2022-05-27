class Point
  attr_reader :x, :y, :z
  def initialize(x, y, z)
    @x = x
    @y = y
    @z = z
  end

  def -(p2)
    Point.new(x - p2.x, y - p2.y, z - p2.z)
  end

  def +(p2)
    Point.new(x - p2.x, y - p2.y, z - p2.z)
  end
end
