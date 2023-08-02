from HumanWorker import HumanWorker
from RobotWorker import RobotWorker

if __name__ == '__main__':

    human = HumanWorker()
    robot = RobotWorker()

    human.work()
    human.eat()

    robot.work()