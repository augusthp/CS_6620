August Halm-Perazone
CS 6620
May 20 2026

Assigment 1

This project was made to test Github workflows. The code I included is a simple calculator app made in python. It has add, subtract, multiply,and  divide functions. This code also includes a calc_test program that tests each functon. This makes it easy to break a function and see it fail a test. 

##         Local Setup

```bash
git clone
cd python3 -m venv .venv
source .venv/bin/activate
pip install -r requirments.txt
pytest
```

This workflow was made  with the premade Python .yml file found in the github actions tab. This is using the standard file except I added the "workflow_dispatch"line which adds the ad hock functionality.
