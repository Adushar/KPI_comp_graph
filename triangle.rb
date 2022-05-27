class Triangle
  attr_reader :p0, :p1, :p2
  # @param [Vector] p0
  # @param [Vector] p1
  # @param [Vector] p2
  def initialize(p0, p1, p2)
    @p0 = p0
    @p1 = p1
    @p2 = p2
  end

  def intersection(ray)
    epsilon = 0.00001
    e1 = p1 - p0
    e2 = p2 - p0
    q  = ray.direction.cross(e2)
    a  = e1.dot(q)
  end
end
