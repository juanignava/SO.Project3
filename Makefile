client:
	python3 Client.py

server:
	python3 Server.py

hping:
	sudo hping3 -i u20 -S -p 17017 -c 100000 192.168.0.49