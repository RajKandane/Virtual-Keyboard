# HUMAN-COMPUTER INTERACTION USING ON-AIR VIRTUAL KEYBOARD
AUG 2022 - JUN 2023

# Virtual Keyboard Demo

Check out the On-Air Virtual Keyboard in action on YouTube:

[![Virtual Keyboard Demo](https://img.youtube.com/vi/hEfXnnKTFzQ/0.jpg)](https://youtu.be/hEfXnnKTFzQ)


## Project Overview:
The On-Air Virtual Keyboard is a cutting-edge project that aims to revolutionize human-computer interaction by developing a touchless virtual keyboard. The project utilizes advanced computer vision and machine learning techniques to recognize finger movements and gestures in the air and translate them into keyboard input. The touchless interface offers a convenient and hygienic alternative to physical keyboards, making it suitable for various applications, including smart devices, virtual reality, and interactive displays.

## Project Objectives:
1. Develop a user-friendly interface with adaptive key size and centroid distance between keys for improved usability.
2. Implement a finger action detection system for precise in-air typing interactions.
3. Integrate computer vision algorithms to accurately recognize and interpret finger movements and gestures.
4. Create a virtual keyboard application that can seamlessly replace physical keyboards for typing and input commands.
5. Evaluate the performance and usability of the On-Air Virtual Keyboard through user testing and feedback.

## Project Timeline

- August 2022: Project Planning and Research
- September 2022: Data Collection and Preparation
- October 2022: Model Development and Training
- November 2022: Virtual Keyboard Interface Design
- December 2022: Integration and Testing
- January 2023: Performance Optimization
- February 2023: Documentation and Final Report
- March 2023: Presentation and Review
- April 2023: Final Submission
- May 2023: Project Evaluation and Analysis
- June 2023: Project Conclusion and Wrap-up

## Related Work

Several studies and papers have investigated virtual keyboards and their design frameworks:

- Smith and Johnson compared different virtual keyboards on mobile devices, considering factors such as typing speed and accuracy.
- Sridhar et al. presented vision-based cursor control using hand motion, which has applications in virtual keyboards.
- Kim and Lee proposed a touchless virtual keyboard that uses hand and fingertip location for text input.
- Chen and Chen surveyed virtual keyboards, discussing design frameworks, advantages, and limitations.
- Lee and Park reviewed virtual keyboard technology, including challenges and usability considerations.
- Zhang and Wang compared touchscreen and physical keyboards for mobile text entry tasks.

## Requirement Analysis

The system must:

1. Accurately recognize and interpret different finger movements and gestures, such as tapping, swiping, and pinching, for diverse in-air typing interactions.
2. Provide a user-friendly and customizable virtual keyboard layout with adjustable key sizes and distances for improved user experience.
3. Be responsive with low latency to ensure a real-time typing experience, allowing users to type effortlessly.
4. Offer a secure input method to protect sensitive data during typing sessions, preventing unauthorized access.
5. Accommodate different hand sizes and shapes to ensure inclusivity and accessibility for all users.
6. Be compatible with various devices, including mobile phones, tablets, laptops, and desktop computers, enhancing versatility.
7. Operate effectively in different lighting conditions and environments, ensuring reliable performance in various settings.


## System Design

The On-Air Virtual Keyboard's architectural design includes several components:

1. Camera: Captures live video feed of the user's hand and fingers for input.
2. Finger Motion Estimation: Estimates finger motion based on the camera input using computer vision algorithms.
3. Touch/Non-touch Classification: Classifies whether a finger is touching a virtual key or not.
4. Virtual Keyboard Controller: Identifies the virtual key being touched and generates corresponding keystrokes.
5. Display Keystroke: Sends keystrokes to the target application or device and displays them on the screen.

## Algorithmic Description of Each Module

1. Hand Tracking Module: Processes video frames to detect and extract landmarks from hands.
2. Utils: Provides image processing utilities for the classification model.
3. Touch/Non-touch Classifier: Uses SVM classification to determine if a finger is touching a virtual key or not.
4. Virtual Keyboard Controller: Identifies touched virtual keys and generates keystrokes.
5. Display Keystroke: Sends keystrokes to the target application and displays them on the screen.

## Technologies and Tools

- Programming Languages: Python (for computer vision and machine learning), JavaScript (for user interface)
- Libraries: OpenCV, Mediapipe, TensorFlow, Tkinter, pynput, NumPy, PIL (Python Imaging Library)
- Frameworks: Convolutional Neural Network (CNN) for image processing and gesture recognition
- Hardware: Webcam or camera for video input

## Project Demo

A demo of the On-Air Virtual Keyboard is available on YouTube [HUMAN-COMPUTER INTERACTION USING ON-AIR VIRTUAL KEYBOARD](https://youtu.be/hEfXnnKTFzQ). The video showcases the touchless typing capabilities and the user-friendly interface. The demo includes a performance evaluation comparing the virtual keyboard to traditional physical keyboards.

## Installation Guide

To use the On-Air Virtual Keyboard, follow these steps:

1. Create a Python environment by installing the PyCharm application on your system.
2. Install all the dependencies, such as Cvzone, Mediapipe, Tkinter, Pynput, Math, Numpy, and OpenCV.
3. Select the project using the PyCharm application.
4. Run the project to use the touchless virtual keyboard.


**References:**

[1] Smith, J., & Johnson, L. (2018). A Comparative Analysis of Virtual Keyboards on Mobile Devices. International Journal of Mobile Devices, Wearable Technology, and Human-Computer Interaction, 10(1), 47-58.

[2] Sridhar, K., Subramanian, S., & Rajan, R. (2019). Vision-Based Cursor Control Utilizing Hand Motion. Proceedings of the International Conference on Human-Computer Interaction, 175-187.

[3] Kim, H., & Lee, C. (2020). Touchless Virtual Keyboard Using Hand and Fingertip Location. Journal of Human-Computer Interaction, 15(3), 210-223.

[4] Chen, X., & Chen, Y. (2017). A Survey of Virtual Keyboards: Design Frameworks, Advantages, and Limitations. International Journal of Human-Computer Interaction, 11(2), 143-159.

[5] Lee, S., & Park, J. (2018). A Review of Virtual Keyboard Technology: Design, Challenges, and Usability. Journal of Human-Computer Interaction, 14(4), 315-328.

[6] Zhang, Y., & Wang, Y. (2021). Comparison of Touchscreen and Physical Keyboards for Mobile Text Entry. Proceedings of the International Conference on Human-Computer Interaction, 267-279.



## Additional Information

### Implementation Details

The On-Air Virtual Keyboard project utilizes advanced computer vision and machine learning techniques to recognize finger movements and gestures in the air and translate them into keyboard input. The game logic and finger action detection system are implemented in Python, leveraging libraries such as OpenCV, Mediapipe, TensorFlow, Tkinter, pynput, NumPy, and PIL (Python Imaging Library) to handle real-time hand tracking and classification.

### Future Enhancements

The current version of the On-Air Virtual Keyboard is a cutting-edge project that aims to revolutionize human-computer interaction. For future enhancements, some possible features to consider are:

- Refining the user interface to improve usability and aesthetics.
- Expanding the keyboard's language support to include multiple languages.
- Implementing gesture customization, allowing users to define their own gestures for specific commands or actions.
- Integrating the virtual keyboard with other applications and platforms for broader accessibility.

## Contribution Guidelines

Contributions to the On-Air Virtual Keyboard project are highly appreciated. If you wish to contribute, please feel free to submit a pull request. Whether it's fixing bugs, adding new features, or improving documentation, every contribution is valuable.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details. 

## For more information or inquiries, please contact:

- LinkedIn: [RITESHKUMAR KANDANE](https://www.linkedin.com/in/dkteriteshkumarkandane/)

---
