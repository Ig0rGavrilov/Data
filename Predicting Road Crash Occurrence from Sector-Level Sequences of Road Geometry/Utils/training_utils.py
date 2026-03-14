import torch
from torch import nn
from sklearn.metrics import confusion_matrix

def train_step(model: nn.Module,
               dataloader: torch.utils.data.DataLoader,
               loss_fn: torch.nn.Module,
               optimizer: torch.optim.Optimizer,
               device: torch.cuda):
    
    model.train()

    train_loss = 0

    for batch, (X,y) in enumerate(dataloader):
        X, y = X.to(device), y.to(device)

        # Forward pass
        y_pred = model(X)
        y_pred = torch.squeeze(y_pred, dim=1)
        # Calculate loss
        loss = loss_fn(y_pred, y)
        train_loss += loss.item()
        # Set 0 Gradient
        optimizer.zero_grad()
        # Backpropagation
        loss.backward()
        # Update weights
        optimizer.step()

    train_loss = train_loss/(len(dataloader))
    return train_loss



def val_step(model: nn.Module,
               dataloader: torch.utils.data.DataLoader,
               loss_fn: torch.nn.Module,
               device=torch.cuda):
    
    model.eval()
    val_loss = 0

    for batch, (X,y) in enumerate(dataloader):
        X, y = X.to(device), y.to(device)

        # Forward pass
        y_pred = model(X)
        y_pred = torch.squeeze(y_pred, dim=1)
        # Calculate loss
        loss = loss_fn(y_pred, y)
        val_loss += loss.item()

        y_pred_int = (y_pred > 0.5).long()
        cm = confusion_matrix(y, y_pred_int)
        TN = cm[0][0]
        FP = cm[0][1]
        FN = cm[1][0]
        TP = cm[1][1]

        TPR = TP/(TP+FN)
        FAR = FP/(FP+TN)
        

    val_loss = val_loss/(len(dataloader))
    return val_loss, TPR, FAR


def train_function(model: torch.nn.Module,
          train_dataloader: torch.utils.data.DataLoader,
          val_dataloader: torch.utils.data.DataLoader,
          optimizer: torch.optim.Optimizer,
          loss_fn: torch.nn.Module,
          device = torch.cuda,
          epochs: int=5,
          patience: int=10,
          model_name: str="model",
          path: str="/"):
    
    # Create an empty results dictionary
    results = {"train_loss": [],
               "validation_loss": [],
               "TPR":[],
               "FAR":[]}
    counter = 0
    best_val_loss = float('inf')
    for epoch in range(epochs):
        train_loss = train_step(model=model,
                                dataloader=train_dataloader,
                                loss_fn=loss_fn,
                                optimizer=optimizer,
                                device=device)
        
        val_loss, TPR, FAR = val_step(model=model,
                                    dataloader=val_dataloader,
                                    loss_fn=loss_fn,
                                    device=device)
        
        
        print(f"Epoch {epoch+1}  Train Loss {train_loss:.4f} | Validation Loss {val_loss:.4f} | True Positive Rate {TPR:.4f} | False Alarm Rate {FAR:.4f}")

        results["train_loss"].append(train_loss.item() if isinstance(train_loss, torch.Tensor) else train_loss)
        results["validation_loss"].append(val_loss.item() if isinstance(val_loss, torch.Tensor) else val_loss)
        results["TPR"].append(TPR.item() if isinstance(TPR, torch.Tensor) else TPR)
        results["FAR"].append(FAR.item() if isinstance(FAR, torch.Tensor) else FAR)

        if val_loss < best_val_loss:
            best_val_loss = val_loss
            counter = 0

            # Save the best model
            torch.save(model.state_dict(), f"{path}\{model_name}.pth")
        else:
            counter+=1
            if counter >= patience:
                print(f"Early stoppint at epoch {epoch+1}")
                break


    return results