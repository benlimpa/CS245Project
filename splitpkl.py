import pickle
import gzip
import os
import time

PKL_FILEPATH = "fr_dbp15k_link_img_dict_full.pkl"
OUTDIR = "~/pkls"
SUBSET_SIZE = 1000

def save_pkl(subset, path):
    with gzip.open(path, "wb") as f:
        pickle.dump(subset, f)

with open(PKL_FILEPATH, "rb") as f:
    tic = time.time()
    data = pickle.load(f)
    print(f"Loaded data in {time.time() - tic} seconds")

    subset = dict()
    subset_ind = 0
    tic = time.time()
    for key, value in data.items():
        subset[key] = value

        if len(subset) == SUBSET_SIZE:
            print(f"Got subset in {time.time() - tic} seconds")
            tic = time.time()
            save_pkl(subset, os.path.join(OUTDIR, f"{subset_ind}.pkl.gz"))
            print(f"Saved {len(subset)} items in {time.time() - tic} seconds")
            tic = time.time()
            subset_ind += 1
            subset = dict()
    if len(subset) > 0:
        print(f"Got subset in {time.time() - tic} seconds")
        tic = time.time()
        save_pkl(subset, os.path.join(OUTDIR, f"{subset_ind}.pkl.gz"))
        print(f"Saved FINAL {len(subset)} items in {time.time() - tic} seconds")
