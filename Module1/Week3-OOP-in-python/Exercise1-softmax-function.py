import torch
import torch.nn as nn

class MySoftMax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        return x_exp / x_exp.sum(0, keepdim=True)
    
class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_max = torch.max(x, dim=0, keepdim=True)
        x_exp = torch.exp(x - x_max.values)
        return x_exp / x_exp.sum(0, keepdim=True)

data = torch.Tensor([1, 2, 3000])
softmax_stable = SoftmaxStable()
output = softmax_stable(data)
print(output)