
import torchvision.models as models

def load_model():
    model = models.resnet18(pretrained=True)
    return model

if __name__ == "__main__":
    model = load_model()
    print("Pretrained ResNet18 model loaded successfully.")
