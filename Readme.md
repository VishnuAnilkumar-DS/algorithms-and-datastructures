
> ## This repo is based on Udemy course : https://www.udemy.com/course/algorithms-and-data-structures-in-python/

> >### SEARCHING ALGORITHMS

> Linked List
>>> A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers

> Stack
> >>Stack is a linear data structure which follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out).

> Binary Search Tree
> >> Binary search tree, also called an ordered or sorted binary tree, is a rooted binary tree whose internal nodes each store a key greater than all the keys in the node's left subtree and less than those in its right subtree.

> AVL Tree
> >> AVL tree is a self-balancing binary search tree. It was the first such data structure to be invented. In an AVL tree, the heights of the two child subtrees of any node differ by at most one; if at any time they differ by more than one, rebalancing is done to restore this property.

> Red Black Tree
> >>Red–black tree is a kind of self-balancing binary search tree. Each node stores an extra bit representing "color", used to ensure that the tree remains approximately balanced during insertions and deletions.

> Heap Search
> >> Need to search through every element in the heap in order to determine if an element is inside. One optimization is possible, though (we assume a max heap here). If you have reached a node with a lower value than the element you are searching for, you don't need to search further from that node.

> Heap Search in Python

> Hash Linear Probing
 
> Breadth First Search
>   > Application: Web Crawler
> >>Breadth-first search is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root, and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level. 

> Depth First Search
> >> Depth-first search is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node and explores as far as possible along each branch before backtracking.

> Depth First Search Recursion

> Dijkstra's Algorithm
> >> Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph, which may represent.

> Dijkstras with Adjacency Matrix

> Bellman Ford
> >> The Bellman–Ford algorithm is an algorithm that computes shortest paths from a single source vertex to all of the other vertices in a weighted digraph.
 
> Prims Jarnik
> >> Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized.



> >### SORTING ALGORITHMS

> Bogo Sort
>>>BogoSort also known as permutation sort, stupid sort, slow sort, shotgun sort or monkey sort is a particularly
ineffective algorithm based on generate and test paradigm. The algorithm successively generates permutations of its
input until it finds one that is sorted

> Bubble Sort
>>> Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

> Selection Sort
>>> The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two sub arrays in a given array.

> Insertion Sort
>>> Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

> ShellSort
>>> ShellSort is mainly a variation of Insertion Sort. In insertion sort, we move elements only one position ahead. When an element has to be moved far ahead, many movements are involved. The idea of shellSort is to allow exchange of far items. In shellSort, we make the array h-sorted for a large value of h. We keep reducing the value of h until it becomes 1. An array is said to be h-sorted if all sub lists of every h’th element is sorted.

> Quick Sort
>>> QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.

> Merge Sort
>>> Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.


> Counting Sort
>>> Counting sort is a sorting technique based on keys between a specific range. It works by counting the number of objects having distinct key values (kind of hashing). Then doing some arithmetic to calculate the position of each object in the output sequence.

> Radix Sort
>>> Radix sort is a non-comparative sorting algorithm. It avoids comparison by creating and distributing elements into buckets according to their radix. For elements with more than one significant digit, this bucketing process is repeated for each digit, while preserving the ordering of the prior step, until all digits have been considered. For this reason, radix sort has also been called bucket sort and digital sort.

