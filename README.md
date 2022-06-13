# S.P.E.A.R.

This repo cointais the basic codes of the new version of the project.

# About the Project

S.P.E.A.R. project consist in a autonomous weapon station and sentry gun for low-medium caliber guns. Its based in three diferent control modes: Manual Mode using joystick, Auto Tracking Mode where the operator locks on a target and Surveillance Mode, where ir uses a trained model to recognize handguns to find and track possible targets.

# Instalation

The project runs on Python 3.7+, so you should download a stable version [here](https://www.python.org/downloads/). We also use Arduino [IDE](https://www.arduino.cc/en/software) to program and control the electrical and mechanical parts of the project. For computer vision we mainly use modified versions of OpenCV and YOLOv5, wich are also included in this repo and the requiremements are included bellow. 

The first step to install the project is to clone this repo via HTTPS, and install requirements.txt via pip using

```bash
git clone https://github.com/Alema1/spearproject.git  # clone
cd spearproject
pip install -r requirements.txt  # install
```
 The current version is configurated to run on Visual Studio.

# Hardware Info

Communication Protocol:

 SSP3

Joystick:

 Thrustmaster T.Flight HOTAS

Motors:

 3.2A Sanyo Denki Stepper Motor for the horizontal axis.
 2.4A Sanyo Denki Stepper Motor for the vertical axis.

Drivers:

 5A driver for the horizontal axis.
 4A driver for the vertical axis.
