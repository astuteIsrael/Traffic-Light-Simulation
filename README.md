# Traffic Light Simulation
## Project Overview
This project implements a simple traffic light system simulation using Python. The traffic light has three states: Red, Yellow, and Green. The light transitions between these states at specific intervals to emulate the behavior of a real-world traffic light. Each phase of the light lasts for a fixed number of seconds:

1. Red: 5 seconds
2. Yellow: 2 seconds
3. Green: 5 seconds
The simulation runs for a specified number of cycles (default is 3) and then stops.

## Features
1. Three traffic light states: Red, Yellow, and Green.
2. Automatic transitions between states with delays to simulate real traffic light timings.
3. A loop that repeats the traffic light cycle for a given number of times.
4. Customizable number of cycles before the program stops.

## Customization
- Cycles: The number of times the traffic light sequence repeats can be modified by passing a custom value to the TrafficLight constructor.
- Timing: The duration of each light can be adjusted by changing the time.sleep() values within the respective methods.

## Future Improvements
- Add a pedestrian crossing signal.
- Implement a graphical user interface (GUI) to visualize the traffic light changes.
- Introduce dynamic timing based on traffic conditions.
