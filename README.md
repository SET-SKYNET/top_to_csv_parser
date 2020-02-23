
    # INSTRUCTION HOW TO USE top_to_csv_parser.py SCRIPT:


    # PRECONDITIONS:
    1. Install docker-compose (according to your operating system, use GOOGLE if required)


    # EXAMPLE:
    1. From your Mac or Linux terminal goto folder [ top_to_csv_parser ], (e.g. using command
        [ *cd path/to/top_to_csv_parser* ])
    2. Execute docker-compose command below to deploy latest CentOS-8 image on your system (just to see the result of the script)
       In addition docker-compose.yml file will automatically update our CentOS-8 image and install vim and python3.
        [ **docker-compose up -d** ]
    3. Open a new terminal tab and execute next command, to 'jump' into the containers tty.
       To quit from containers tty (later) - type [ exit ] command and hit enter.
        [ docker container exec -it CentOS-8 /bin/bash ]
    4. Goto [ /home ] folder
        [ cd home ]
    5. This folder is actually 'mupped' folder from a container to our local machine [ ../top_to_csv_parser/home ] folder.
       So now, when we type [ ls -l ] command - you will see your LOCAL files [ top_log.csv ] and [ top_to_csv_parser.py ],
       just as if they were on docker machine
        [ ls -l ]
    6. Execute [ chmod ] command to have a possibility to run script.
        [ chmod +x top_to_csv_parser.py ]
    7. At last, run script and it will automatically take data from [ top ] and write it to [ top_log.csv ] file every 'n' seconds. =)
       By default - 100 iterations every 1 second.
       To stop script executing, press [ CTRL + C ] keys.
        [ ./top_to_csv_parser.py ]
    8. All script settings are made solely in the script itself.


    # POST CONDITIONS:
        After testing script:
    1. Type [ exit ] to quit from containers tty;
    2. Stop CentOS-8 container with [ docker-compose down ] command.
    3. You may check, that container is stopped correctly, with [ docker container ps ] command

    # P.S. ENJOY! =)
