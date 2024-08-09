## Bluetooth testing

> focus is on getting **confidence in performance and reliability** 

### Common Symptoms of BT Protocol Errors 

### 1.Pairing Issues:

* Failure to Connect:
  * Device fails to pair during OOB or drops connection frequently.
* Inconsistent Pairing:
  * System fails to recognize paired devices.
* Examples:
  * Release testing for Oculus3 - OOB OTA,
  * testing daily RCs for Google Assistant,
  * pairing wearables with the phone.
  
### 2.Audio Problems:

* Audio Dropouts:
  * Intermittent loss of audio or poor audio quality during streaming or calls.
* White [Noise](https://www.youtube.com/watch?v=iR0FzWA93n0):
  * Unwanted noise or static in audio transmitted over Bluetooth.

### 3.Data Transfer Issues:

* Failed File Transfers:
  * Problems with transferring media files or contacts between devices.
* Incorrect Metadata:
  * Mismatches in song titles, artists, or album artwork.

### 4.Command Recognition Problems:

* Voice Commands:
  * Failure to recognize or correctly execute voice commands.
* Control Functions:
  * Issues with controlling music, navigation, or other functions via Bluetooth. => big topic, but takes more than one paragraph
* Examples: Google Assitant, Amazon, Fitbit, Infotainment system: ask in a foreign language for a song.

---

### what is what?
> Pairing, Audio, Data transfer Voice command - Which functionality is connected with which protocol?

* Bluetooth Classioc and BLE,
* Bluetooth4,5,
* Bluetooth Mesh

Please check the Bluetooth profile [page](https://trumpfheller.github.io/testing/bt_profiles.html).

