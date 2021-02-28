
# Note:neeed to have an environmental variable for GOOGLESHEET_ID

structure.csv:
	wget --output-file="logs.csv" "https://docs.google.com/spreadsheets/d/${GOOGLESHEET_ID}/export?format=csv&gid=0" -O "structure.csv"

network_structure.csv: get_structure.py structure.csv
	./get_structure.py

graph.png: network_structure.csv create_graph.wsl
	./create_graph.wsl network_structure.csv graph.png
