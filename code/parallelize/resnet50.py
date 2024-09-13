import pytorch_lightning as pl
import torch
import torch.nn.functional as F
from torchvision.models import resnet50, ResNet50_Weights

class resnet50Model(pl.LightningModule):
    def __init__(self):
        super().__init__()
        weights = ResNet50_Weights.DEFAULT
        self.model = resnet50(weights=weights)

    def forward(self, x):
        return self.model(x)

    def training_step(self,batch):
        x, labels = batch
        pred=self.forward(x)
        train_loss = F.cross_entropy(pred, labels)
        self.log("training_loss", train_loss)
    
        return train_loss

    def configure_optimizers(self):
            return torch.optim.Adam(self.parameters(), lr=0.02)

