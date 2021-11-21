from fastapi import FastAPI, File, UploadFile
from efficientnet_pytorch import EfficientNet
import pickle
from PIL import Image
from torchvision import transforms
import torch
from collections import Counter

app = FastAPI()
model = EfficientNet.from_pretrained('efficientnet-b0')
model.eval()

with open('magic_list.pickle', 'rb') as f:
    magic_list = pickle.load(f)
with open('svd2000.pickle', 'rb') as f:
    svd = pickle.load(f)

with open('knn2000.pickle', 'rb') as f:
    knn = pickle.load(f)

def pic_to_emb(pic_path, model, svd, magic_list):
    size = 224
    tfms = transforms.Compose([transforms.Resize(size),transforms.CenterCrop(size), transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),])
    p =pic_path
    try:
        img = tfms(Image.open(p)).unsqueeze(0)

        with torch.no_grad():
            features = model.cpu().extract_features(img).numpy()
            emb = svd.transform(features.reshape(1, -1))
        calories = 0
        cats = Counter()
        for prob, item in zip(knn.predict_proba(emb).reshape(-1), magic_list):
            calories += prob * item[1]
            for c in item[2]:
                cats[c] += prob
        return {'calories': calories, 'categories' : [x for x in cats.most_common(5) if x[1] > 0.2]}
    except Exception as a:
        raise a
        #print(Image.open(p).size)

@app.post("/process_image")
async def create_upload_file(image: UploadFile = File(...)):
    file_name = image.filename.replace(" ", "-")
    with open(file_name, 'wb+') as f:
        f.write(image.file.read())
        f.close()
    return pic_to_emb(file_name , model, svd, magic_list)
