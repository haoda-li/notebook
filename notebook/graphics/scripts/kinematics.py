import numpy as np
import matplotlib.pyplot as plt


# --8<-- [start:catmull]
def catmull_rom_interpolation(kfs, t):
    """ return the interpolated data
        
        kfs: Tuple[List[float], List[data]]  
                             sorted keyframes as (time, data)
        t:   float           query times
    """
    times, pos = kfs
    if len(times) < 2 or t > times[-1] or t < times[0]:
        raise ValueError(t)
    found_idx = -1
    for kf_idx, time in enumerate(times):
        if t < time:
            found_idx = kf_idx - 1
            break
    P = [pos[found_idx], pos[found_idx], 
         pos[found_idx+1], pos[found_idx+1]]
    if found_idx > 0:
        P[0] = pos[found_idx-1]
    if found_idx < len(kfs) - 2:
        P[3] = pos[found_idx+2]
    t = (t - times[found_idx]) / (times[found_idx + 1] - times[found_idx])
    interpolated =  (         2*P[1]                  )
    interpolated += ( -P[0] +            P[2]         ) * t
    interpolated += (2*P[0] - 5*P[1] + 4*P[2] -   P[3]) * t**2
    interpolated += ( -P[0] + 3*P[1] - 3*P[2] +   P[3]) * t**3
    return interpolated / 2
# --8<-- [end:catmull]



N = 10
times = np.linspace(0, 10, N)
pos = np.random.uniform(0, 10, N)
kfs = (times, pos)
ts = np.arange(times.min(), times.max(), .1)
interpolated = [catmull_rom_interpolation(kfs, t) for t in ts]
plt.figure(figsize=(6, 4))
plt.scatter(times, pos)
plt.plot(ts, interpolated)
plt.tight_layout()
plt.savefig("../assets/catmull_rom_interpolation.png")