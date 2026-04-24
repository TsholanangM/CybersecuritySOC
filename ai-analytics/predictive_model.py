import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

class IncidentPredictionModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(IncidentPredictionModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)  # First layer
        self.fc2 = nn.Linear(hidden_size, output_size)  # Output layer

    def forward(self, x):
        x = F.relu(self.fc1(x))  # Apply ReLU activation
        x = self.fc2(x)  # Output layer
        return x

# Hyperparameters
input_size = 10  # Example input size
hidden_size = 5  # Example hidden size
output_size = 1  # Example output size for binary prediction

# Create model
model = IncidentPredictionModel(input_size, hidden_size, output_size)

# Example input for prediction
example_input = torch.randn(1, input_size)
output = model(example_input)
print(output)