Total time spent: 13.5 hours

# 16/7/2025

I researched about ways I could go around making this project. I figured out I'll be using a Raspberry Pi, as I need some processing power for the EQ and interconnection with the application, it will also be easier to work with.
Another thing I newly realised was the fact, that I'd need to use a DAC to get an audio signal out of the RPI, which will add some cost later on.

<img width="540" height="464" alt="image" src="https://github.com/user-attachments/assets/dda9b827-5238-4289-8537-756319eaf611" />

Time spent: 1.5 hour

# 18/7/2025

Now I got to the audio part of the project, I have been looking for and researching which speaker drivers to use for the smart speaker and found out I will be using a 100mm radius 50 watt bass speaker as the subwoofer from a local store with cheaper shipping, the midrange speaker isn't as heavy, so it will be purchased from Aliexpress and so will be the tweeters.

<img width="501" height="375" alt="image" src="https://github.com/user-attachments/assets/076be486-189d-4631-a344-a669b4a13b83" />

Another thing I was thinking about was whether I'll be needing a DSP or not, I came to the conclusion, that I'll just be using a software DSP, which will be running on the RPI.

I couldn't decide which DAC I'll be using, I was thinking about HiFiBerry DAC's, however those are pretty expensive, so I'll probably go for an IQaudIO DAC. Another problem I encountered though, was the fact, that I'd be wanting to have 3 audio outputs (lows, mids, highs), this DAC is stereo, so I can use one channel for one type and the other for the other type, however I need 3 outputs, so I figured, I could just use an amplifier with a low pass filter to get lows from mids.

<img width="500" height="500" src="https://github.com/user-attachments/assets/b702c339-f7b3-4ee4-8325-7d7f35f5a95b" />

I also looked into some mid-range speaker options and I'll be going for these from Aliexpress

<img width="615" height="537" alt="image" src="https://github.com/user-attachments/assets/040e36cc-8788-4da8-8f05-e52cb51a1f01" />

Time spent: 3.5 hours

# 19/7/2025

I researched a bit about the tweeters and found out these would probably be the best value from Aliexpress:

<img width="626" height="524" alt="image" src="https://github.com/user-attachments/assets/a87c5edf-cfcc-4a1e-9ef5-ad13f6b955b1" />

I also looked at some sub+mids amplifier options, which I'll be ordering from Aliexpress, and I found this one to be good and powerful:

<img width="626" height="576" alt="image" src="https://github.com/user-attachments/assets/00ff7056-3c4c-4187-b5d8-4ee6e35c0d71" />

Then I also looked for some amplifiers for the tweeters and found this one to be suitable for the tweeters:

<img width="607" height="522" alt="image" src="https://github.com/user-attachments/assets/4d18bbc5-4010-4c88-a2fe-86a780eccffd" />

It uses the same chip as the amplifier for the sub + mid drivers, so it should be able to power the tweeters without issues.

As for some on device settings adjustment (volume control, playback control - pause/play track, skip track etc.) I figured using a small touch sensor, which can penetrate through plastic, would be the best for this project, so I found this on Aliexpress

<img width="581" height="404" alt="image" src="https://github.com/user-attachments/assets/61e0c680-8742-4a39-b868-9ce7a7678991" />

These are ideal to just have simple

And with that to have some indication about something being changed, it would be great to have an LED light to see when something has changed (the volume changed, track has been skipped or paused/unpaused)

Therefore I would be purchasing these white LED's on Aliexpress:

<img width="574" height="478" alt="image" src="https://github.com/user-attachments/assets/ac3b57d8-8b35-46cf-92c2-b91a81456787" />

Another thing I looked at today was a power supply to power the whole speaker with, I found out that 24 volts would be perfect and most power efficient for the speaker amplifiers and would also make the PSU more efficient. Then for the wattage, I would probably need somewhere around 150 watts, however to get a bit of headroom and also to make sure the PSU almost never runs at full power, getting a 200 watt power supply would be more ideal.

I found this 24v 8.3A (200W) thin power supply on Aliexpress, which I would be using:

<img width="640" height="620" alt="image" src="https://github.com/user-attachments/assets/143fd8ec-00b6-44d8-b97d-c61680c60f44" />

It should be able to power all the speaker amps and with a step-down voltage regulator could even power the Raspberry Pi, making it look neater with just one wall outlet cable. The step down voltage regulator I will be using is this one from Aliexpress:

<img width="625" height="541" alt="image" src="https://github.com/user-attachments/assets/9fc01d68-7d96-4d37-a1b9-4ef215966e3e" />

Getting an external power supply would probably be better, however it would look bad, like this it will look much neater.

The last thing I wanted to get were some speaker wires, for it to not be a fire hazard, especially with the subwoofer, eventhough it should be safe, I'd rather be safer. I decided to get these wires from Aliexpress:

<img width="576" height="386" alt="image" src="https://github.com/user-attachments/assets/0666a927-660c-4763-bbb5-c4fb7c9b7f63" />

Time spent: 5.5 hours

# 21/7/2025

I thought through and created a (wiring) sketch of all the components used in the project and spaced out all the components how they're going to be connected.

<img width="1760" height="1014" alt="image" src="https://github.com/user-attachments/assets/c75b86b5-63e2-4b9d-b31b-84c9fc9f2aa1" />

The black lines are generic wires, red and black lines are live + neutral wires and the purple lines are speaker wires connecting the speakers.

Time spent: 1.5 hours

# 22/7/2025

I created some basic software for the speaker to be able to atleast play back music via bluetooth and make the touch sensors work with one LED with basic functions. There will be two buttons, one for volume up, the other for volume down, and a third button, which will be a mixed function button, where if it's pressed once it will either pause or play depending whether something is playing or not or when pressed twice within a second it will skip the current track. There are also basic .sh files to setup and install the software and to run it. Obviously more features will be added later, after having the RPI on hand and being able to experiment with it.

Time spent: 1.5 hours
