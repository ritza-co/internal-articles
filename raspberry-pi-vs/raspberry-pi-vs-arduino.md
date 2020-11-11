# Raspberry Pi vs Arduino

## Introduction

The Raspberry Pi and the Arduino are often seen as the same thing whereas in fact they are two very different devices. Both come with General Purpose Input Output (GPIO) pins and are widely used to interact with other electronic devices such as sensors and motors; however, the Raspberry Pi is a fully fledged single-board computer (SBC) while the Arduino is simply a microcontroller that can handle only a single process at a time.

Both devices were designed as teaching tools for a wide variety of subjects including computer science and “internet of things” (IoT) applications. Over the years these devices have become increasingly powerful and today are widely used to develop proof-of-concept (POC) solutions that lay the foundation for much larger industrial applications.

## The Raspberry Pi

The Raspberry Pi was developed in the United Kingdom at the University of Cambridge’s Computer Laboratory in 2006 as a teaching tool for computer science students and was publicly released in 2012. It was developed to give students a cheap hackable computer on which they could safely tinker and test things out, allowing them to apply what they learn in a practical manner and experience first-hand the capabilities of computers. 

The Raspberry Pi is closed-source hardware and is produced only by the Raspberry Pi Foundation. Luckily there is a large community of engineers, enthusiasts and hobbyists who have created and shared ample resources like open-source projects and guides for you to learn from.

Being a fully functional computer, the Raspberry Pi has its own microprocessor and memory, and can run a variety of different operating systems. It is also equipped with USB ports, audio output, HDMI graphic output and networking capabilities such as Ethernet, Wi-Fi and Bluetooth. 

Although the Raspberry Pi comes with a lot of features out of the box, it does not have everything. Hundreds of expansion boards, called HATs (Hardware Attached on Top), have been developed to add more functionality to the Pi. You can find all kinds of HATs that fit on top of the existing pins and can be stacked to add features like screens, LoRa (Long Range) chips, or another Pi to build clusters.

The Raspberry Pi has its own flavor of the Linux OS called Raspberry Pi OS, previously known as Raspbian. Raspberry Pi OS comes pre-installed with software for education, programming and general use such as an Office suite, Scratch, Python, and Java. 

There are a variety of different models, the most popular today being the Raspberry Pi 3+, which is the model we will look at in this article.

### Strengths
- Stronger and quicker processor to run multiple software applications.
- Built-in networking capabilities: Ethernet, Wi-Fi and Bluetooth.
OS can be switched.
- Built-in audio output, camera port, multiple USB ports, and HDMI output.
- Great to use as a desktop computer, media device, or retro gaming console.
- A great device to start learning and experimenting with programming.
- Best for projects where you need to connect to the internet and run multiple programs at the same time.

### Weaknesses
- Time-consuming setup.
- Need extra components to get started (screen, mouse, keyboard, etc.).
- Need to install programs for specific use cases and keep them updated with the OS.
- Can be more expensive if you just need a basic microcontroller.
- Does not support analog input out of the box.
- Higher power usage and more difficult to connect to a battery.

## The Arduino

The Arduino was developed in Italy as a single-board microcontroller in the year 2000. It was designed to be a prototyping development board for connecting devices such as sensors and motors to a network. 

The main difference between the Arduino and the Raspberry Pi is that the Arduino is not a computer and cannot run its own OS. The Arduino is only part of a computer: a microcontroller that can run a single program at a time. The board comes with plenty of digital and analog I/O pins which can be connected to other electronic devices. 

When it comes to connecting everyday electronic devices to a system, collecting data with sensors, and controlling switches, the Arduino is the first choice for most. It is a simple plug-and-play device that can get your project started effortlessly by connecting it to a computer via USB, and loading your code through the Arduino IDE.

The Arduino has its own simplified version of the C++ programming language; however, it supports code written in C or C++ and there are some workarounds to make other programming languages work with it.

In order to add certain functionality to the Arduino, a lot of expansion boards and modules have been developed. These expansion boards are called shields and most of them were developed to easily add functionality by simply attaching them to the Arduino board. 

Unlike the Raspberry Pi, the Arduino is a fully open-source hardware and software project.

### Strengths

- Can connect analog components easily.
- Variety of shields that can add functionality.
- Easy to get started: just connect USB, load code, and run. No software or OS to be installed.
- Price is lower when you only need a microcontroller.
- Best for projects where you collect data from sensors and only need one program to work with the data.
- Low power usage and can easily be connected to a battery.

### Weaknesses 
- Limited resources and can only run one program at a time.
- No network connectivity out of the box.
- Bigger learning curve with C/C++ language.

