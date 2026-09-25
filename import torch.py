import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import numpy as np
 
class Generator(nn.Module):
    def __init__(self, input_dim, output_dim, hidden_dim):
        super(Generator, self).__init__()
        self.gen = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(True),
            nn.Linear(hidden_dim, hidden_dim * 2),
            nn.ReLU(True),
            nn.Linear(hidden_dim * 2, hidden_dim * 4),
            nn.ReLU(True),
            nn.Linear(hidden_dim * 4, output_dim),
            nn.Tanh()
        )

    def forward(self, x):
        return self.gen(x)


class Discriminator(nn.Module):
    def __init__(self, input_dim, hidden_dim):
        super(Discriminator, self).__init__()
        self.disc = nn.Sequential(
            nn.Linear(input_dim, hidden_dim * 4),
            nn.LeakyReLU(0.2),
            nn.Linear(hidden_dim * 4, hidden_dim * 2),
            nn.LeakyReLU(0.2),
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.LeakyReLU(0.2),
            nn.Linear(hidden_dim, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.disc(x)
# Hyperparameters
z_dim = 100  # Input noise dimension
image_dim = 28 * 28  # Image size for MNIST dataset (28x28 pixels)
hidden_dim = 128  # Hidden layer dimension
batch_size = 64  # Batch size
lr = 0.0002  # Learning rate

# Initialize generator and discriminator
generator = Generator(z_dim, image_dim, hidden_dim)
discriminator = Discriminator(image_dim, hidden_dim)

# Optimizers
gen_optimizer = optim.Adam(generator.parameters(), lr=lr)
disc_optimizer = optim.Adam(discriminator.parameters(), lr=lr)

# Loss function
criterion = nn.BCELoss()
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])
])

dataset = datasets.MNIST(root='mnist_data', train=True, transform=transform, download=True)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
def train_gan(generator, discriminator, dataloader, num_epochs=50):
    for epoch in range(num_epochs):
        for batch_idx, (real_images, _) in enumerate(dataloader):
            batch_size = real_images.size(0)

            # Reshape the real images
            real_images = real_images.view(batch_size, -1)

            # Labels for real and fake data
            real_labels = torch.ones(batch_size, 1)
            fake_labels = torch.zeros(batch_size, 1)

            # Train the discriminator
            disc_optimizer.zero_grad()
            outputs = discriminator(real_images)
            real_loss = criterion(outputs, real_labels)
            real_loss.backward()

            # Generate fake images
            noise = torch.randn(batch_size, z_dim)
            fake_images = generator(noise)
            outputs = discriminator(fake_images.detach())
            fake_loss = criterion(outputs, fake_labels)
            fake_loss.backward()
            disc_optimizer.step()

            disc_loss = real_loss + fake_loss

            # Train the generator
            gen_optimizer.zero_grad()
            outputs = discriminator(fake_images)
            gen_loss = criterion(outputs, real_labels)
            gen_loss.backward()
            gen_optimizer.step()

        # Print the losses and generate images for every epoch
        print(f"Epoch [{epoch+1}/{num_epochs}], Disc Loss: {disc_loss.item()}, Gen Loss: {gen_loss.item()}")

        if (epoch+1) % 10 == 0:
            generate_images(generator)
def generate_images(generator, num_images=16):
    noise = torch.randn(num_images, z_dim)
    fake_images = generator(noise).view(-1, 1, 28, 28)

    grid = np.transpose(torchvision.utils.make_grid(fake_images, nrow=4, normalize=True).cpu(), (1, 2, 0))

    plt.figure(figsize=(5, 5))
    plt.imshow(grid)
    plt.axis('off')
    plt.show()
num_epochs = 50
train_gan(generator, discriminator, dataloader, num_epochs)
