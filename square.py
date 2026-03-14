from expyriment import design, control, stimuli

# set default modes for countdown, screen size and quit
control.set_develop_mode()

# create an experiment and set its start
exp = design.Experiment(name="Square")
control.initialize(exp)

# create the stimuli
fixation = stimuli.FixCross()
square = stimuli.Rectangle(size=(50,50), colour=(0, 0, 255))

#start the experiment
control.start(subject_id=1)

# present the fixation cross with the square for 50 ms
square.present(clear=True, update=False)
fixation.present(clear=False, update=True) 
exp.clock.wait(500)

# remove the cross and leave the square
square.present(clear=True, update=True)

# set the ending at a keyboard press
exp.keyboard.wait()

# end the current experiment
control.end()