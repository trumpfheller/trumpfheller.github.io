## Bluetooth testing

> focus is on getting confidence in **performance and reliability** (BT has one channel for energy and one for data (oversimplified)

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

### Which functionality is behind which protocol?

* Bluetooth Classioc and BLE,
* Bluetooth4,5,
* Bluetooth Mesh

Please check the Bluetooth profile [page](https://trumpfheller.github.io/testing/bt_profiles.html).

