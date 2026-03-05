Simple Reflex Agent for Air Quality Index (AQI) Detection

Project Overview

This project implements a Simple Reflex Agent in Python that determines the Air Quality Index (AQI) of a region using environmental sensor data.

The agent reads pollution parameters from a sensor data file, evaluates them using predefined condition–action rules, and outputs the AQI value and corresponding air quality category.

The system simulates how an AI agent interacts with the environment through sensors and produces actions based on rules.

⸻

Objectives
	•	To understand the concept of Simple Reflex Agents in Artificial Intelligence
	•	To simulate environmental sensing using a data file
	•	To implement rule-based decision making
	•	To determine AQI category based on pollution levels

⸻

Agent Architecture

The system follows the Simple Reflex Agent architecture, where the agent makes decisions based only on the current percept.

Architecture Flow

Environment
     ↓
Sensors (Read pollution data file)
     ↓
Simple Reflex Agent
     ↓
Condition–Action Rules
     ↓
AQI Category Output

Components

Environment
	•	Contains pollution parameters of a region.

Sensors
	•	Read environmental data from a file (sensor_data.txt).

Agent
	•	Processes the input and determines AQI.

Actuator (Output)
	•	Displays AQI value and air quality category.

⸻

Environmental Parameters Used

The following pollutants are considered:

Parameter	Description
PM2.5	Fine particulate matter
PM10	Coarse particulate matter
CO	Carbon monoxide
NO2	Nitrogen dioxide
SO2	Sulfur dioxide

These values are read from the sensor data file.

⸻

AQI Categories

The AQI value is classified into different air quality levels:

AQI Range	Category
0 – 50	Good
51 – 100	Moderate
101 – 150	Unhealthy for Sensitive Groups
151 – 200	Unhealthy
201 – 300	Very Unhealthy
301+	Hazardous


⸻

Project Structure

AQI-Reflex-Agent
│
├── aqi_reflex_agent.py
├── sensor_data.txt
└── README.md


⸻

Sensor Data File

Example content of sensor_data.txt:

PM2.5: 55
PM10: 90
CO: 1.2
NO2: 40
SO2: 15

This file represents environmental parameters collected from sensors.

⸻

Algorithm

Step 1: Read environmental parameters from the sensor file
Step 2: Extract pollutant values
Step 3: Calculate AQI using a simplified weighted formula
Step 4: Apply condition–action rules
Step 5: Display AQI value and air quality category

⸻

How to Run the Program

Step 1

Clone the repository

git clone https://github.com/yourusername/AQI-Reflex-Agent.git

Step 2

Navigate to the project folder

cd AQI-Reflex-Agent

Step 3

Run the Python program

python aqi_reflex_agent.py


⸻

Example Output

--- AQI Monitoring Agent Activated ---

Sensor Data Received:
PM2.5 : 55
PM10 : 90
CO : 1.2
NO2 : 40
SO2 : 15

Computed AQI: 64.0
Air Quality Category: Moderate

Agent Decision: Air quality is acceptable.


⸻

Applications
	•	Environmental monitoring systems
	•	Smart city air quality monitoring
	•	Pollution control analysis
	•	AI-based environmental decision systems

⸻

Technologies Used
	•	Python
	•	Artificial Intelligence (Simple Reflex Agent Model)

⸻

Conclusion

This project demonstrates how a Simple Reflex Agent can be used to process environmental data and determine the Air Quality Index of a region. The agent makes decisions using rule-based reasoning, showing a basic implementation of AI agent architecture.
