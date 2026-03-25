import math
from expyriment import design, control, stimuli
from expyriment.misc import geometry # import the geometry helper to build the shapes

# set default modes for countdown, screen size and quit
control.set_develop_mode()

# create an experiment and set its start
exp = design.Experiment(name="Labeled Shapes")
control.initialize(exp)

# build the triangle from geometry package 
triangle_build = geometry.vertices_regular_polygon(n_edges=3, length=50)
# determine the height of the two shapes from the triangle 
height = math.sqrt(50**2 - 25**2)
# determine the side of the hexagon and build it
hex_edge = height / math.sqrt(3)
hexagon_build = geometry.vertices_regular_polygon(n_edges=6, length=hex_edge)

# labeling the shapes
line_tri = stimuli.Rectangle(size=(3, 50),colour=(255, 255, 255), position=(-100, height + 25))
line_hex = stimuli.Rectangle(size=(3, 50),colour=(255, 255, 255), position=(100, height + 25))
label_tri = stimuli.TextLine(text="triangle", text_size=(22), text_colour=(255, 255, 255), position=(-100, height*2 + 20))
label_hex = stimuli.TextLine(text="hexagon", text_size=(22), text_colour=(255, 255, 255), position=(100, height*2 + 20))

# create the stimuli so that the two purple and yellow shapes are 200 pixels apart
fixation = stimuli.FixCross()
triangle = stimuli.Shape(vertex_list=triangle_build, colour=(128, 0, 128), position=(-100, 0))
hexagon = stimuli.Shape(vertex_list=hexagon_build, colour=(255, 255, 0), position=(100, 0))

# start the experiment
control.start(subject_id=1)

# present the fixation cross between the two squares until keyboard press
fixation.present(clear=True, update=False)
triangle.present(clear=False, update=False)
line_tri.present(clear=False, update=False)
label_tri.present(clear=False, update=False)
hexagon.present(clear=False, update=False)
line_hex.present(clear=False, update=False)
label_hex.present(clear=False, update=True)

exp.keyboard.wait()

# end the experiment
control.end()
