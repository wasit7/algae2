#!/bin/bash
echo Deploying Django on Ubuntu16
sudo apt-get update
sudo apt-get install -y build-essential libssl-dev libffi-dev python-dev
sudo apt-get install -y python-pip
sudo pip install --upgrade pip
sudo apt-get install -y libopencv-dev python-opencv
yes w | sudo pip install -r requirements.txt
