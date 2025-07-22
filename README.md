# DIY smart speaker

This is a Wi-Fi speaker with Bluetooth functionality, that is made for home use, powered by a Raspberry Pi.
The speaker will be able to stream music through Spotify (or you will be able to connect to it using Bluetooth).
Users can adjust settings themselves, or add special features they might like (making it a nice alternative to speakers like Sonos). On top of that, users can hook up any kind of speaker onto the DAC, so it can become a smart subwoofer, or a waterproof outdoor speaker.

## The actual speaker I will be making will consist of:

- Small subwoofer speaker
- Two midrange driver
- Two tweeters
- There will also be a DAC for the RPI, two amplifiers for the speakers and other components (power supply to power the whole speaker, a voltage step down regulator to power the RPI, LED's and touch sensors to control playback and get a visible response that something changed, cables and protoboard to connect everything)

## Why did I make this?

I wanted a high quality, bass-heavy smart speaker, while also learning new things about creating electronics and programming real-world devices. I also like working with audio and speakers, so this also covers one of my interests. I also want to have full control over it (the EQ and other settings) so I can experiment with it however I want.
I also built a custom mobile app in the past, which can integrate and pair speakers for future control and music streaming, which I wanted to try to make work in the future, and learn new stuff on the way.

## Images

### Wiring diagram for the speaker prototype

<img width="1760" height="1014" alt="image" src="https://github.com/user-attachments/assets/1c621f33-9654-4e18-9d37-58a0f77500ec" />

The black lines are generic wires, red and black lines are live + neutral wires and the purple lines are speaker wires connecting the speakers.
Then there are connections for the LED's and touch sensors, which are a bit chaotic, but it's just a 5V rail for the touch sensors ran down (they need 5V to function) with a GND rail also for the touch sensors and the LED's. Then each LED is connected to an output pin of the RPI, so it's able to turn them on independently (right there will be a 150 Ohm resistor in series), and each touch sensor is also connected to an input pin of the RPI, so that it can read when the touch sensor is activated.

## Bill of materials (BOM)

| Item                                | Quantity | Total Price (CZK) (with shipping) | Total Price (USD) (with shipping)             | Link                                                                                                                                                                                      |
| ----------------------------------- | -------- | --------------------------------- | --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Raspberry PI 5 4GB                  | 1        | 1648                              | 78,32                                         | [Link](https://rpishop.cz/raspberry-pi-5/6497-raspberry-pi-5-4gb-ram.html)                                                                                                                |
| SAL 50W subwoofer driver            | 1        | 369,14                            | 17,54                                         | [Link](https://www.ame.cz/Elektronika/Reproduktory-mikrofony-sluchatka/Reproduktory-znacky-SAL/Stredobasove-reproduktory/Reproduktor-SAL-SBX1010-BK-8ohm-50W-basovy-stredobasovy-d153582) |
| Raspberry Pi Pi-DAC+                | 1        | 539                               | 25,58                                         | [Link](https://rpishop.cz/zvukove-karty/803-iqaudio-pi-dac.html)                                                                                                                          |
| Mid range speakers (2 pcs)          | 1        | 227                               | 10,77                                         | [Link](https://www.aliexpress.com/item/1005007256226541.html)                                                                                                                             |
| Sub+mid AMP                         | 1        | 183,57                            | 8,72                                          | [Link](https://www.aliexpress.com/item/1005007922429735.html)                                                                                                                             |
| Tweeters (2 pcs)                    | 1        | 163,9                             | 7,78                                          | [Link](https://www.aliexpress.com/item/1005007671411735.html)                                                                                                                             |
| Tweeter AMP                         | 1        | 112,92                            | 5,36                                          | [Link](https://www.aliexpress.com/item/1005007039518679.html)                                                                                                                             |
| Mini touch sensor                   | 3        | 192,39                            | 9,17                                          | [Link](https://www.aliexpress.com/item/1005008634223216.html)                                                                                                                             |
| White LED's (100pcs)                | 1        | 68,49                             | 3,27                                          | [Link](https://www.aliexpress.com/item/1005009131564126.html)                                                                                                                             |
| 200W 24V thin power supply          | 1        | 137,57                            | 6,56                                          | [Link](https://www.aliexpress.com/item/1005007655951765.html)                                                                                                                             |
| 3 types of dupont cables (20pc)     | 1        | 42,91                             | 2,05                                          | [Link](https://www.aliexpress.com/item/1005009366257883.html)                                                                                                                             |
| Universal PCB Breadboard (5pcs)     | 1        | 108,05                            | 5,15                                          | [Link](https://www.aliexpress.com/item/1005008240247248.html)                                                                                                                             |
| 24V to 5V step down                 | 1        | 73,23                             | 3,5                                           | [Link](https://www.aliexpress.com/item/1005008717423594.html)                                                                                                                             |
| Speaker wire (3m)                   | 1        | 126,37                            | 6,03                                          | [Link](https://www.aliexpress.com/item/32694142009.html)                                                                                                                                  |
| 150 Ohm resistors for LED's (100pc) | 1        | 40,76                             | 1,94                                          | [Link](https://www.aliexpress.com/item/1005006730653425.html)                                                                                                                             |
|                                     |          |                                   |                                               |                                                                                                                                                                                           |
| **Subtotal**                        |          | **4033,3**                        | **191,74** (may change due to exchange rates) |                                                                                                                                                                                           |
