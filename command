ssh <server> tail -f /var/log/rdio.log | grep "JavaScript Error" --line-buffered | ~/Dev/jslogparse/parselogs.py

