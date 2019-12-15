# Distributed Monitoring System
The system to monitor remote computers.  
There are two parts of this system:
- Agent
- Server

## Agent 
Reeds provided config file with params of operation system. Tracks these parameters and send the results to monitoring server.

To run an agent use the command: 
``python agent.py``

## Server
Collects the monitoring params, provides histograms with collected data.

Run: ``python ./manage.py runserver``

Histograms for each tracked computer are available by the following url: http://localhost:8000/computers/