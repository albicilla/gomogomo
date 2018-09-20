export j=0
export i=0
for i in `seq 1 10`;do
	python3 server.py panda.py vulture.py > hardVSmygomoku.txt
	python3 server.py vulture.py panda.py > mygomokuVShard.txt
done
