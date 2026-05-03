import torch
import torch.nn as nn

class LSTM(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, bidirectional, dropout):
        super().__init__()
        self.bl = 2 if bidirectional else 1
        # LSTM Layer 1
        self.lstm = nn.LSTM(input_size=input_dim, hidden_size=hidden_dim, batch_first=True, bidirectional = bidirectional)
        # Dropout Layer 2
        self.dropout = nn.Dropout(dropout)
        # Full Connected
        self.fc = nn.Linear(hidden_dim*self.bl, output_dim)

    def forward(self, x):
        # LSTM Layer 1
        out, _ = self.lstm(x)
        
        out = out[:,-1,:] # Last timestep
        
        # Dropout Layer 2
        out = self.dropout(out)
        
        # Full Connected Layer 3
        output = self.fc(out)

        return output
    
class GRU(nn.Module):
    def __init__(self, input_dim, hidden_dim, bidirectional, dropout, output_dim):
        super().__init__()
        self.bl = 2 if bidirectional else 1

        # GRU Layer 1
        self.gru = nn.GRU(input_size=input_dim, hidden_size=hidden_dim, batch_first=True, bidirectional = bidirectional)

         # Dropout Layer 2
        self.dropout = nn.Dropout(dropout)
       
        # Full Connected Layer 3
        self.fc = nn.Linear(hidden_dim*self.bl, output_dim)

    def forward(self, x):
        # GRU Layer 1
        out, _ = self.gru(x)
        
        out = out[:,-1,:] # Last timestep
        
        # Dropout Layer 2
        out = self.dropout(out)
        
        # Full Connected Layer 3
        output = self.fc(out)
     
        return output
    
    
class RNN(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, bidirectional,dropout):
        super().__init__()
        self.bl = 2 if bidirectional else 1
        # RNN Layer 1
        self.rnn = nn.RNN(input_size=input_dim, hidden_size=hidden_dim, batch_first=True, bidirectional = bidirectional)
       
        # Dropout Layer 2
        self.dropout = nn.Dropout(dropout)

        # Fully Connected Layer 3
        self.fc = nn.Linear(hidden_dim*self.bl, output_dim)

    def forward(self, x):
        # RNN Layer 1
        out, _ = self.rnn(x)
        
        out = out[:,-1,:] # Last timestep
        
        # Dropout Layer 2
        out = self.dropout(out)
        
        # Full Connected Layer 3
        output = self.fc(out)
        
        return output