## Side-by-side comparison

|                                    | Arduino Uno                                    | Raspberry Pi 3 Model B+                                            |
|------------------------------------|------------------------------------------------|--------------------------------------------------------------------|
| Price                              | $25                                            | $40                                                                |
| Size                               | 68.6 mm × 53.3 mm                              | 8.6 cm × 5.4 cm × 1.7 cm                                           |
| Memory                             | 2 KB                                           | 1 GB                                                               |
| Clock speed                        | 16 MHz                                         | 1.4 GHz                                                            |
| On-board network                   | None                                           | 2.4 & 5 GHz 802.11 b/g/n/ac Wi-Fi; Bluetooth 4.2; gigabit Ethernet |
| Multitasking                       | No                                             | Yes                                                                |
| Input voltage                      | 5 V                                            | 5 V                                                                |
| Flash                              | 32 KB                                          | SD card                                                            |
| GPIO (pins)                        | 20 GPIO (14 digital; 6 analog) (28 pins total) | 28 GPIO (0 analog) (40 pins total)                                 |
| Power output (pins)                | 40 mA                                          | 16 mA                                                              |
| Idle power usage                   | 50 mA                                          | 700+ mA                                                            |
| USB                                | 1; input only                                  | 4; peripherals OK                                                  |
| Operating system                   | None                                           | Linux distributions                                                |
| Integrated development environment | Arduino IDE                                    | Scratch, IDLE, Python, Java, anything with Linux support           |

## Which one to use?

Now that you have a better idea of what these devices are and what their purpose is you might have already concluded that the answer is: it depends.

Both devices can be used in similar projects; however, because they are very different devices, one might be better than the other depending on your project’s requirements. Keeping the requirements of your project in mind, consider these factors when making your choice: scalability, functionality, flexibility, cost, power requirements, environmental conditions, and storage capacity.

### Use the Raspberry Pi:

- If you want the functionality of a desktop computer or you want to use it as a media device with a screen, etc.
- If you are just starting out with programming and want to explore and learn different programming languages.
- If you have a need for more processing power, for example a central server, a network gateway, a web server, a media device, or a small desktop computer.
- If you want to learn or experiment with building a supercomputer. The Raspberry Pi is stackable which allows you to build clusters of multiple Raspberry Pis and learn how to combine the resources of many nodes.
- If you need to run specific software that the Arduino does not support.
- When you are planning to run multiple programs at once.
- If you are already proficient in the Python programming language.
- When the environment is easily accessible and has a sufficient and stable power source.
- In applications where processing is vital.
- If a system needs to collect data from multiple sensors, pull or push data to or from the internet, connect to wireless devices, or provide complex output on a display.
- If you are looking for an all-in-one solution.

### Use the Arduino:

- If you simply want to control some electronics.
- If you are just starting out with electronics and IoT use cases.
- If you are already proficient at C programming.
- If you want to write a program to it, connect a battery (solar charger) and place it somewhere with sensors or electronics attached that send the data back to a database or central server.
- When you only need to run one process and you want to leave it running repeatedly for an extended period of time without any issues.
- When the environment does not have a stable power supply and you want to incorporate a battery or solar panel.
- If you want to read analog sensors in real time. 

## Best of both worlds

While it is clear that these are two very different devices, they are often used together to take advantage of their respective strengths. 

Because the Raspberry Pi is a few thousand times more powerful than the Arduino, resources are often wasted when you use a Raspberry Pi to connect to a single sensor or run a single small program. However, this makes it the perfect candidate for controlling multiple Arduinos, connecting to the internet and running web applications of a complete IoT system.

A Raspberry Pi and an Arduino can easily be connected with the help of PySerial (https://pypi.org/project/pyserial/), a Python library for setting up serial communication. This allows for two-way communication where your more powerful Raspberry Pi can be used to manage multiple Arduinos.

Often the Raspberry Pi is used as the server and the Arduinos are connected to it as nodes. 

For example, you can have Arduinos connected to sensors to collect data which you send to a Raspberry Pi which then uses that data to send new instructions to more Arduinos connected to valves, motors, or other electronics.

## Conclusion

If you need processing power, want to run multiple processes at the same time, connect to the internet, or have the need for media capabilities then the Raspberry Pi is your best option.

If you want a quick startup, low power usage, easy connection of sensors and only need to run a single process at a time then the Arduino is the most viable option. 

If you are beyond learning the basics and you are looking to build a larger solution with multiple sensors and electronics then consider using both as a system.

It is up to you to decide which device aligns best with your requirements.

