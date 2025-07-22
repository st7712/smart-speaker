#!/bin/bash

echo "Installing Smart Speaker (Bluetooth Sink + GPIO Controls)..."

# Update & install dependencies
sudo apt update
sudo apt install -y pulseaudio pulseaudio-module-bluetooth bluez python3-pip playerctl

# Enable Bluetooth & PulseAudio services
sudo systemctl enable bluetooth
sudo systemctl start bluetooth

# Install Python libs
pip3 install -r requirements.txt

# Configure PulseAudio as A2DP Sink
mkdir -p ~/.config/systemd/user

# Enable Bluetooth A2DP module
echo "Configuring PulseAudio A2DP..."
pactl load-module module-bluetooth-discover
pactl load-module module-bluetooth-policy

# Set Bluetooth device name
sudo hostnamectl set-hostname SmartSpeaker
sudo sed -i '/^#Name = .*/c\Name = SmartSpeaker' /etc/bluetooth/main.conf

# Restart Bluetooth to apply name
sudo systemctl restart bluetooth

# Setup systemd service for bluetooth.py
sudo tee /etc/systemd/system/bluetooth-controller.service > /dev/null <<EOF
[Unit]
Description=Smart Speaker Touch Controller
After=bluetooth.target network.target sound.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/pi/smart-speaker/bluetooth.py
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl enable bluetooth-controller

echo "Installation done!"
echo "Your Raspberry Pi will now show up as 'SmartSpeaker' in Bluetooth."
echo "To manually run: ./run.sh"
