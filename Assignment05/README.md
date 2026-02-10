# Simulation Assignment using SimPy

This repository contains the solution for the simulation assignment in which a simulation tool was selected from the provided list and used to generate data by running multiple simulations.

---

## Simulator Used

For this assignment, **SimPy** was selected as the simulation tool. SimPy is an open-source, Python-based discrete-event simulation library and is explicitly mentioned in the provided Wikipedia list of simulation software. It allows modeling systems that evolve over time, such as queues and service systems, making it suitable for this assignment.

---

## Simulation Description

A simple queueing system was modeled using SimPy. In this system, customers arrive at a server based on an arrival rate and require a certain amount of service time. If the server is busy, incoming customers wait in a queue until the server becomes available. The main output measured from the simulation is the average waiting time experienced by customers.

This setup represents a basic discrete-event simulation where events such as arrivals, service start, and service completion are handled by the simulator.

---

## Parameters and Bounds

The simulation uses the following parameters, which are randomly sampled for each run within fixed bounds:

- **Arrival Rate:** between 1 and 10  
- **Service Time:** between 0.5 and 5  

These parameters are varied to observe how different conditions affect the average waiting time in the system.

---

## Data Generation

The simulation was executed **1000 times**. For each simulation run:

- Arrival rate and service time were sampled within the defined bounds  
- The simulation was executed using SimPy  
- The resulting average waiting time was recorded  

The outputs of all simulation runs were saved in a CSV file named `simulation_data.csv`.

Each row in the CSV file corresponds to one simulation run and contains the following columns:

- Arrival_Rate  
- Service_Time  
- Avg_Waiting_Time  

---

## Visualization

Basic visualizations were created inside the Jupyter notebook to understand the simulation results. These include plots showing the distribution of average waiting times and the relationship between the input parameters and the simulation output. The graphs are displayed directly in the notebook and are not saved as separate image files.

---

## Repository Contents

- `Simulation.ipynb` – Jupyter notebook containing the simulation code, data generation, and visualizations  
- `simulation_data.csv` – CSV file containing results from 1000 simulation runs  
- `README.md` – Description of the assignment and implementation  

---

## Conclusion

This assignment demonstrates how a simulation tool can be used to model a system, vary parameters within defined bounds, generate data through repeated simulation runs, and analyze the results. SimPy was effectively used to build a discrete-event simulation and produce reproducible simulation data.

