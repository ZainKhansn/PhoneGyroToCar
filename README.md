GO FOLLOW COLLABORATOR @Jaganmranal 

Android Phone Gyro-controlled Car using Raspberry Pi
This project aims to create a car controlled by the built-in gyroscope of an Android phone, powered by a Raspberry Pi. It utilizes two motors connected to an L298N motor driver for precise control and movement. This project was developed in collaboration with Jagan Mranal as part of our Computer Science final project.

Features
Gyroscope Control: The car can be controlled by tilting the Android phone in the desired direction using its built-in gyroscope. This allows for an intuitive and immersive control experience.

Raspberry Pi Power: The Raspberry Pi serves as the brain of the project, processing the gyroscope data from the Android phone and translating it into motor commands to control the car's movement.

L298N Motor Driver: The two motors of the car are connected to an L298N motor driver, which provides efficient and reliable control. The motor driver allows us to regulate the speed and direction of the motors, enabling smooth and precise movements.

Getting Started
To set up the project, follow these steps:

Hardware Setup: Connect the L298N motor driver to the Raspberry Pi according to the provided pinout diagram. Connect the two motors to the motor driver, ensuring correct polarity.

Software Installation: Install the necessary libraries and dependencies on the Raspberry Pi, as mentioned in the project's documentation. These libraries will enable communication between the Android phone and the Raspberry Pi.

Android App Installation: Install the custom Android app on your phone, which will send gyroscope data to the Raspberry Pi over a wireless connection. The app can be found in the project's repository.

Calibration: Calibrate the gyroscope in the Android app to ensure accurate control. Follow the instructions in the app for the calibration process.

Connectivity: Establish a connection between the Android phone and the Raspberry Pi. Ensure that both devices are connected to the same network and configure the necessary IP addresses and ports as per the project documentation.

Launch the Project: Start the project script on the Raspberry Pi. The script will listen for gyroscope data from the Android app and translate it into motor commands, controlling the movement of the car.

Contributors
Jagan Mranal: Collaborated on the project, contributed to the hardware setup and motor control aspects (Collaboration on coding and electrical engineering).

Zain: Developed the Android app, integrated the gyroscope control, and handled the communication between the Android phone and the Raspberry Pi plus collaboration on electrical engineering and coding motors).

