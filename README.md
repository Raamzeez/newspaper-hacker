# Newspaper-Hacker Instructions

## SSH into EC2
In your terminal do: `ssh ec2-3-135-211-87.us-east-2.compute.amazonaws.com`

## Run App
To run app you will type command `nohup ./run_server.sh &` inside the git repository on the local machine.

---

## Updating App
To update the app, follow these steps in the terminal:

1. SSH into the server: `ssh ec2-3-135-211-87.us-east-2.compute.amazonaws.com`
2. cd into the newspaper hacker repository by typing this in the terminal: `cd newspaper-hacker`
3. Pull from the GitHub repository: `git pull`
4. Kill python script by typing this in the terminal: `ps -A | grep run_server.sh`
5. Restart the python script by typing this in the terninal: `nohup ./run_server.sh &`
6. Press (Ctrl + C) to get out of nohup
7. Exit the server by typing this in the terminal: `exit`