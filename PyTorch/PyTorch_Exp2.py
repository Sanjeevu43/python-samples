
import torch
import torch.nn as nn
import torch.optim as optim

# 1. Define a Simple Model
#    Inherits from nn.Module, the base class for all neural network modules.
class SimpleLinearModel(nn.Module):
    def __init__(self):
        super(SimpleLinearModel, self).__init__()
        # Define a single linear layer:
        # Takes 1 input feature, produces 1 output feature.
        self.linear = nn.Linear(in_features=1, out_features=1)

    def forward(self, x):
        # Defines how data flows through the model.
        # Here, it just passes through the linear layer.
        return self.linear(x)

# 2. Create Dummy Data
#    We need input data (x) and target data (y_true).
#    Let's pretend we want to learn the relationship y = 2x + 1
#    Requires gradients allows PyTorch to track operations for differentiation.
x_train = torch.tensor([[1.0], [2.0], [3.0], [4.0]], requires_grad=False) # Input
y_true = torch.tensor([[3.0], [5.0], [7.0], [9.0]], requires_grad=False) # Target (2*x + 1)

# 3. Instantiate the Model, Loss Function, and Optimizer
model = SimpleLinearModel()
criterion = nn.MSELoss() # Mean Squared Error Loss - common for regression
optimizer = optim.SGD(model.parameters(), lr=0.01) # Stochastic Gradient Descent optimizer

# --- Before Training ---
print("--- Before Training ---")
# Get the randomly initialized weights and bias
# Parameters are returned as a generator, convert to list to see them
initial_params = list(model.parameters())
print(f"Initial Weight: {initial_params[0].item():.4f}")
print(f"Initial Bias: {initial_params[1].item():.4f}")
# Make a prediction with initial random weights
with torch.no_grad(): # Disable gradient calculation for prediction
     initial_pred = model(x_train)
print(f"Initial Predictions:\n{initial_pred.numpy().flatten()}")


# 4. Perform a Single Training Step (usually this is in a loop)

# a) Forward pass: Get model's prediction
y_pred = model(x_train)

# b) Calculate loss: How far off is the prediction?
loss = criterion(y_pred, y_true)

# c) Zero gradients: Reset gradients from previous steps (important!)
optimizer.zero_grad()

# d) Backward pass: Calculate gradients of the loss w.r.t. model parameters
loss.backward()

# e) Optimizer step: Update model parameters based on gradients
optimizer.step()


# --- After One Training Step ---
print("\n--- After One Training Step ---")
# Get the updated weights and bias
updated_params = list(model.parameters())
print(f"Updated Weight: {updated_params[0].item():.4f}")
print(f"Updated Bias: {updated_params[1].item():.4f}")
print(f"Loss after 1 step: {loss.item():.4f}") # .item() gets the scalar value from the tensor

# Make a prediction with the updated weights
with torch.no_grad():
     updated_pred = model(x_train)
print(f"Predictions after 1 step:\n{updated_pred.numpy().flatten()}")

# Note: In a real scenario, you would repeat steps 4a-4e many times (epochs)
#       over your dataset until the loss converges to a low value.
#       The parameters would gradually get closer to weight=2.0 and bias=1.0.