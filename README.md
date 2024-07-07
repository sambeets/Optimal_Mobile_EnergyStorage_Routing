# Optimal Mobile Energy Storage Routing

This repository contains two models - (1) Optimal vehicle routing for mobile energy storage including technological details (2) Extended model with Optimal Charging Cycle. 
The mathematical formulations are presented in the PDF file. The models are presented in Jupyter notebook format. 


## Descriptions
### Model Optimal vehicle routing
A detailed optimization model for mobile energy storage system (MESS) transportation management has been developed using a mixed-integer linear programming (MILP) approach to prioritize route optimization, which minimizes operational costs. This mathematical model is designed to successfully tackle real-world transportation difficulties by incorporating twelve specific constraints.

The dynamic programming method is used to develop this model. This approach is specifically developed to continuously update the state of charge (SOC) of the MESS and make appropriate adjustments to the pickup selections. Validation in several situations has confirmed that the system effectively reduces travel distances and operating costs, promoting more sustainable MESS transportation in the construction industry.

### Model optimal charging cycle
The data for an optimal charging cycle is collected from Skagerak Energi, located in Prosgrunn, Norway. This company generates power and heat from renewable sources, significantly contributing to the transition towards sustainability. 

This model ensures the monitoring of the state of charge (SOC) levels for four excavators and the MESS at the charging sites and optimizes the charging cycle.

### Data descriptions
Optimal vehicle routing

A synthetic dataset was developed that precisely mirrors the actual construction site variables and scenarios. Three types of datasets are developed for this model: the construction site demand dataset, the vehicle specification dataset, and the distance matrix between the nodes. Those datasets can be found in the "dataset" folder.

optimal charging cycle

The dataset is from a project that has one charging hub with three MESS units, each with a capacity of 550 KWh. This charging hub supports two charging sites, named Charging Site 1 and Charging Site 2. These charging sites are eight and twelve kilometers away from the charging hub. The charging site 1 supports two excavators and one MESS. Similarly, charging site 2 has two excavators and a MESS. Those excavators get energy from their allocated charging sites. During the day, charging the excavator to 90 percent SOC is the maximum. The SOC threshold for both excavator and MESS is set at 15 percent. The operation time window for excavators is 07:00 to 19:00. At work, all machines require 100 percent SOC, starting at 07:00.


## Guidelines to use



## Refrences
