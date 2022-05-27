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
end
