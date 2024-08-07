---
layout: default
---

## Test scenario for Classic Bluetooth (BR/EDR) continuous data streaming 

* verify data can be transmitted consistently and reliably over a Bluetooth connection. 

Test Case: Continuous Data Streaming over Classic Bluetooth (BR/EDR)
Objective:
To ensure that a Classic Bluetooth (BR/EDR) connection can handle continuous data streaming effectively without data loss or significant performance degradation.

### Test Environment:

* Devices: Two Bluetooth-enabled devices with BR/EDR support (e.g., smartphones, tablets, or specialized Bluetooth test devices).
* Software: Bluetooth communication application or test tool that supports continuous data transfer.
* Configuration: Ensure both devices are paired and connected using Classic Bluetooth (BR/EDR).

## Test Steps

### 1.Setup and Initialization:

* Pair Devices: Pair the two Bluetooth devices if not already paired.
* Establish Connection: Connect the devices using Classic Bluetooth (BR/EDR) in a data transfer mode (e.g., SPP - Serial Port Profile).

### 2. Test Preparation:

* Select Data Source: Choose or create a data source for streaming (e.g., a file with a known size or a data generator tool).
* Determine Stream Rate: Define the rate at which data will be sent (e.g., 1 MB per minute).

### 3.Continuous Data Streaming:

* Start Data Transmission: Begin streaming data from the source device to the target device.
* Monitor Data Transfer: Use monitoring tools or software to observe data transmission rates and ensure the data is being sent continuously.

### 4.Metrics Collection:

* Measure Throughput: Record the data transfer rate (throughput) during the streaming process.
Track Latency: Measure the latency of data packets (time taken for a packet to travel from the sender to the receiver).
* Monitor Errors: Check for any data errors, lost packets, or retransmissions.

### 5.Stress Testing:

* Increase Data Rate: Gradually increase the data transfer rate to test the limits of the Bluetooth connection.
* Vary Environment: Test in different environments to observe how factors like distance and obstacles affect data streaming.

### 6.Interruption Testing:

* Simulate Interference: Introduce potential sources of interference (e.g., other Bluetooth devices, Wi-Fi networks) and observe the impact on data streaming.
* Disconnection and Reconnection: Temporarily disconnect one device and reconnect to ensure that the streaming resumes correctly. Example of a [Root Cause Analysis](https://trumpfheller.github.io/testing/bt_rootCause_BTClassic.html)

### 7.Data Integrity Check:

* Verify Data: After the streaming is complete, verify that the received data matches the sent data without corruption or loss.
* Check File Integrity: If using a file-based approach, compare the original file with the received file for consistency.

---

### Expected Results:

* Consistent Throughput: The data transfer rate should be consistent with the expected rate and should not fall below a specified threshold.
* Minimal Latency: Latency should be within acceptable limits as defined by the application or Bluetooth specification.
* No Data Loss: Data should be transmitted and received without loss or corruption.
* Stable Connection: The connection should remain stable throughout the streaming process, even under stress or interference conditions.

### Reporting:

* Document the test results, including throughput, latency, any data loss or corruption, and the impact of environmental factors.
* Include screenshots or logs from monitoring tools if applicable.

### In some Agile teams you will have a debriefing/retro in which you can contribute

* Provide recommendations based on test findings, such as improvements needed for better performance or stability.
