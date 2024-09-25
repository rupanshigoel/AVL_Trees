# AVL_Trees
Implemented AVL Trees for adding different objects in different bins via largest fit and compact fit algorithms.
Every bin has a capacity and an id wherein the ids are unique. Every object has a unique id, some size, and some colour wherein the total number of colours are 4.
The colour decides the bin in which the object has to be placed. <br />
Largest Fit ALgorithm: <br />
When adding an object to a bin, this algorithm selects the bin with the largest remaining capacity. In case the capacities of the largest remaining capacities are the same, then the colour decides if the one with the larger id has to be chosen or the least one. <br />
Compact Fit Algorithm: <br />
When adding an object to a bin, this algorithm selects the bin with the smallest remaining capacity that can accommodate this particular object. In case the capacities of the largest remaining capacities are the same, then the colour decides if the one with the larger id has to be chosen or the least one. <br />
Using AVL Trees to store the cargoes reduced the time complexity of operations to O(log n) and made the storage and removal more efficient.
