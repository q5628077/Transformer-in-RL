from torch import nn as nn
import torch

encoder_layer = nn.TransformerEncoderLayer(d_model=512, nhead=8)
transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=6)
src = torch.rand(10, 32, 512)

out = transformer_encoder(src)

print(out)
print(out.shape)

