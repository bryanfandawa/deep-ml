import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    probabilities = []
    for x in features:
        for j in range(len(weights)):
            x[j] = x[j] * weights[j]
        
        z = sum(x) + bias

        probability = 1 / (1 + (math.exp(-z)))
        probabilities.append(probability)

    #mse = (prediction - actual)^2 / total_y
    total = 0
    for i in range(len(labels)):
        error = probabilities[i] - labels[i]
        total += error ** 2
    
    mse = total / len(labels)

    return probabilities, mse