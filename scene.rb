class Scene
  SCREEN_WIDTH = 300.freeze
  SCREEN_HEIGHT = 300.freeze
  attr_accessor :objects, :light_source

  def initialize(light_point:, camera:, objects: [])
    @light_point = light_point
    @camera = camera
    @objects = objects
  end

  def render
    calculate_pixels
  end

  def calculate_pixels
    pixels = (0..SCREEN_WIDTH).product((0..SCREEN_HEIGHT))
    pixels.map do |x, y|

    end
  end

  def intersect_point(rayVector, rayPoint, planeNormal, planePoint)
    diff = rayPoint - planePoint
    prod1 = diff.dot planeNormal
    prod2 = rayVector.dot planeNormal
    prod3 = prod1 / prod2
    rayPoint - rayVector * prod3
  end
end
