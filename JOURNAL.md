Total time spent: 13.5 hours

# 16/7/2025

I researched about ways I could go around making this project. I figured out I'll be using a Raspberry Pi, as I need some processing power for the EQ and interconnection with the application, it will also be easier to work with.
Another thing I newly realised was the fact, that I'd need to use a DAC to get an audio signal out of the RPI, which will add some cost later on.

<img width="270" height="232" src="https://github.com/user-attachments/assets/83ba8a09-70e3-4cba-a73d-f2f74033f782" />

Time spent: 1.5 hour

# 18/7/2025

Now I got to the audio part of the project, I have been looking for and researching which speaker drivers to use for the smart speaker and found out I will be using a 100mm radius 50 watt bass speaker as the subwoofer from a local store with cheaper shipping, the midrange speaker isn't as heavy, so it will be purchased from Aliexpress and so will be the tweeters.

<img width="270" height="232" src="https://github.com/user-attachments/assets/c897f596-cebc-41d9-81d2-8fc65175deb2" />

Another thing I was thinking about was whether I'll be needing a DSP or not, I came to the conclusion, that I'll just be using a software DSP, which will be running on the RPI.

I couldn't decide which DAC I'll be using, I was thinking about HiFiBerry DAC's, however those are pretty expensive, so I'll probably go for an IQaudIO DAC. Another problem I encountered though, was the fact, that I'd be wanting to have 3 audio outputs (lows, mids, highs), this DAC is stereo, so I can use one channel for one type and the other for the other type, however I need 3 outputs, so I figured, I could just use an amplifier with a low pass filter to get lows from mids.

<img width="270" height="232" src="https://github.com/user-attachments/assets/eb249061-2689-410f-a8ea-581c06a1820f" />

I also looked into some mid-range speaker options and I'll be going for these from Aliexpress

<img width="270" height="232" src="https://github.com/user-attachments/assets/9ce3fcf4-7e33-48c3-bd71-cf3383d01b58" />

Time spent: 3.5 hours

# 19/7/2025

I researched a bit about the tweeters and found out these would probably be the best value from Aliexpress:

<img width="270" height="232" src="https://github.com/user-attachments/assets/462b7bd6-2a8e-4a4e-b389-97014de064ef" />

I also looked at some sub+mids amplifier options, which I'll be ordering from Aliexpress, and I found this one to be good and powerful:

<img width="626" height="576" alt="image" src="https://github.com/user-attachments/assets/16221a55-ae07-4ca2-a067-82822f0efc8f" />

Then I also looked for some amplifiers for the tweeters and found this one to be suitable for the tweeters:

<img width="607" height="522" src="https://github.com/user-attachments/assets/4cd5ba81-cc89-4495-a59c-8e968594cf33" />

It uses the same chip as the amplifier for the sub + mid drivers, so it should be able to power the tweeters without issues.

As for some on device settings adjustment (volume control, playback control - pause/play track, skip track etc.) I figured using a small touch sensor, which can penetrate through plastic, would be the best for this project, so I found this on Aliexpress

<img width="581" height="404" alt="image" src="https://github.com/user-attachments/assets/f20fa7f0-3cfa-4643-9e68-ee2e35307999" />

These are ideal to just have simple

And with that to have some indication about something being changed, it would be great to have an LED light to see when something has changed (the volume changed, track has been skipped or paused/unpaused)

Therefore I would be purchasing these white LED's on Aliexpress:

<img width="574" height="478" alt="image" src="https://github.com/user-attachments/assets/e3841688-d164-427a-a6e9-acae03cfea4c" />

Another thing I looked at today was a power supply to power the whole speaker with, I found out that 24 volts would be perfect and most power efficient for the speaker amplifiers and would also make the PSU more efficient. Then for the wattage, I would probably need somewhere around 150 watts, however to get a bit of headroom and also to make sure the PSU almost never runs at full power, getting a 200 watt power supply would be more ideal.

I found this 24v 8.3A (200W) thin power supply on Aliexpress, which I would be using:

<img width="640" height="620" alt="image" src="https://github.com/user-attachments/assets/7fa24f6f-61f6-49da-8cc6-ff5a74a57973" />

It should be able to power all the speaker amps and with a step-down voltage regulator could even power the Raspberry Pi, making it look neater with just one wall outlet cable. The step down voltage regulator I will be using is this one from Aliexpress:

<img width="625" height="541" alt="image" src="https://github.com/user-attachments/assets/c09210b5-000b-4b5a-8d98-4017bf0ed916" />

Getting an external power supply would probably be better, however it would look bad, like this it will look much neater.

The last thing I wanted to get were some speaker wires, for it to not be a fire hazard, especially with the subwoofer, eventhough it should be safe, I'd rather be safer. I decided to get these wires from Aliexpress:

<img width="576" height="386" alt="image" src="https://github.com/user-attachments/assets/5e876297-ebbd-430b-b90d-cc38c4e32a10" />

Time spent: 5.5 hours

# 21/7/2025

I thought through and created a (wiring) sketch of all the components used in the project and spaced out all the components how they're going to be connected.

<img width="1760" height="1014" alt="image" src="https://github.com/user-attachments/assets/1c621f33-9654-4e18-9d37-58a0f77500ec" />

The black lines are generic wires, red and black lines are live + neutral wires and the purple lines are speaker wires connecting the speakers.

Time spent: 1.5 hours

# 22/7/2025

I created some basic software for the speaker to be able to atleast play back music via bluetooth and make the touch sensors work with one LED with basic functions. There will be two buttons, one for volume up, the other for volume down, and a third button, which will be a mixed function button, where if it's pressed once it will either pause or play depending whether something is playing or not or when pressed twice within a second it will skip the current track. There are also basic .sh files to setup and install the software and to run it. Obviously more features will be added later, after having the RPI on hand and being able to experiment with it.

Time spent: 1.5 hours
