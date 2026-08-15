import time
import mlx.core as mx

def benchmark_mlx(mode="gpu", size=4000):
    if mode == "cpu":
        mx.set_default_device(mx.cpu)
    else:
        mx.set_default_device(mx.gpu)
    
    a = mx.random.normal((size, size))
    b = mx.random.normal((size, size))
    
    # Warmup
    mx.eval(mx.matmul(a, b))
    
    start = time.time()
    for _ in range(10):
        c = mx.matmul(a, b)
        mx.eval(c)
    end = time.time()
    
    return end - start

print("CPU:", benchmark_mlx("cpu"))
print("GPU:", benchmark_mlx("gpu"))
