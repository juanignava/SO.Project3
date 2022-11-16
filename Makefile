IP=192.168.0.25
TEST_MESSAGE=test
END_MESSAGE=end

client_end:
	python3 Client.py $(IP) end

client:
	python3 Client.py $(IP) $(filename)

client_attacker:
	python3 Client_attacker.py $(IP)

queue:
	python3 Client_queue.py

server:
	python3 Server.py $(IP)

hping_interval:
	sudo hping3 -i u20 -S -p 17017 -d 2048 $(IP)

hping_flood:
	sudo hping3 --flood -d 2048 -S $(IP)

ping_flood:
	sudo ping -s 12048 -f $(IP)