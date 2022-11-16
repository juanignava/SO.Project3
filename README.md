# SO.Project3
Ping flood atack

## Prerequisites

- Install a virtual machine with ubuntu 20.04 (not limited to this OS).

- In the virtual machine install python3

- In the virtual machine clone this project

- Configure the virtual machine Network with the `Attached to` option as `Bridged Adapter` and with the Name `wlp2s0`

- Get the ip address of the virtual machine and save this number.

### How to run

To run this project you can follow this steps:

1. Change the server's code ip address to the one obtained in the last section.

2. Run the server in the virtual machine with the command `make server`

3. Change the makefiles IP variable to the one obtained in the last section.

4. Run the client in the local machine by running `make client src_filename=<your source filename> dest_filename=<your destination filename>` note that the names of the files will be added with the txt extension. For example : `make client src_filename=test.txt dest_filename=test4.txt`

5. At the end of the analysis the program prints the server time, the total time and their difference which is the connection time. 

6. In order to implement the attack open another terminal and run the command `make client_attacker` and while this is running execute the step 4.

7. You'll notice a big difference in the results and these numbers represent the impact of the attack.


### Important links 

https://www.redeszone.net/tutoriales/seguridad/hping3-manipular-paquetes-tcp-ip-ataques/

https://www.keysight.com/us/en/assets/7019-0414/technical-overviews/Simulating-a-DDoS-Attack-in-Your-Own-Lab.pdf

https://youtu.be/fGWkhmCp_js
