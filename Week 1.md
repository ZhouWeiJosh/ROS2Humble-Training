
# Week 1 — ROS 2 Fundamentals

## 1. Sourcing the ROS 2 Environment

Before using any ROS 2 commands, you must **source the ROS 2 environment**.

```bash
source /opt/ros/humble/setup.bash
```

Sourcing does the following:

* Adds ROS 2 tools (`ros2`, `colcon`) to your PATH
* Makes ROS 2 packages discoverable
* Sets environment variables required for ROS communication

### Making sourcing persistent

To avoid manually sourcing every new terminal, add it to your `.bashrc`:

```bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
```

Your `.bashrc` is executed **every time a new terminal opens**, so ROS 2 will
automatically be available.

---

## 2. Creating a ROS 2 Workspace

A **workspace** is where you build and manage your own ROS 2 packages.

Create a workspace with the standard ROS layout:

```bash
mkdir -p ~/ros2_ws/src
```

Explanation:

* `mkdir` — make directory
* `-p` — create parent directories if they do not exist
* `src` — required directory where all ROS packages live

Expected structure:

```
ros2_ws/
└── src/
```

---

## 3. Conceptual Overview: Nodes and Topics

### Nodes

A **node** is a single executable that performs **one focused responsibility**.

Examples:

* Reading joystick input
* Controlling motors
* Publishing sensor data
* Running navigation logic

Key idea:

> **One node = one job**

Multiple nodes running together form a robotic system.

---

### Topics

A **topic** is a **named communication channel** used by nodes to exchange data.

* Nodes **publish** messages to topics
* Other nodes **subscribe** to those topics
* Communication is asynchronous and loosely coupled

Example topic:

```
/joy
```

* `joy_node` publishes joystick data
* Your node subscribes to `/joy`
* The nodes do not need to know about each other

Key idea:

> **Nodes do not talk to nodes — nodes talk to topics**

---

### Nodes and Topics Together

A ROS system looks like this:

```
[ joy_node ]  --publishes-->  /joy  --subscribed by-->  [ controller_node ]
```

This design allows nodes to be replaced, extended, or reused without changing the rest
of the system.

---

## 4. Creating a ROS 2 Package

A **package** is the basic unit of build, install, and execution in ROS 2.

### Creating a Python package

From inside the `src` directory:

```bash
ros2 pkg create \
  --build-type ament_python \
  --license Apache-2.0 \
  <package_name>
```

Example:

```bash
ros2 pkg create --build-type ament_python --license Apache-2.0 py_joy
```

---

### Python package structure

A typical Python ROS 2 package looks like:

```
py_joy/
├── package.xml
├── setup.py
├── setup.cfg
├── resource/
│   └── py_joy
├── py_joy/
│   ├── __init__.py
│   └── xbox_reader.py
└── test/
```

Important files:

* `package.xml` — package metadata and dependencies
* `setup.py` — Python install and executable definitions
* `py_joy/` — actual Python source code

---

## 5. Building the Package

From the workspace root (`ros2_ws`):

```bash
colcon build --packages-select py_joy
```

This:

* Builds only the selected package
* Installs it into the `install/` directory
* Makes it runnable with `ros2 run`

---

## 6. Sourcing the Workspace

After building, you must source the workspace:

```bash
source install/local_setup.bash
```

This step:

* Makes newly built packages visible to ROS
* Must be repeated after every rebuild
* Must be run in each new terminal

---

## 7. Running a Node

Once built and sourced, run a node using:

```bash
ros2 run <package_name> <executable_name>
```

Example:

```bash
ros2 run py_joy reader
```

The executable name is defined in `setup.py` under `console_scripts`.

---

## 8. Week 1 — Joystick Reader

Create a branch with your name using this command:
```bash
git checkout -b week1-<yourname>
```

### Objective

Practice:

* Creating a ROS 2 package
* Writing a Python node
* Subscribing to a topic
* Reading live hardware input

### Task

1. Clone this repository
2. Create a package named `xbox_controller`
3. Write a Python node that:

   * Subscribes to the `/joy` topic
   * Reads the **left joystick X and Y axes**
   * Prints the values to the terminal

### Hints

* Start the joystick driver:

  ```bash
  ros2 run joy joy_node
  ```
* The message type is:

  ```text
  sensor_msgs/Joy
  ```
* Joystick axes are accessed using:

  ```python
  msg.axes[index]
  ```

---
