# CS6244_project: Towards More Realistic Hand Preservation in High-Resolution Virtual Try-On

# Our environment setup is similar to [HR-VITON](https://github.com/sangyun884/HR-VITON)

## Dataset & Weights
You can find our finetune dataset and pretrained weights in [google drive]([https://github.com/sangyun884/HR-VITON](https://drive.google.com/drive/folders/1MOrBbNxtHis6jP6cXXs2MPRkIZrdCA7l))

## Inference
```python
python3 test_generator.py --occlusion --cuda {True} --test_name {test_name} --tocg_checkpoint {condition generator ckpt} --gpu_ids {gpu_ids} --gen_checkpoint {image generator ckpt} --datasetting unpaired --dataroot {dataset_path} --data_list {pair_list_textfile}
```

## Train try-on condition generator
```python
python3 train_condition_finetune.py --cuda {True} --gpu_ids {gpu_ids} --Ddownx2 --Ddropout --lasttvonly --interflowloss --occlusion
```
