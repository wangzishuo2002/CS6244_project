import os
import random

root_path = './data/zalando-hd-resize/train/image-parse-v3-finetune'
finetune_all = os.listdir(root_path)
random.shuffle(finetune_all)
pairs_all = []
for i in range(0,len(finetune_all),2):
    pairs_all.append([finetune_all[i][:-3] + 'jpg', finetune_all[i+1][:-3] + 'jpg'])
    pairs_all.append([finetune_all[i+1][:-3] + 'jpg', finetune_all[i][:-3] + 'jpg'])

random.shuffle(pairs_all)
print(len(pairs_all))
for i in range(len(pairs_all)):
    with open('./data/zalando-hd-resize/train_pairs_finetune.txt', 'a+') as file:
        file.write(pairs_all[i][0] + ' ' + pairs_all[i][1] + '\n')




