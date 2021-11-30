# CS245Project

# Terminology, Acronyms, and other stuff they didn't bother to explain
- ills: entity links (typically in the form of two hyperlinks that refer to the same object)
- rel: relationships


# Notes

## Experiments in reducing embedding size:

- emb_sizes = (relation, attribute, image)

Benchmark:
- cell runtime: 57 sec
- emb_sizes = 100, 100, 200; graph = 200
```
l2r: acc of top [1, 10, 50] = [0.1588 0.3899 0.6066], mr = 472.792, mrr = 0.235, time = 19.4155 s 
r2l: acc of top [1, 10, 50] = [0.1528 0.3938 0.6022], mr = 477.969, mrr = 0.233, time = 19.4165 s 
```

Half-length embeddings:
- cell runtime: 53 sec
- emb_sizes = 50, 50, 100; graph = 100
```
l2r: acc of top [1, 10, 50] = [0.1315 0.3661 0.587 ], mr = 481.222, mrr = 0.209, time = 19.4183 s 
r2l: acc of top [1, 10, 50] = [0.133  0.3636 0.5822], mr = 487.313, mrr = 0.209, time = 19.4200 s 
```

Half-length image embedding:
- cell runtime: 53 sec
- emb_sizes = 100, 100, 100; graph = 200
```
l2r: acc of top [1, 10, 50] = [0.1515 0.385  0.6084], mr = 426.256, mrr = 0.230, time = 19.2522 s 
r2l: acc of top [1, 10, 50] = [0.1487 0.3879 0.6058], mr = 430.392, mrr = 0.229, time = 19.2528 s 
```
Quarter-length image embedding:
- cell runtime: 53 sec
- emb_sizes = 100, 100, 50; graph = 200
```
l2r: acc of top [1, 10, 50] = [0.1532 0.3877 0.6077], mr = 439.124, mrr = 0.231, time = 19.4410 s 
r2l: acc of top [1, 10, 50] = [0.1508 0.3929 0.605 ], mr = 443.180, mrr = 0.231, time = 19.4416 s 
```
10-length image embedding:
- cell runtime: 53 sec
- emb_sizes = 100, 100, 10; graph = 200
```
l2r: acc of top [1, 10, 50] = [0.129  0.3652 0.5949], mr = 396.255, mrr = 0.207, time = 19.5654 s 
r2l: acc of top [1, 10, 50] = [0.1233 0.3682 0.592 ], mr = 401.066, mrr = 0.203, time = 19.5659 s 
```