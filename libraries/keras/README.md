Keras research 

Actual model params fits:

```python train.py --img 640 --batch 8 --epochs 5 --data config.yaml --weights yolov5s.pt```

```python .\detect.py --weights .\runs\train\exp\weights\best.pt --conf 0.05 --source ..\auto.jpg
```

```python train.py --img 640 --batch 16 --epochs 5 --data plate.yaml --weights yolov5m.pt --cache disk --cache ram```