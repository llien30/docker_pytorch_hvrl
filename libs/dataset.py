import torch
import torchvision.transforms as transforms
from torchvision import datasets


def load_MNIST(batch=128, intensity=1.0):
    train_loader = torch.utils.data.DataLoader(
        datasets.MNIST(
            "./data",
            train=True,
            download=True,
            transform=transforms.Compose(
                [transforms.ToTensor(), transforms.Lambda(lambda x: x * intensity)]
            ),
        ),
        batch_size=batch,
        shuffle=True,
    )

    test_loader = torch.utils.data.DataLoader(
        datasets.MNIST(
            "./data",
            train=False,
            transform=transforms.Compose(
                [transforms.ToTensor(), transforms.Lambda(lambda x: x * intensity)]
            ),
        ),
        batch_size=batch,
        shuffle=True,
    )

    return {"train": train_loader, "test": test_loader}
