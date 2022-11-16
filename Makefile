IP=192.168.0.25

client:
	python3 Client.py $(IP) $(src_filename) $(dest_filename)

client_attacker:
	python3 Client_attacker.py $(IP)

server:
	python3 Server.py $(IP)

clean_thread:
	rm encryptedFiles/*
	rm savedFiles/*

decrypt:
	python3 decrypt.py $(filename)