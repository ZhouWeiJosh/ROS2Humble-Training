# Week 2

## Recap / Instructions
So now you after finishing the Week 1 Exercise, you should have a ROS2 package that can be exectuted via `ros2 run <package_name> <executable_name>`. This Week 2 exercise will build off your Week 1 solution. You will modify your node from last week to publish button data to a topic instead of logging the left joystick. Then you will create another node that subscribes to that topic and does something. The very basics will be to print out a message whenever a button is pressed, but you are free to do anything you want. 


## Git Stuff
Do this week's exercise in another branch called `week2-<your_name>`. In order to do this follow these steps:
1. Make sure you are on the same branch from Week 1 i.e (week1-<your_name>)
- When you run `git branch` make sure the asterisk (*) is next to it
2. Run `git checkout -b week2-<your_name>` to create a new branch that is based off your week 1 branch

## Steps to follow
1. Create a publisher that publishes to `button_a_press` in node `__init__` 
2. Change joy_callback to publish `button_a` data to `button_a_press`
- Hint: Think of what you did last week for axes
3. Create new file `xbox_logger` with a node that subscribes to topic `button_a_press`
4. In the callback do something with the button press data such as logging 'Button A is pressed'
5. Test it! 
- Hint: Refer back to what you had to do in setup.py in week 1 in order to be able to ros2 run it
- Hint: Use `colcon build --symlink-install && source ./install/setup.bash` to build and source in one command

## Launch File Time
Now that cumbersome to test wasn't it. You had to pull up three different terminals in order to test your new node. 
1. `ros2 run joy joy_node`
2. `ros2 run <package_name> <your_week_1_node>`
3. `ros2 run <package_name> xbox_logger`
<br>
Wouldn't it be so much easier if you could launch all these nodes with one command. Well you can! That will be your next task for this exercise. Launch files are very powerful and are how multiple nodes are started and configured. For this exerise we will just go over how to start multiple nodes from one launch file. 

### Launch File Steps
1. In your package's root directory create a directory called `launch`
```bash
mkdir launch
```

Your package should look something like this:
```
<package_name>/
├── package.xml
├── launch/
│   └── <launch_file.py>
├── setup.py
├── setup.cfg
├── resource/
│   └── <package_name>
├── <package_name>/
│   ├── __init__.py
│   └── <week1_node>.py
│   └── <xbox_logger>.py
└── test/
```
2. Create a launch file within the `<package_name>/launch/` directory \
Hint: Use the [tutorials](https://docs.ros.org/en/humble/Tutorials/Intermediate/Launch/Creating-Launch-Files.html) as a base
3. Test it! Use `ros2 launch <package_name> <launch_file_name>` ***in the*** `<package_name>/launch/` directory. Remember to build and source before testing. \


Now this works, but you can only luanch it if you are in the `<package_name>/launch/` directory so how do we make it so you can launch it in the workspace root? We need to edit the setup.py file so that ros2 knows it's there. 

Follow this [page](https://docs.ros.org/en/humble/Tutorials/Intermediate/Launch/Launch-system.html) and add 
```python
(os.path.join('share', package_name, 'launch'), glob('launch/*'))
```
to the `data_files[]` in `setup.py`. Basically it puts all your launch files into the share directory so that you can execute it. 


Now you have a Node that subscribes to the `/joy` topic and publishes data to a seperate topic that another Node processes in order to do something. It's the same principle that we used for the URC 2025 teleoperation of the rover. Add some logic to control motors and you can move things with a controller.

## Extra 
1. Debounce the button press
2. Add a way to not flood the terminal with messages constantly with prints *WITHOUT* using time.sleep()
3. Research and implement other cool things you can do with launch files
