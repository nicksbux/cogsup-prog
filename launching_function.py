from expyriment import design, control, stimuli

# set default modes for countdown, screen size and quit
control.set_develop_mode()

# create an experiment and set its start
exp = design.Experiment(name="Launching")
control.initialize(exp)

# create the stimuli so that the two red and green squares are 200 pixels apart
fixation = stimuli.FixCross()
squarel = stimuli.Rectangle(size=(50,50), colour=(255, 0, 0), position=(-400, 0))
squarer = stimuli.Rectangle(size=(50,50), colour=(0, 255, 0), position=(0, 0)) 
square_length = 50

# start the experiment
control.start(subject_id=1)

# present the fixation cross between the two squares
fixation.present(clear=True, update=False)
squarel.present(clear=False, update=False)
squarer.present(clear=False, update=True)

exp.keyboard.wait()

# setting distance to travel on the x axis 
displacement_x = 400
# setting speed in pixels per update
step_size = 8

# create a function 
def launching_f(michotte, time_gap, space_gap, speed):

    if michotte :
    # motion of the left (red) square to the right, up to the right (green) square
        while squarer.position[0] - squarel.position[0] > square_length: 
            squarel.move((step_size, 0))    # set motion of the left square only on the x axis
            fixation.present(clear=True, update=False)
            squarel.present(clear=False, update=False)
            squarer.present(clear=False, update=True)

    # motion of the right(green) square to the right, when reached by the left(red) one 
        while squarer.position[0] < displacement_x:
            squarer.move((step_size, 0)) 
            fixation.present(clear=True, update=False)
            squarel.present(clear=False, update=False)
            squarer.present(clear=False, update=True)
    
    elif time_gap :
        # motion of the left (red) square to the right, up to the right (green) square
        while squarer.position[0] - squarel.position[0] > square_length: 
            squarel.move((step_size, 0))    # set motion of the left square only on the x axis
            fixation.present(clear=True, update=False)
            squarel.present(clear=False, update=False)
            squarer.present(clear=False, update=True)

    # create a temporal delay
        exp.clock.wait(200)

    # motion of the right(green) square to the right, when reached by the left(red) one 
        while squarer.position[0] < displacement_x:
            squarer.move((step_size, 0)) 
            fixation.present(clear=True, update=False)
            squarel.present(clear=False, update=False)
            squarer.present(clear=False, update=True)

    elif space_gap:
    # motion of the left (red) square to the right, BEFORE (SPACE GAP) the right (green) square
        while squarer.position[0] - squarel.position[0] > square_length + 50: 
            squarel.move((step_size, 0))    # set motion of the left square only on the x axis
            fixation.present(clear=True, update=False)
            squarel.present(clear=False, update=False)
            squarer.present(clear=False, update=True)

    # motion of the right(green) square to the right, when reached by the left(red) one 
        while squarer.position[0] < displacement_x:
            squarer.move((step_size, 0)) 
            fixation.present(clear=True, update=False)
            squarel.present(clear=False, update=False)
            squarer.present(clear=False, update=True)

    elif speed:
         # motion of the left (red) square to the right, up to the right (green) square
        while squarer.position[0] - squarel.position[0] > square_length: 
            squarel.move((step_size, 0))    # set motion of the left square only on the x axis
            fixation.present(clear=True, update=False)
            squarel.present(clear=False, update=False)
            squarer.present(clear=False, update=True)

    # motion of the right(green) square to the right, when reached by the left(red) one 
        while squarer.position[0] < displacement_x:
            squarer.move((3*step_size, 0)) 
            fixation.present(clear=True, update=False)
            squarel.present(clear=False, update=False)
            squarer.present(clear=False, update=True)

# THE FOUR POSSIBLE PARAMETERS ARE SET AND THESE 4 CODES CALL THE DIFFERENT FUNCTIONS : THE CODES ARE SIGNALED BY A ##
# executing the function with MICHOTTE
##launching_f(michotte=True, time_gap=False, space_gap=False, speed=False)
# executing the function with TIME_GAP
##launching_f(False, True, False, False)
# executing the function with SPACE_GAP
##launching_f(False, False, True, False)
# executing the function with SPEED
##launching_f(False, False, False, True)

# end the experiment
control.end()