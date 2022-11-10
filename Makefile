client_end:
	python3 Client.py end

client:
	python3 Client.py MessageTest test.txt

queue:
	python3 Client_queue.py

server:
	python3 Server.py 192.168.0.25

hping_interval:
	sudo hping3 -i u20 -S -p 17017 -d 2048 192.168.0.25

hping_flood:
	sudo hping3 --flood -d 2048 -S 192.168.0.25

ping_flood:
	sudo ping -s 12048 -f 192.168.0.25