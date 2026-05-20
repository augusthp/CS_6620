August Halm-Perazone
CS 6620
May 20 2026

Assigment 1

This project was made to test Github workflows. This code I included is a simple calculator app made in python. It has add, subtract, multiply,and  divide functions. This code also includes a calc_test program that tests each functon. This makes it easy to break a function and see it fail a test. 

The calc_test file runs each time a new commit is pushed and the result is displayed in the actions tab. To run simply do a git pull of this repo and then make a change to calc.py and push the file. If the change breaks the code in a manor that fails the test the actions tab will show the failed test. Otherwise actions will show a green checkmark. The workflow can also be manually triggered by navigating to the actions tab, clicking the Python Application tab and then selecting "Run workflow" from the right side.

This workflow was made  with the premade Python .yml file found in the github actions tab. This is using the standard file except I added the "workflow_dispatch"line which adds the ad hock functionality.
