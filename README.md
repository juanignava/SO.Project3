# SO.Project3
Ping flood atack

## Prerequisites

- Install a virtual machine with ubuntu 20.04 (not limited to this OS).

- In the virtual machine install python3

- In the virtual machine clone this project

- Configure the virtual machine Network with the `Attached to` option as `Bridged Adapter` and with the Name `wlp2s0`

- In the local machine install hping3 by running `sudo apt install hping3`

- Verify the instalation with `hping3 --version`

- Get the ip address of the virtual machine and save this number.

### How to run

To run this project you can follow this steps:

1. Change the server's code ip address to the one obtained in the last section.

2. Run the server in the virtual machine with the command `make server`

3. Change the client's code ip address to the one obtained in the last section.

4. Run the client in the local machine by running `make client`

5. The console indicates you that you can send messages to the server and you will receive the time it took the server to handle your request. Keep these times in mind.

6. Open other console and run the command `make hping` this is the attack, it will send a predefined amount of packages thourgh socket communication to the server.

7. While the last steps's pings are being executed, repeat step 5 so that it will send the application message, notice that the time it takes to answer es bigger, this happens due to the attack.


