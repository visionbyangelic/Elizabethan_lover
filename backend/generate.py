import torch
import pickle
import model 
import GPTConfig, GPT

#load tokenizer
with open('meta.pkl', 'rb') as f:
    meta = pickle.load(f)
    stoi, itos = meta['stoi'], meta['itos']
    
#load model
ckpt = torch.load('ckpt.pt', map_location='cpu')
config = GPTConfig(
    vocab_size=ckpt['model_args']['vocab_size'], 
    block_size=ckpt['model_args']['block_size'],
    n_layer=ckpt['model_args']['n_layer'], 
    n_head=ckpt['model_args']['n_head'], 
    n_embd=ckpt['model_args']['n_embd']
)
model = GPT(config)
model.load_state_dict(ckpt['model'])
model.eval()

def encode(text):
    return torch.tensor([stoi[c] for c in text], dtype=torch.long).unsqueeze(0)

def decode(tokens):
    return ''.join([itos[t] for t in tokens])

@torch.no_grad()
def generate_text(prompt, max_new_tokens=50):
    input_ids = encode(prompt)
    out = model.generate(input_ids, max_new_tokens=max_new_tokens)
    return decode(out[0].tolist())