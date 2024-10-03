By: Zaynap Ahmad

# Integration Session

## Our Outlines:

* **robotic system archetecture**
* **System Components**
* **Software Integration**
* **Hardware - Software Integration**
* **Hands-On Activity**

## teleoperational vs autonomous robots

<div align="center">
  <img src="images/High-level-architecture-of-a-UAV-system.png" alt="System Components Diagram" style="width: 100%; max-width: 1000px;">
</div>

Teleoperational Robots are controlled directly by a human. The operator uses a remote control or a computer to send commands. This type of robot is often used in situations where it might be dangerous for a person to be present, like in bomb disposal or remote surgery. The operator must stay focused and react quickly, as they are responsible for every action the robot takes. However, teleoperational robots can be slower and have limitations in their speed and range due to the reliance on human control and the need for a stable communication link.

<div align="center">
  <img src="images/The-software-architecture-of-our-UAV-inspection-system.png" alt="System Components Diagram" style="width: 100%; max-width: 1000px;">
</div>

On the other hand,autonomous robtos  can operate on their own without human control. They use sensors to understand their environment and make decisions based on what they see. These robots can adapt to changes around them and do not need someone to guide them constantly. They are often used in applications like self-driving cars or robotic vacuum cleaners.
in this system i need the system it self to determine its action

### Key Differences

1. **Control**:

   - **Teleoperational Robots**: A human operates these robots by sending commands. The operator must pay close attention and be skilled. Because the robot relies on human input, it can be slower and may not react as quickly to changes.
   - **Autonomous Robots**: These robots can make decisions on their own and act without human control. They use sensors to understand their environment and can respond quickly to changes around them.
2. **Communication**:

   - **Teleoperational Robots**: They need a strong communication link with the operator. If the connection is lost, the robot might stop working or become hard to control. This limits how far away they can operate.
   - **Autonomous Robots**: They don’t need to communicate with a human to function. They process information and react to their surroundings independently, which gives them more freedom to move around.
3. **Software Complexity**:

   - **Teleoperational Robots**: The software is simpler and focuses on allowing the operator to control the robot easily. It doesn’t have to make complex decisions because a person is in charge.
   - **Autonomous Robots**: Their software is more complex, using advanced technology to help the robot see, think, and learn from its experiences.

## our system archetechure

<div align="center">
  <img src="images/software pipeline.png" alt="System Components Diagram" style="width: 100%; max-width: 1000px;">
</div>

### Components Description

#### 1. Perception

- **Description:** Enables the robot to sense and interpret its environment.
- **Input:** Raw sensor data (e.g., camera images, LIDAR data)
- **Output:** Processed environmental data (e.g., detected objects, distance measurements)

#### 2. SLAM (Simultaneous Localization and Mapping)

- **Description:** Builds a map of the environment while tracking the robot's location.
- **Input:** Sensor data and motion data
- **Output:** Environment map and robot’s position

#### 3. Path Planning

- **Description:** Determines the optimal route from the current location to the destination.
- **Input:** Environment map and goal coordinates
- **Output:** Planned path (waypoints or trajectory)

#### 4. Control

- **Description:** Manages the robot's movements and actions based on the planned path and feedback.
- **Input:** Planned path and sensor feedback
- **Output:** Actuator commands (e.g., motor speeds, steering angles)

### this how the whole system work but how the system repspond to the environment by any sequance ?

The relationship between the computational requirements for coming up with an an appropriate response to a given environmental challenge and the time allowed by the circumstances is at the heart of designing robot architectures

### sort of archetectures allow for timely response across environment ?

Murphy(2000) describes the range of current architectures (or  *paradigms* ) in terms of the relationships between three primitives,  *sense* , *plan* and *act* and in terms of how sensory data is processed and propagated through the system.

<div align="center">
  <img src="images/paradigms.gif" alt="paradigms" style="width: 100%; max-width: 1000px;">
</div>

### hierarchical appraoch :

