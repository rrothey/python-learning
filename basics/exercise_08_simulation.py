import simpy
import random

def workstation(env):
    while True:
        process_time = random.gauss(10, 2)
        yield env.timeout(process_time)

env = simpy.Environment()
env.process(workstation(env))
env.run(until=100)