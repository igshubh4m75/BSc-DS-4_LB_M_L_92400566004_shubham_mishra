#!/bin/bash

for count in {1..54}
do
    echo "Running prog${count}.py..."
    python "prog${count}.py"
done

echo "All programs executed"