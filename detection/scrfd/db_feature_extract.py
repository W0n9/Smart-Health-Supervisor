import os
import pickle
from backbones import get_model
from torch.utils.data.dataloader import DataLoader
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
import torch


def encode(db_path, model_path, model_name='VGG-Face'):

    if os.path.isdir(db_path) == True:
        file_name = "representations.pkl"

        if os.path.exists(db_path+"/"+file_name):
            f = open(db_path+'/'+file_name, 'rb')
            db_items = pickle.load(f)
            print("There are ", len(db_items)," representations found in ",file_name)
            labels = [i[0][0] for i in db_items]
            db_embeddings = [i[1][0] for i in db_items]
            db_embeddings = torch.vstack(db_embeddings)
        else:
            transform_dict = transforms.Compose(
                            [transforms.Resize([112, 112]),
                            transforms.ToTensor(),
                            transforms.Normalize(std=[0.5,0.5,0.5], mean=[0.5,0.5,0.5])]
                        )
            dataset = ImageFolder(root=db_path, transform=transform_dict)
            dataloader = DataLoader(dataset, shuffle=False, num_workers=1, batch_size=1)
            db = []
            with torch.no_grad():
                for idx, (data, target) in enumerate(dataloader):
                    db_embeddings = []
                    net = get_model(model_name, fp16=False)
                    net.load_state_dict(torch.load(model_path))
                    net.eval()
                    outs = net(data)
                    # outs = inference(model_path, model_name, data)
                    labels = [dataset.classes[t] for t in target]
                    db_embeddings.append(labels)
                    db_embeddings.append(outs)
                    db.append(db_embeddings)
            f = open(db_path+'/'+file_name, "wb")
            pickle.dump(db, f)
            f.close()
            print('finish extracting!')
            labels = [i[0][0] for i in db]
            db_embeddings = [i[1][0] for i in db]
            db_embeddings = torch.vstack(db_embeddings)
    return db_embeddings, labels
            
            
            


if __name__ == '__main__':
    encode(db_path="D:/face/database_aligned/", 
    model_path="C:/Users/DELL/Downloads/ms1mv3_arcface_r50_fp16_backbone.pth", 
    model_name='r50')
    f = open("D:/face/database_aligned/representations.pkl", 'rb')
    db_embeddings = pickle.load(f)
    labels = [i[0][0] for i in db_embeddings]
    labels = torch.vstack(labels)
    print(labels.size())
