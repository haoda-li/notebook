import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import datasets, transforms
import numpy as np
import matplotlib.pyplot as plt


# --8<-- [start:vae]
class VAE(nn.Module):
    def __init__(self, x_dim, h_dim1, h_dim2, z_dim):
        super(VAE, self).__init__()
        
        # encoder part
        self.fc1 = nn.Linear(x_dim, h_dim1)
        self.fc2 = nn.Linear(h_dim1, h_dim2)
        self.fc31 = nn.Linear(h_dim2, z_dim)
        self.fc32 = nn.Linear(h_dim2, z_dim)
        # decoder part
        self.fc4 = nn.Linear(z_dim, h_dim2)
        self.fc5 = nn.Linear(h_dim2, h_dim1)
        self.fc6 = nn.Linear(h_dim1, x_dim)
        
    def encoder(self, x):
        h = F.relu(self.fc1(x))
        h = F.relu(self.fc2(h))
        return self.fc31(h), self.fc32(h) # mu, log_var
    
    def sampling(self, mu, log_var):
        std = torch.exp(0.5*log_var)
        eps = torch.randn_like(std)
        return eps.mul(std).add_(mu) # return z sample
        
    def decoder(self, z):
        h = F.relu(self.fc4(z))
        h = F.relu(self.fc5(h))
        return torch.sigmoid(self.fc6(h)) 
    
    def forward(self, x):
        mu, log_var = self.encoder(x.view(-1, 784))
        z = self.sampling(mu, log_var)
        return self.decoder(z), mu, log_var

def ELBO_loss(recon_x, x, mu, log_var):
    # ~ Bernoulli ELBO
    BCE = F.binary_cross_entropy(recon_x, x.view(-1, 784), reduction='sum')
    # Normal ELBO
    KLD = -0.5 * torch.sum(1 + log_var - mu.pow(2) - log_var.exp())
    return BCE + KLD

def train(model, train_loader, optimizer):
    model.train()
    train_loss = 0
    for data, _ in train_loader:
        data = data.cuda()
        optimizer.zero_grad()
        recon_batch, mu, log_var = model(data)
        loss = ELBO_loss(recon_batch, data, mu, log_var)
        loss.backward()
        train_loss += loss.item()
        optimizer.step()
    return train_loss / len(train_loader.dataset)

def test(model, test_loader):
    model.eval()
    test_loss= 0
    with torch.no_grad():
        for data, _ in test_loader:
            data = data.cuda()
            recon, mu, log_var = model(data)
            # sum up batch loss
            test_loss += ELBO_loss(recon, data, mu, log_var).item()
    return test_loss / len(test_loader.dataset)
# --8<-- [end:vae]

# MNIST Dataset
train_dataset = datasets.MNIST(root='./mnist_data/', train=True, transform=transforms.ToTensor(), download=True)
test_dataset = datasets.MNIST(root='./mnist_data/', train=False, transform=transforms.ToTensor(), download=False)
# Data Loader (Input Pipeline)
train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=100, shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=1000, shuffle=False)

# build model
vae = VAE(x_dim=784, h_dim1= 512, h_dim2=256, z_dim=2).cuda()
optimizer = torch.optim.Adam(vae.parameters())
nepoch = 40
train_loss = np.empty(nepoch)
test_loss = np.empty(nepoch)
from tqdm import tqdm
for epoch in tqdm(range(nepoch)):
    train_loss[epoch] = train(vae, train_loader, optimizer)
    test_loss[epoch] = test(vae, test_loader)
    
plt.figure(figsize=(6,4))
plt.title("Loss")
plt.plot(train_loss, label="train loss")
plt.plot(test_loss, label="test loss")
plt.savefig("../assets/vae_loss.png")


fig, axs = plt.subplots(2, 4, figsize=(16, 8))
from random import sample
with torch.no_grad():
  for i, idx in enumerate(sample(range(len(test_dataset)), 4)):
    input = test_dataset[idx][0]
    axs[0, i].imshow(input.view(28, 28).numpy(), cmap="gray")
    input = input.cuda()
    recon, mu, log_var  = vae(input)
    axs[1, i].imshow(recon.view(28, 28).detach().cpu().numpy(), cmap="gray")
    axs[1, i].set_axis_off(); axs[0, i].set_axis_off()
fig.savefig("../assets/vae_recons.png")


fig, axs = plt.subplots(2, 4, figsize=(16, 8.4))
with torch.no_grad():
  for i in range(8):
    z = torch.randn(2)
    axs[i%2, i//2].set_title(f"mu={z[0]:.6f}, sigma={z[1]:.6f}")
    z = z.cuda()
    sample = vae.decoder(z).cuda()
    axs[i%2, i//2].imshow(sample.view(28, 28).detach().cpu().numpy(), cmap="gray")
    axs[i%2, i//2].set_axis_off()
fig.savefig("../assets/vae_random.png")