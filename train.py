import matplotlib.pyplot as plt
import torch
import torch.nn.functional as f

from libs.dataset import load_MNIST
from libs.model import MyNet


def main():
    epoch = 5

    net = MyNet()
    loaders = load_MNIST()
    optimizer = torch.optim.Adam(params=net.parameters(), lr=0.001)

    history = {
        "train_loss": [],
        "test_loss": [],
        "test_acc": [],
    }

    for e in range(epoch):
        loss = None
        net.train(True)  # 引数は省略可能
        for i, (data, target) in enumerate(loaders["train"]):
            data = data.view(-1, 28 * 28)

            optimizer.zero_grad()
            output = net(data)
            loss = f.nll_loss(output, target)
            loss.backward()
            optimizer.step()

            if i % 10 == 0:
                print(
                    "Training log: {} epoch ({} / 60000 train. data). Loss: {}".format(
                        e + 1, (i + 1) * 128, loss.item()
                    )
                )

        history["train_loss"].append(loss.detach().numpy())
        net.eval()  # または net.train(False) でも良い
        test_loss = 0
        correct = 0

        with torch.no_grad():
            for data, target in loaders["test"]:
                data = data.view(-1, 28 * 28)
                output = net(data)
                test_loss += f.nll_loss(output, target, reduction="sum").item()
                pred = output.argmax(dim=1, keepdim=True)
                correct += pred.eq(target.view_as(pred)).sum().item()

        test_loss /= 10000

        print("Test loss (avg): {}, Accuracy: {}".format(test_loss, correct / 10000))

        history["test_loss"].append(test_loss)
        history["test_acc"].append(correct / 10000)

    # 結果の出力と描画
    plt.figure()
    plt.plot(range(1, epoch + 1), history["train_loss"], label="train_loss")
    plt.plot(range(1, epoch + 1), history["test_loss"], label="test_loss")
    plt.xlabel("epoch")
    plt.legend()
    plt.savefig("loss.png")

    plt.figure()
    plt.plot(range(1, epoch + 1), history["test_acc"])
    plt.title("test accuracy")
    plt.xlabel("epoch")
    plt.savefig("test_acc.png")


if __name__ == "__main__":
    main()
