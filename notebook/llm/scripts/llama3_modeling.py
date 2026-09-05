from math import ceil

# model configs
byte_size = 2 # bfloat16 is 2 bytes
n_layers = 80
H = 8192
I = 28672
n_q = 64
n_kv = 8
d_head = 128
vocab = 128256

for TP in (1, 4, 8, 64):
    n_kv_heads = ceil(n_kv / TP)
    n_heads = ceil(n_q / TP) + n_kv_heads * 2
    
    weights_total = sum([
        vocab / TP * H * byte_size, # embedding_w
        (n_heads * d_head) * H * n_layers * byte_size, # QKV_w
        (n_heads * d_head) * H * n_layers * byte_size, # out_w
        3 * (H / TP * I) * n_layers * byte_size, # gate_w + up_w + down_w
        2 * H * n_layers * byte_size, # norm_w, 2 RMS norm per layer
        vocab * H / TP * byte_size# lm_head_w
    ]) / 1024 / 1024 / 1024
    
    kv_cache_per_tok = 2 * n_kv_heads * d_head * n_layers * byte_size / 1024 / 1024
    print(f"TP={TP}")
    print(f"Total weights: {weights_total: .2f}Gb")
    print(f"KV Cache per token: {kv_cache_per_tok : .4f}Mb")

# TP=1
# Total weights:  133.92Gb
# KV Cache per token:  0.3125Mb
# TP=4
# Total weights:  33.48Gb
# KV Cache per token:  0.0781Mb
# TP=8
# Total weights:  16.74Gb
# KV Cache per token:  0.0391Mb
# TP=64
# Total weights:  2.64Gb
# KV Cache per token:  0.0391Mb