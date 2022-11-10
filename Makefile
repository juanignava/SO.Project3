client_end:
	python3 Client.py end

client:
	python3 Client.py MessageTest

server:
	python3 Server.py

hping_interval:
	sudo hping3 -i u20 -S -p 17017 -d 2048 192.168.0.25

hping_flood:
	sudo hping3 --flood -d 2048 -S 192.168.0.25