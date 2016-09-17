last update 30/08/2016
by Wasit Limprasert

# algae_marker.py 
To label objects,

1. put all images (*.jpg) in folder /dataset
2. Press number key (0 to 9) to select calss of object. There are avialable 10 classes
3. [left click] or ctrl + [left click] on image to label the area of object
4. alt + [left click] to remove the label
5. space bar to save
6. esc to close the window

# algae_prep.py
To prepare the feature vectors (x) and labels (y). Uncomment to check the cross val_score()

# algae_train.py
To train a tree and save to dataset/timestamp.tree.

# algae_combine.py
To cimbined all tree into dataset/forest.pic

# algae_predict.py
Using forest.pic to identify and count objects








