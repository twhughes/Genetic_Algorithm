# Simple-Genetic-Algorithm
Genetic algorithm example.

## Problem Statement

Each organism contains a 'DNA' string consisting of 0's and 1's.
This DNA string can also be represented as a non-negative integer in binary notation.

The fitness of an organism is defined by how close this integer is to a target value.

## Optimization Procedure

A population of organisms is randomly generated.  
Out of these organisms, a certain percentage is 'killed'.  
The remaining organisms now 'mate' with each other by crossover of their respective DNA strings.
Mutations of individual entries of the DNA strand may now occur at random.
These resulting children now fill the population and this process is repeated.

## Results

After several iterations, the population is filled with organisms with integer values close to the target.