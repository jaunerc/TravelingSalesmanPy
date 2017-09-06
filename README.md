# Traveling Salesman Problem Python
Traveling Salesman Problem solver written in python.

## What this repo provides
You will find solver implementations for the Traveling Salesman Problem. In addition there is a ui module to visualize the algorithms. The latest commit includes only a greedy solver who try out every possible path to find the shortest path.

![alt Graphical solution](https://image.ibb.co/iNGQgv/traveling_Salesman_Py.png)

## The problem
The traveling salesman problem is a well known math problem. Take a look at [wikipedia.org](https://en.wikipedia.org/wiki/Travelling_salesman_problem) if you need further informations about it. To put it in a nutshell, it asks for the shortest path that visits all cities that a traveling salesman wants to visit.

## A bit of math
To find a solution for this easy question can be very hard. That's because the number of possible paths between all cities is huge. As an example, if you have 5 cities there are 12 different paths. Adding a single city extends the number of different paths by the factor of 5. So there are now 60 different paths. With 7 cities 360 paths and so on...

The number of different paths can be writen as **(n - 1)! / 2**   (n = number of cities).

>Note: That formula applies to a symmetric TSP. That means that the direction of traveling between two cities doesn't matter (A -> B is equals with B -> A). If we talk about an asymmetric TSP there are more different paths **(n - 1)!**.
---
As you can see the growth of this function is immense. As an example, let's take 15 cities. If all directions between two cities are symmetric the number of different paths is (15 - 1)! / 2 or 43'589'145'600.

But 15 is still a small number. For the next example we take 100. Which results in (100 - 1)! / 2. The calculator of google search says the result is approximately 4.666311e+155.
>Or 4.666311e * 10^155 = 4.666311e * 100'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000'000

## Solving the problem
The TSP is called an NP problem. That means we can't solve the problem efficient with an existing computer (but maybe sometime in the future ;-) [Quantum computing](https://en.wikipedia.org/wiki/Quantum_computing)).

The simple and exact way of solving is to try out every possible path. That works fine for a very small number of cities but not for the 100-cities-example. Therefore several probabilistic approaches can be used to find a quicker but less accurate solution.
