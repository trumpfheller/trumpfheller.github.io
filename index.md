---
layout: default
---

> Content restructuring & development, re-think & re-imagine.

---

## My QA Playbook
  - [Introduction](./playbook/qa_playbook.html)
  - [Milestone 1 Initiation](./playbook/01.html)
  - [Milestone 2: Set the stage and plan Agile](./playbook/02.html)
  - [Milestone 3: Agile Test Plan](./playbook/03.html)
  - [Milestone 4: User centric TCs - Early and Continuous Testing](./playbook/04.html)
  - [Milestone 5: From Bug report to Bug Cycle](./playbook/05.html)
  - [Milestone 6: Triage Defects](./playbook/06.html)
  - [Milestone 7: Monitoring](./playbook/07.html)
  - [Milestone 8: Realease Release - in progress](./playbook/08.html)
  - [Milestone 9: Foster Continuous Learning and Knowledge Sharing](./another-page.html)

---

- [Workexperience](https://sciustechnologia.github.io/)

---

### Bluetooth testing lab

As an example, you have a Bluetooth loudspeaker and your marketing department wants to say: works within 20 feet distance, streams high quality sound and works on every device. 
My Bluetooth testing lab will take your prototype, and test if it actally delivers what and then compromise a report based on the logs from the prototype or the phone.
In technical terms:
> Using a **Raspberry Pi 5 Cluster** controlled by a Linux (Ubuntu) machine that allows for automated testing, multi-device compatibility, and signal analysis.

#### General Use Cases

* **Automated Bluetooth Device Testing** – Using scripts to automate pairing, unpairing, signal strength tests, and data transfer analysis.

#### Basic architecture
* Controller Node – Manages test execution, collects logs, and analyzes results (Linux/Ubuntu with an AMD Ryzen7, 64GB RAM).
* Test Nodes – Run Bluetooth tests, interact with target devices, and send results to the controller (RasPi4 and 5s). 

| Node              | Role | Tools Installed | OS | under the hood |
| :---------------- | :------: | ----: | :------: | ----: |
| Pi 1 |   Controller   | Ansible, Grafana, Logstash |   Linux/Ubuntu    | AMD Ryzen 7 5700u, 64GB DDR4 RAM, 2TB PCIe SSD |
| Pi 2 |   Test Node   | PyBluez, hcitool, btmon |   Raspberry Pi OS / Debian  | Pi4, ARM Cortex-A72, SanDisk 32GB MicroSD |
| Pi 3    |  Test Node   | PyBluez, hcitool, Ubertooth |   Raspberry Pi OS / Debian   | Pi5 |
| Pi 4  |  Test Node   | PyBluez, hcitool, nRF Sniffer |   Raspberry Pi OS / Debian   | Pi5 |

#### Software used
* **Ansible** to deploy scripts across all Raspberry Pi nodes.
* **BlueZ** – for scanning, pairing, and debugging (Linux Bluetooth stack).
* **hcitool & hcidump** – for low-level Bluetooth device scanning and debugging.
* **btmon** – for capturing Bluetooth events (a monitoring tool).
* **Wireshark with Bluetooth Plugins** – for sniffing and analyzing Bluetooth traffic.
* **BLE Sniffers** – for deeper BLE analysis (need to do research on Nordic Semiconductor nRF Sniffer). 

#### Documentation 
* using Jekyll (Markdown)
  
---

## Private Research
> Leading question: what do we know about knowledge?

- [epistemological tree](epistemologicalTree.html)
