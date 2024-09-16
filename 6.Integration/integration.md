By: Zaynap Ahmad

# Integration Session

## Our Outlines:

1. System Components
2. Software Integration
3. Hardware - Software Integration
4. Hands-On Activity

## **1. System Components**

### System Overview

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

<div align="center">
  <img src="images/udacity self driving.png" alt="System Components Diagram" style="width: 100%; max-width: 1000px;">
</div>

## **2. Software Integration**

### Why Integrate Software Components?

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
    A[Software Integration ] 
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
