# Tree Recursion <br>

## Slide 10 - Counting Partitions

The number of partitions of a positive integer n, using parts up to size m, is the number
of ways in which n can be expressed as the sum of positive integer parts up to m in
increasing order. <br>

```python
def count_partitions(n,m):
    if n == 0:
        return 1
    elif m == 0:
        return 0
    elif n < 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return with_m + without_m

print(count_partitions(4,2))
```

<img src="https://lh3.googleusercontent.com/JHT-JwAKI3hkQ7F1X90dYlclzLlGbq1QshAWDF_avSzgMoTgAoM5clHa_PyUpT5BQjWl=s170" width="500">
<br>

## Lab04 Q4 - Insect Combinatorics <br>

Consider an insect in an M by N grid. The insect starts at the bottom left corner, (0, 0), and wants to end up at the top right corner, (M-1, N-1). The insect is only capable of moving right or up. Write a function paths that takes a grid length and width and returns the number of different paths the insect can take from the start to the goal. (There is a closed-form solution to this problem, but try to answer it procedurally using recursion.) <br>

For example, the 2 by 2 grid has a total of two ways for the insect to move from the start to the goal. For the 3 by 3 grid, the insect has 6 diferent paths (only 3 are shown above).

<img src="https://i.stack.imgur.com/6tfVZ.png">

```python
def paths(m, n):
    if m == 1 or n == 1:
        return 1
    else:
        move_right = paths(m-1, n)
        move_top = paths(m, n-1)
        return move_right + move_top

print(paths(3,3))
```

<img src="https://lh3.googleusercontent.com/DqJoM1NJXSkqUvdKF1baYjKwu8V9zqHfv10nXkKkD5Vg2WRkbpq4XGuKtLzZijg5Rig9IA=s146" width="500">


