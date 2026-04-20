# 1-mashq
def outer(x):
    def inner(y):
        return x + y
    return inner

add5 = outer(5)
print(add5(10))  
# 2-mashq
def binary_search(arr, target, low=0, high=None):
    if high is None: high = len(arr) - 1
    if low > high: return -1
    mid = (low + high) // 2
    if arr[mid] == target: return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid-1)
    else:
        return binary_search(arr, target, mid+1, high)

arr = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(arr, 7))  
# 3-mashq
def login_required(func):
    def wrapper(*args, **kwargs):
        print("Foydalanuvchi tizimga kirdi (tekshirildi)")
        return func(*args, **kwargs)
    return wrapper

@login_required
def dashboard():
    return "Xush kelibsiz, Dashboard!"

print(dashboard())
