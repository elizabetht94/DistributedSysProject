import ray
import time
from datetime import datetime as dt

@ray.remote
def multiplier(input_value):
    time.sleep(1)
    return (input_value*2)

if __name__ == '__main__':
    ray.init(address='auto')
    values = range(10000)
    start = dt.now()
    new_values = [multiplier.remote(x) for x in values]
    return_value = ray.get(new_values)
    end = dt.now()
    print("Return Value: {}".format(return_value))
    print("Elapsed Time: {}".format((end-start).total_seconds()))
