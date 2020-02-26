### **Tree Recursion** <br>

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

