## Bluetooth testing

* focus is on **performance and reliability** (BT has one channel for energy and one for data (includes low energy I guess, but I got to double check)

### Common Symptoms of Bluetooth Protocol Errors 

### 1.Pairing Issues:

* Failure to Connect: The device fails to pair with the infotainment system or drops connection frequently.
* Inconsistent Pairing: The system intermittently recognizes or fails to recognize paired devices.
* Examples: Release testing for Oculus3, testing daily RCs for Google Assistant, pairing wearables with the phone.
  
### 2.Audio Problems:

* Audio Dropouts: Intermittent loss of audio or poor audio quality during streaming or calls.
* Static or Noise: Unwanted noise or static in audio transmitted over Bluetooth.
* Examples: Audio testing for Google Assistant cmds. Compare what was said, with what was heared, with what is expected audio.file.

### 3.Data Transfer Issues:

* Failed File Transfers: Problems with transferring media files or contacts between devices.
* Incorrect Metadata: Mismatches in song titles, artists, or album artwork.
* Examples: 

### 4.Command Recognition Problems:

* Voice Commands: Failure to recognize or correctly execute voice commands.
* Control Functions: Issues with controlling music, navigation, or other functions via Bluetooth. => big topic, but takes more than one paragraph
* Examples: Google Assitant, Amazon, Fitbit, Infotainment system: ask in a foreign language for a song.

---

### what does what?

* BLE,
* Bluetooth5,
* Bluetooth Mesh 

---

When creating TCs, keep in mind that the complexity of your test scenarios has to grow over time.
1. You start with TCs that relate to the install, the OAU (over the air update), and the OOB.
2. Make sure your TCs cover have all the little steps first (foundation, you can include them later in bigger scenarios).
3. The bigger the scenarios get consider to seperate them and give them their own folder. Example:
a) Connect the car with the phone.
b) connect an Ipod with the iPhone
c) connect the iPod with a loudspeaker
d) verify that the iPod gets the music from the phone's wifi/spotify and relates it to the loudspeaker without the infotainmentsystem is interferring.
You have 3 smaller TCs which you add up in a scenario because d) will have different possible issues => automate this scenario eventually.
