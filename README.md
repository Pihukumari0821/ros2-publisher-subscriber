# ROS 2 Publisher and Subscriber

A beginner ROS 2 project demonstrating inter-node communication using Publisher and Subscriber nodes in Python.

## Project Overview

This project implements a simple communication system using ROS 2. A publisher node generates incrementing integer values and publishes them to a ROS 2 topic. A subscriber node receives these messages and displays them in the terminal.

## Architecture

The project consists of two ROS 2 nodes:

**1. Publisher Node**
- Node name: `publisher_node`
- Generates incrementing integer values.

- Publishes messages every second.
- Uses `std_msgs/msg/Int32`.

**2. Subscriber Node**
- Node name: `subscriber_node`
- Subscribes to the publisher's topic.
- Receives and displays incoming integer messages.

## Communication Details

| Parameter | Value |
|---|---|
| Topic | `number_topic` |
| Message Type | `std_msgs/msg/Int32` |
| Publishing Interval | 1 second |
| QoS Queue Depth | 10 |
| Language | Python |

## Technologies Used

- ROS 2
- Python
- rclpy
- std_msgs
- Ubuntu Linux

## Project Structure

```text
pub_sub_demo/
├── pub_sub_demo/
│   ├── __init__.py
│   ├── publisher.py
│   └── subscriber.py
├── resource/
├── test/
├── package.xml
├── setup.py
├── setup.cfg
├── .gitignore
└── README.md
```

## Installation and Execution

### 1. Clone the repository

```bash
cd ~/ros2_ws/src
git clone YOUR_REPOSITORY_URL
```

### 2. Build the package

```bash
cd ~/ros2_ws
colcon build --packages-select pub_sub_demo
```

### 3. Source the workspace

```bash
source install/setup.bash
```

### 4. Run the publisher

Open a terminal:

```bash
ros2 run pub_sub_demo publisher
```

### 5. Run the subscriber

Open another terminal and source the workspace:

```bash
source ~/ros2_ws/install/setup.bash
```

Then execute:

```bash
ros2 run pub_sub_demo subscriber
```

## Expected Output

**Publisher Terminal:**

```text
[INFO] Publishing: 0
[INFO] Publishing: 1
[INFO] Publishing: 2
[INFO] Publishing: 3
```

**Subscriber Terminal:**

```text
[INFO] Received: 0
[INFO] Received: 1
[INFO] Received: 2
[INFO] Received: 3
```

## Learning Outcomes

- Understanding ROS 2 nodes.
- Implementing Publisher and Subscriber communication.
- Working with ROS 2 topics.
- Using standard ROS 2 message types.
- Implementing periodic publishing using timers.
- Understanding basic ROS 2 Python package structure.
