from expyriment import design, control, stimuli

# set default modes for countdown, screen size and quit
control.set_develop_mode()

# create an experiment and set its start
exp = design.Experiment(name="Two Squares")
control.initialize(exp)

# create the stimuli so that the two red and green squares are 200 pixels apart
fixation = stimuli.FixCross()
squarel = stimuli.Rectangle(size=(50,50), colour=(255, 0, 0), position=(-100, 0))
squarer = stimuli.Rectangle(size=(50,50), colour=(0, 255, 0), position=(100, 0))

# start the experiment
control.start(subject_id=1)

# present the fixation cross between the two squares until keyboard press
fixation.present(clear=True, update=False)
squarel.present(clear=False, update=False)
squarer.present(clear=False, update=True)

exp.keyboard.wait()

# end the experiment
control.end()
