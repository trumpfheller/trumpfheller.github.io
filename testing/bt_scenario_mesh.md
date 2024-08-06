## Test scenario to assess Bluetooth Mesh’s capabilities 
> to support many-to-many communications and robust message delivery
> ensuring that the network performs effectively under various conditions.


* Description: Testing Bluetooth Mesh's ability to support many-to-many communications and ensure robust message delivery involves evaluating the network's performance and reliability when multiple devices are involved.
* Test Case: Many-to-Many Communications and Robust Message Delivery in Bluetooth Mesh
* Objective:
To verify that a Bluetooth Mesh network can handle many-to-many communications effectively and deliver messages reliably across multiple nodes.

---

## Test Environment:

* Devices: Multiple BLE devices configured as nodes in a Bluetooth Mesh network (e.g., 10-20 devices for scalability testing). 
* Software: Mesh network management tools or applications for provisioning, configuration, and message monitoring.

---

## Test Steps:

### 1.Setup and Initialization:

* Provision Nodes: Provision all devices into the Bluetooth Mesh network, ensuring they are properly added as nodes with unique addresses.
* Configure Network: Set up network parameters, including addressing, group addresses, and publication/subscription configurations for the nodes.

### 2.Configure Many-to-Many Communication:

* Define Groups: Create one or more groups of nodes that will be used for communication (e.g., a group address for a set of devices).
* Publish/Subscribe Configuration: Configure some nodes to publish messages to a group address and others to subscribe to that group address.

### 3.Message Broadcasting:

* Send Broadcast Messages: Initiate message broadcasting from the publisher nodes to the group address. Ensure that the messages are designed to be broadcasted to multiple subscribing nodes.
* Monitor Delivery: Verify that all subscribed nodes receive the broadcast messages. Use tools to check if the messages are delivered successfully and whether any packets are lost.

### 4. Robustness Testing:

* Test Interference: Introduce sources of interference (e.g., other wireless devices) and observe the impact on message delivery. Ensure that the mesh network can handle interference and still deliver messages reliably.
* Stress Test Network: Increase the frequency and volume of messages sent to evaluate the network’s capacity to handle high traffic loads and maintain message delivery performance.

### 5.Message Integrity and Handling:

* Check Message Integrity: Verify that the content of the messages received by subscribing nodes matches the messages sent by the publishing nodes, without corruption or data loss.
* Handle Retransmissions: Test how the network handles retransmissions and acknowledgments. Ensure that messages are retransmitted if necessary and successfully received by all intended nodes.

### 6.Failure and Recovery Testing:

* Simulate Node Failures: Disconnect one or more nodes from the network and observe how the remaining nodes handle message delivery. Verify that the network continues to function and deliver messages despite the failure.
* Reintegrate Nodes: Reconnect the previously disconnected nodes and ensure that they are re-integrated into the mesh network and can resume normal communication.

### 7.Performance Metrics:

* Measure Latency: Record the time taken for a message to travel from the publisher to all subscribing nodes.
* Measure Throughput: Assess the overall throughput of the mesh network by measuring the number of messages delivered per unit of time.
* Track Packet Loss: Monitor and document any packet loss or failed message deliveries.

---

### Cleanup:

Disconnect Devices: Properly disconnect and remove devices from the Bluetooth Mesh network after testing.
Clear Logs: Ensure that any logging or monitoring data is archived or cleared.

### Expected Results:
Successful Communication: All subscribed nodes should receive the broadcast messages from the publisher nodes.
Reliable Delivery: Messages should be delivered reliably, even in the presence of interference or high traffic conditions.
Data Integrity: The content of the received messages should match the sent messages without corruption.
Resilience: The network should handle node failures gracefully and recover effectively, maintaining overall communication reliability.

### Reporting:
Document the results of the many-to-many communication tests, including message delivery success rates, performance metrics, and any issues encountered.
Include observations on network behavior under different conditions, such as interference or high traffic.
Provide recommendations based on the findings, such as any improvements needed for better performance or reliability in the mesh network.

---

None of the companies I worked for ever used this scenario. How many of us are using 10 devices at the same time?
Humor aside, of course it is about the a different situation: 10 people occupying the same space
and then - for some reason they decide to communicate. Event like scenario.