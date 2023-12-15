# Complete the following to implement the described hamming distance function.
# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def hamming_dist(signal_1, signal_2):
    if not signal_1["data"] or not signal_2:
        return "Empty signal on at least one of the sensors"
    
    if isinstance(signal_1, dict):
        data1 = signal_1["data"]
        if isinstance(signal_2, tuple):
            data2 = list(signal_2)
        else:
            return "Sensor defect detected"
    elif isinstance(signal_1, tuple):
        data1 = list(signal_1)
        if isinstance(signal_2, dict):
            data2 = signal_2['data']
        else:
            return "Sensor defect detected"
    else:
        return "Sensor defect detected"
    
    if len(data1) != len(data2):
        return "Empty signal on at least one of the sensors"
    
    output = []
    for i in range(len(data1)):

        if len(data1[i]) == 0 or len(data2[i]) == 0:
            return "Empty signal on at least one of the sensors"
        
        if len(data1[i]) != len(data2[i]):
            return "Sensor defect detected"
        
        dist = sum(c1 != c2 for c1, c2 in zip(data1[i], data2[i]))
        if dist > 0:
            output.append((data1[i], data2[i], dist))
    
    return output

# The following lines print your function's output for an exemplary input to the console.
# Note that this does not include any of the mentioned edge cases for defective sensors or signals of different lenghts.
# Try to write your own tests for this.

signal_sensor_1 = {"times": [0, 1, 2, 3, 4, 5],
                   "data": ['22', '']}
signal_sensor_2 = ("2", "", "")
print(hamming_dist(signal_sensor_1, signal_sensor_2))
