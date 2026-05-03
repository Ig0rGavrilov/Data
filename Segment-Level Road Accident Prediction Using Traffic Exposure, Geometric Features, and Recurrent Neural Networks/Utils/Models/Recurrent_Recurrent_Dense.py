import torch
import torch.nn as nn

class RNN(nn.Module):
    def __init__(self, input_dim, hidden_dim_layer1, hidden_dim_layer2,bidirectional_layer1, bidirectional_layer2, output_dim, dropout):
        super().__init__()

        self.bl1 = 2 if bidirectional_layer1 else 1
        self.bl2 = 2 if bidirectional_layer2 else 1

        # RNN Layer 
        self.rnn_layer1 = nn.RNN(input_size=input_dim, 
                                 hidden_size=hidden_dim_layer1,                                 
                                 bidirectional = bidirectional_layer1, 
                                 batch_first=True)
        
        # Dropout Layer 1
        self.dropout1 = nn.Dropout(dropout)
        # RNN Layer 
        self.rnn_layer2 = nn.RNN(input_size=hidden_dim_layer1*self.bl1, 
                                 hidden_size=hidden_dim_layer2, 
                                 bidirectional = bidirectional_layer2, 
                                 batch_first=True)

       # Dropout Layer 2
        self.dropout2 = nn.Dropout(dropout)

        self.fc = nn.Linear(hidden_dim_layer2*self.bl2, output_dim)
        

    def forward(self, x):
        # RNN Layer 1
        out, _ = self.rnn_layer1(x)

        # Dropout Layer 2
        out = self.dropout1(out)

        # RNN Layer 3
        out, _ = self.rnn_layer2(out)

        out = out[:,-1,:] # Last timestep
        
        # Dropout Layer 4
        out = self.dropout2(out)

        # Full Connected Layer 5
        output = self.fc(out)

        return output
    
class GRU(nn.Module):
    def __init__(self, input_dim, hidden_dim_layer1, bidirectional_layer1, hidden_dim_layer2, bidirectional_layer2, dropout, output_dim):
        super().__init__()

        self.bl1 = 2 if bidirectional_layer1 else 1
        self.bl2 = 2 if bidirectional_layer2 else 1

        # GRU Layer 1
        self.gru_layer1 = nn.GRU(input_size=input_dim, 
                          hidden_size=hidden_dim_layer1,
                          bidirectional = bidirectional_layer1, 
                          batch_first=True)
        # Dropout Layer 1
        self.dropout1 = nn.Dropout(dropout)
        # GRU Layer 2
        self.gru_layer2 = nn.GRU(input_size=hidden_dim_layer1*self.bl1, 
                          hidden_size=hidden_dim_layer2,
                          bidirectional = bidirectional_layer2, 
                          batch_first=True)
        
        # Dropout Layer 2
        self.dropout2 = nn.Dropout(dropout)
        
        self.fc = nn.Linear(hidden_dim_layer2*self.bl2, output_dim)

    def forward(self, x):
        # GRU Layer 1
        out, _ = self.gru_layer1(x)

        # Dropout Layer 2 
        out = self.dropout1(out)

        # GRU Layer 3
        out, _ = self.gru_layer2(out)

        out = out[:,-1,:] # Last timestamp
        
        # Dropout Layer 4
        out = self.dropout2(out)

        # Full Connected Layer 5      
        output = self.fc(out)

        return output
    
class LSTM(nn.Module):
    def __init__(self, input_dim, hidden_dim_layer1, bidirectional_layer1, hidden_dim_layer2, bidirectional_layer2, output_dim, dropout):
        super().__init__()
        self.bl1 = 2 if bidirectional_layer1 else 1
        self.bl2 = 2 if bidirectional_layer2 else 1
        
        # LSTM Layer 1
        self.lstm1 = nn.LSTM(input_size=input_dim, hidden_size=hidden_dim_layer1, batch_first=True, bidirectional = bidirectional_layer1)
        # Dropout Layer 1
        self.dropout1 = nn.Dropout(dropout)
        # LSTM Layer 2    
        self.lstm2 = nn.LSTM(input_size=hidden_dim_layer1*self.bl1, hidden_size=hidden_dim_layer2, bidirectional = bidirectional_layer2)
        # Dropout Layer 2
        self.dropout2 = nn.Dropout(dropout)
        # Full Connected Layer
        self.fc = nn.Linear(hidden_dim_layer2*self.bl2, output_dim)

    def forward(self, x):
        # LSTM Layer 1
        out, _ = self.lstm1(x)
        
        # Dropout Layer 2
        out = self.dropout1(out)
        
        # LSTM Layer 3
        out, _ = self.lstm2(out)
        
        out = out[:,-1,:] # Last timestamp
        
        # Dropout Layer 4
        out = self.dropout2(out) 
        
        # Full Connected Layer 5
        output = self.fc(out)
      
        return output