from robot import Robot

def start():
    robot = Robot(robot="my_robot_name")
    robot.say_hello()
    robot.give_date_and_time(Robot)

if __name__ == '__main__':
    start()