he *hierarchical paradigm* is a bit of a caricature. It was however the dominant paradigm in the early days of AI robotics when much of the focus was on robot planning. The emphasis in these early systems was in constructing a detailed world model and then carefully planning out what steps to take next. The problem was that, while the robot was constructing its model and deliberating about what to do next, the world was likely to change. So these robots exhibited the odd behavior that they would look (acquire data, often in the form of one or more camera images), process and plan, and then (often after a considerable delay) they would lurch into action for a couple of steps before beginning the cycle all over again. [Shakey](http://www.frc.ri.cmu.edu/~hpm/book98/fig.ch2/p027.html) a robot developed at the Stanford Research Institute in the 1970s was largely controlled by a remote computer connected to the robot by a radio link; Shakey exhibited this sort of look-and-lurch behavior as it contemplated moving blocks around to achieve a goal

<div align="center">
  <img src="images/horizontal.gif" alt="horizontal" style="width: 100%; max-width: 1000px;">
</div>

<div align="center">
  <img src="images/cc64e1e5-shakeysriinternational1-1487364021434.webp" alt="shaky" style="width: 100%; max-width: 1000px;">
</div>

### Reactive Systems

An alternative to the hierarchical paradigm with its horizontally organized architecture is called the *reactive paradigm* and is labeled as such above. Adherents of the reactive paradigm organize the components vertically so that there is a more direct route from sensors to effectors.

<div align="center">
  <img src="images/vertical.gif" alt="vertical" style="width: 100%; max-width: 1000px;">
</div>

Note that in this vertical decomposition there is the potential for contention over the effectors. Just as in the example of steering a car to exit from the highway while avoiding an accident with the car in the lane to your right, there is contention among the various components, avoiding, exploring, wandering, planning, for taking control of the robots actuators. Brooks suggests that we solve the problem of contention by allowing components at one level to *subsume* components at a lower level. Thus he called his approach the  ***subsumption architecture*** .

In the subsumption architecture, components behaviors are divided into layers with an arbitration scheme whereby behaviors at one level can manipulate what behaviors at a lower level can see or do. Brooks called the most primitive components of his architecture  *modules* . Each module has inputs, outputs and a reset. A module at a higher level can suppress the input of a module at a lower level thereby preventing the module from seeing a value at its input. A module can also inhibit the output of a module at a lower level thereby preventing that output from being propagated to other modules.

The modules are meant to be simple computationally and so it is reasonable to think of them as circuits or finite state-machines. Brooks assumed that they were augmented finite state controllers. The reset would cause the controller to return to its initial state. Once set in motion the controllers would continuously transition from one state to the next. The transitions can be determined in part by reading from the inputs and some internal state and of course by referring to the present state of the controller. Brooks also allows controllers to have an internal clock or timer and so, for example, they can execute a wait. Here are the basic transition types allowed in specifying the transition function of a finite-state controller.

* **Output** - a transition can compute a value as a function of the module's inputs and internal state and then send the value to one of its outputs before entering a specified state
* **Side effect** - a transition can set one of the module's instance variables (internal state) to some value computed as a function of the module's inputs and internal state; the module then enters a specified state
* **Conditional dispatch** - a predicate on the module's inputs and instance variables is evaluated and depending on the outcome the module enters one of two specified states
* **Event dispatch** - a sequence of conditions and states to branch to is specified; the conditions are then monitored continuously until a condition is met and then the module transitions to the corresponding state

<div align="center">
  <img src="images/avoid.gif" alt="vertical" style="width: 100%; max-width: 1000px;">
</div>

### hybrid archetecute :

think and act independantly and concerntly , its a combination of reactive and delibrative

its called the three layerd system (reactive layer , delibretive layer , middle layer )

<div align="center">
  <img src="images/hybrid.png" alt="vertical" style="width: 100%; max-width: 1000px;">
</div>

### The Importance of Integration

We've explored the different architectures for robot control, from the slow and deliberate hierarchical approach to the fast and reactive approach. But there's a key concept that ties them all together: integration.

As Rodney Brooks famously said, **"Robotics is the art of integration."**   A robot is not simply a collection of parts – it's a complex system where hardware, software, sensors, and actuators all work together seamlessly. The success of a robot hinges on how well these elements are integrated.

Integration is crucial for several reasons:

* **Efficiency**: A well-integrated system allows for smooth information flow between components, leading to faster response times and efficient operation.
* **Performance**: When everything works together in harmony, the robot can perform its tasks more accurately and reliably.
* **Flexibility:** Modular and well-integrated systems can be easily adapted to new tasks or environments by adding or replacing components.
* **Scalability**: Integration allows for building complex robots with many functionalities by seamlessly integrating additional components

<!-- <style>
    .mermaid {
        max-width: 200%;
        width: 200%; /* Make the diagram take full width */
        height: auto; /* Adjust height automatically */
    }
    /* Optional: Increase the font size if needed */
    .mermaid .node rect {
        width: 200px; /* Increase node width */
        height: auto; /* Adjust node height automatically */
    }
    .mermaid .node text {
        font-size: 16px; /* Increase font size for better readability */
    }
</style> -->

```mermaid
graph TD;
    A[system Integration ] 
    A --> B[Performance]
    A --> C[Flexibility]
    A --> D[Dependability]
  
    B --> E[System Integration]
    E --> F[Smooth Interaction]
    F --> G[Efficient Memory]

    C --> H[Easy Updates]
    H --> I[New Features]
    I --> J[System Growth]

    D --> K[Steady Results]
    K --> L[Reliable Operation]
    L --> M[Few Errors]

 
    classDef centralNode fill:#e0e0e0,stroke:#333,stroke-width:1px,font-size:14px,color:#000;
    classDef branchNode fill:#cce5ff,stroke:#333,stroke-width:1px,font-size:13px,color:#000;
    classDef detailNode fill:#fff,stroke:#333,stroke-width:1px,font-size:12px,color:#000;

    class A centralNode;
    class B,C,D branchNode;
    class E,H,K detailNode;
    class F,G,I,J,L,M detailNode;
```

#### two main steps in integration :

* software integration
* hardware - software integration

## software integration

> **to integrate the software components there are many archetectures to use**

**Software architecture** is the high-level structure of a software system, defining how components are organized and interact with each other. In the context of robotics, the software architecture plays a crucial role in determining how different software modules are integrated to control the robot's behavior.

image for (software arch)

### the most used  appraches for robotics  :

### Object-Oriented Robotics (OO-R)

**Object-Oriented Robotics (OO-R)** is a design paradigm that applies object-oriented programming (OOP) principles to the development of robotic systems. The focus of OO-R is on creating modular, reusable, and maintainable components that can interact with each other effectively. This approach offers several advantages in the design and implementation of robotic systems.

[example of software archetecture with OO-R](codes/OO-R_psudeoCode.py)

```mermaid
flowchart LR
    subgraph Robot Controller
        A(Robot Controller)
    end    subgraph Sensors
        B(Camera) --> A
        C(LiDAR) --> A
    end    subgraph Actuators
        D(Motor) --> A
        E(Servo) --> A
    end    subgraph Perception
        F(Perception Module) --> A
    end    subgraph Planning
        G(Planning Module) --> A
    end    subgraph Execution
        H(Execution Module) --> A
    end
style A fill:#f0f0f0, stroke:#ccc, stroke-width:2px, font-size:12px, text-align:center
style B, C, D, E, F, G, H fill:#e0e0e0, stroke:#ccc, stroke-width:1px, font-size:12px, text-align:center

```

### Component-Based Robotics (CB-R)

**Component-Based Robotics (CB-R)** is an architectural approach that focuses on building robotic systems using interchangeable and reusable components. This methodology emphasizes modular design, where each component encapsulates specific functionality and can communicate with other components through well-defined interfaces. CB-R enhances flexibility, scalability, and maintainability in robotics development.

[example of software archetecture with CB-R](codes/CB-R_psudeoCode.py)

chart

### Service-Driven Robotics (SD-R)

**Service-Driven Robotics (SD-R)** is an architectural paradigm that focuses on building robotic systems as collections of services that can be independently developed, deployed, and consumed. This approach emphasizes the use of services as discrete units of functionality, promoting interoperability and scalability in robotic applications.

[example of software archetecture with SB-R](codes/SB-R_psudeoCode.py)

chart

after understanding what are the archetectures we could use to build the software , there are frameworks helps us to do this

### Frameworks

<div align="center">
  <img src="images/software framework .png" alt="System Components Diagram" style="width: 100%; max-width: 1000px;">
</div>

**Frameworks** are reusable software platforms that provide a foundation for building applications. They offer pre-built components, tools, and guidelines to streamline the development process and enhance code quality. In the field of robotics, frameworks play a crucial role in simplifying the development of complex software systems.

write that there are frameworks for application , middleware and so on

**Key benefits of using frameworks in robotics:**

* **Efficiency:** Frameworks provide pre-built components and tools, saving development time and effort.
* **Modularity:** Frameworks often promote modular design, making it easier to manage and maintain code.
* **Standardization:** Frameworks can establish common standards and conventions, improving code readability and maintainability.
* **Community Support:** Many frameworks have active communities that provide resources, documentation, and support.

### frameworks used in robotics :

| Framework                 | Overview                                                 | Key Features                                             | Architecture Type                | Use Cases                                   |
| ------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------- | ------------------------------------------- |
| **ROS**             | Open-source robot software framework                     | Modular design, extensive libraries, strong community    | Component-based                  | Research, prototyping, complex systems      |
| **ROS 2**           | Enhanced successor to ROS for real-time applications     | Improved communication, security, multi-platform support | Component-based, Service-based   | Industrial applications, autonomous systems |
| **OpenRTM-aist**    | Framework for robot system integration                   | Real-time operations, easy component integration         | Component-based                  | Academic research, complex systems          |
| **Webots**          | Robot simulation software                                | User-friendly, extensive API                             | OOP (Object-oriented)            | Education, testing, prototyping             |
| **Choreonoid**      | Flexible robotics simulation framework                   | Component-based, supports motion planning                | Component-based                  | Research, prototyping, testing              |
| **CoppeliaSim**     | Versatile robot simulation environment                   | Integrated simulation, Lua scripting                     | OOP, Scripting                   | Algorithm development, testing              |
| **OpenAI Gym**      | Toolkit for reinforcement learning algorithms            | Environment integration                                  | Modular, API-driven              | Reinforcement learning applications         |
| **MATLAB/Simulink** | High-level control system programming                    | Block diagram environment, extensive toolboxes           | Block-based (Visual programming) | Prototyping, simulations                    |
| **ROS for Windows** | ROS version adapted for Windows                          | Windows compatibility, easier integration                | Component-based                  | Windows-based robotic software              |
| **RoboDK**          | Simulation and offline programming for industrial robots | Easy integration with multiple languages                 | OOP, API-driven                  | Industrial robot programming, simulation    |

add these : Yarp[5], Carmen[6], Player/Stage[

## ROS2

finished the software lets put our software into work

### what is ROS ?

The meaning of the acronym ROS is Robot Operating System. It is not an operating system that replaces Linux or Windows but a middleware1 that increases the system’s capabilities to develop Robotic applications.

The number 2 indicates that it is the second generation of this middleware

Robot Operating System (ROS) is a set of open source algorithms, hardware driver software and tools developed to develop robot control software. Even though it has operating system in its name it is not an operating system[4]. It is

* Communication System (Publish Subscribe and Remote Method Invocation),
* Framework & Tools (Build system & dependency management, Visualization, Record and Replay)
* Ecosystem (Language bindings, Drivers, libraries and simulation (Gazebo)).

**currently ros has tow generations ROS1 and ROS2 each with its distributions**

* ROS1 was used moslty for education and acadmeic research
* ROS2 is for commercial robots

ROS includes mature open source libraries to be used for navigation, control, motion planning, vision and simulation purposes. The 3D visualization tool called RVIS is an important tool used with ROS. Similarly, the simulation tool called Gazebo is seen as a usefull tool for robot developers. Apart from this, Open CV library is a library used for detection purposes in ROS 2

<div align="center">
  <img src="images/ros2_libraries.webp" alt="ros2 libraries" style="width: 70%; max-width: 800px;">
</div>

## ROS 2 Architecture

The ROS 2 has distributed real-time system architecture. Sensors in robots, motion controllers, detection algorithms, artificial intelligence algorithms, navigation algorithms, etc are all components (called as node) of this distributed architecture. The DDS middleware selected with ROS 2 for data exchange enables these components to communicate with each other in a distributed environment.

### different between ros1 and ros2

<div align="center">
  <img src="images/different_betweenros1andros2.png" alt="ros1 and ros2 " style="width: 70%; max-width: 800px;" >
</div>

**Compared with ROS1, the main differences are** :

* ROS1 mainly supports Linux-based operating system.
* ROS2 provides more portability of deployment on underlying operating systems, such as Linux, Windows, Mac, and RTOS.
* ROS data transport protocol uses TCPROS/UDPROS, and communication is highly dependent on the operation of Master node.
* Communication in ROS2 is based on DDS (Data Distribution Service) standard, enhancing fault tolerance capabilities.
* Intra-process in ROS2 provides more optimized transmission mechanism.

### ROS2 has three main dimentions

#### The Community:

 The ROS community is a fundamental element when developing applications for robots with this middleware. In addition to providing
technical documentation, there is a vast community of developers who contribute with their own applications and utilities through public repositories, to
which other developers can contribute. Another member of the community may
have already developed something you need.

#### Computation Graph:

The Computational Graph is a running ROS 2 application.
This graph is made up of nodes and arcs.
The Node, the primary computing units in ROS 2, can collaborate with other nodes using several diferent communication paradigms to compose a ROS 2 application.
This dimension also addresses the monitoring tools, which are also nodes that are inserted in this graph.

#### The Workspace:

The Workspace is the set of software installed on the robot
or computer, and the programs that the user develops. In contrast to the Computational Graph, which has a dynamic nature, the Workspace is static. This
dimension also addresses the development tools to build the elements of the
Computational Graph.

**we will proceed with the comoutaion graph**

#### how the node could talk to each other :

A node can access the Computation Graph and provides mechanisms to communicate with other nodes through 3 types of paradigms:

#### Publication/Subscription:

It is an asynchronous communication, where N nodes publish messages to a topic that reaches its M subscribers.
A topic is like a communication channel that accepts messages of a unique type.
This type of communication is the most common in ROS 2.
A very representative case is the node that contains the driver of a camera that publishes images to a topic.
All the nodes in a system needing images from the camera to carry out their function subscribe to this topic.

image

code example

#### Services:

It is a asynchronous communication4 in which a node requests another node and expect an inmediate response.
This communication usually requires an immediate response so as not to afect the control cycle of the node that calls the service.
An example could be the request to the mapping service to reset a map, with a response indicating if the call succeeded.

image

code example

#### Actions:

These are asynchronous communications in which a node makes a request to another node.
These requests usually take time to complete, and the calling node may periodically receive feedback or the notifcation that it has fnished successfully or with some error.
A navigation request is an example of this type of communication. This request is possibly time-consuming, whereby the node requesting the robot to navigate should not be blocked while completing.

image

code example 

### this how the nodes could talk to each other but how the node actually works ?

The function of a node in a computational graph is to perform processing or control.
Therefore, they are considered active elements with some alternatives in terms of their execution model:

#### Iterative execution:

It is popular in the control software for a node to execute its control cycle at a specifc frequency.
This approach allows controlling how many computational resources a node requires, and the output fow remains constant.
For example, a node calculating motion commands to actuators at 20 Hz based on their status.

code examble and image

#### Event-oriented execution:

The execution of these nodes is determined by the frequency at which certain events occur, in this case, the arrival of messages at this node.
For example, a node that, for each image it receives, performs detection on it and produces an output.
The frequency at which an output occurs depends on the frequency at which images arrive.
If no images reach it, it produces no output.

code example and image 

### layed archetecture

<div align="center">
  <img src="images/ros2layers.png" alt="ros2 archetecture" style="width: 70%; max-width: 800px;" >
</div>

### DDS

ROS 2 uses DDS as its middleware. DDS reduces coupling, increases scalability, and improves performance, reliability, security, and flexibility

DDS used moslty in defense industry

ROS 2 has provided its own abstraction layer (rmw) on top of DDS instead of directly using the DDS middleware. Thus, the details of the DDS middleware interface are abstracted from the user.  =In the current ROS 2 versions, Fast-DDS comes as the standard DDS version

<div align="center">
  <img src="images/dds-overview.jpg" alt="ros2 dds overview" style="width: 70%; max-width: 1000px;">
</div>

### ROS2 client library

ROS 2 applications access ROS 2 features through the ROS Client Library (RCL) client library. The Rcl library is written in C language and on it there are Rclcpp client libraries for C ++ language and Rclpy for Python language. There are independently written ROS 2 client libraries in other languages such as Java, Go. The client library is primarily provided with the standard interface required to exchange data with Topic and Service approaches over ROS 2. In addition, the ROS2 library has capabilities to provide operating system abstraction and ready-made micro-architectural structures.

<div align="center">
  <img src="images/DDS_and_clientlib.webp" alt="ros2 dds and clientlib" style="width: 70%; max-width: 500px;">
</div>

## embedded boards used in robotics



## hardware - software integration

<div align="center">
  <img src="images/hardware-software.png" alt="system archetcture" style="width: 80%; max-width: 1000px;">
</div>

## **references :**

4.https://medium.com/software-architecture-foundations/robot-operating-system-2-ros-2-architecture-731ef1867776
