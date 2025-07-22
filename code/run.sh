#!/bin/bash
python3 bluetooth.py
echo "Running Smart Speaker Bluetooth Controller..."
echo "Press Ctrl+C to stop."
trap "echo 'Stopping...'; exit" SIGINT SIGTERM
while true; do
    sleep 1
done
echo "Smart Speaker Bluetooth Controller stopped."
exit 0