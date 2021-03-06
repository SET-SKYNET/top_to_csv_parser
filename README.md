## INSTRUCTION HOW TO USE [ top_to_csv_parser.py ] SCRIPT:
 
### PRECONDITIONS:
1. Install docker-compose (according to your operating system, use GOOGLE if required)

### EXAMPLE:
1. From your Mac or Linux terminal goto folder [ top_to_csv_parser ], (e.g. using command in square brackets):
    ###### [ **cd path/to/top_to_csv_parser** ]
1. Execute docker-compose command below to deploy latest CentOS-8 image on your system (just to see the result of the script)
    In addition docker-compose.yml file will automatically update our CentOS-8 image and install vim and python3.
    ###### [ docker-compose up -d ]
1. Open a new terminal tab and execute next command, to 'jump' into the containers tty.
    To quit from containers tty (later) - type [ exit ] command and hit enter.
    ###### [ docker container exec -it CentOS-8 /bin/bash ]
1. Goto [ /home ] folder
    ###### [ cd home ]
1. This folder is actually 'mupped' folder from a container to our local machine [ ../top_to_csv_parser/home ] folder.
    So now, when we type [ ls -l ] command - you will see your LOCAL files [ top_log.csv ] and [ top_to_csv_parser.py ],
    just as if they were on docker machine
    ###### [ ls -l ]
1. Execute [ chmod ] command to have a possibility to run script.
    ###### [ chmod +x top_to_csv_parser.py ]
1. At last, run script and it will automatically take data from [ top ] and write it to [ top_log.csv ] file every 'n' seconds. =)
    By default - 100 iterations every 1 second.
    To stop script executing, press [ CTRL + C ] keys.
    ###### [ ./top_to_csv_parser.py ]
1. All script settings are made solely in the script itself.

### POST CONDITIONS (after testing script):
1. Type [ exit ] to quit from containers tty;
1. Stop CentOS-8 container with [ docker-compose down ] command.
1. You may check, that container is stopped correctly, with [ docker container ps ] command

    ### P.S. ENJOY! =)

Terminal commands example
![Terminal commands example](example_cmd_in_terminal.png)

csv log file example
![csv log file example](example_top_log.csv.png)
