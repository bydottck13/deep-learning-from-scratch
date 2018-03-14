# Deep Learning from Scratch

------

## Environments
* Install Jupyter with pip
```
$ sudo apt-get install -y python3-pip
$ sudo python3 -m pip install --upgrade pip
$ sudo python3 -m pip install jupyter
$ jupyter notebook
```

* Install relative python packages
```
$ sudo pip3 install -r requirements.txt
```

* Using Jupyter Notebook on Nvidia TX2
```
$ jupyter notebook --generate-config
```

Then, modify `c.NotebookApp.ip = 'localhost'` to `c.NotebookApp.ip = '{Your IP}'`
```
$ vi /home/nvidia/.jupyter/jupyter_notebook_config.py
$ jupyter notebook --no-browser --port 8004
```

Finally, open your browser and paste the url `http://{Your IP}:8004/?token={Your token}`.

## Image sets
Download from ImageNet for non-commerical purposes. Put files into the following directories:
* `wolf`: label to 0
* `not-cat`: label to 0
* `cat`: label to 1

## Reference
* [Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning)
* [ImageNet](http://www.image-net.org)
* [Nvidia Jetson TX2](https://developer.nvidia.com/embedded/buy/jetson-tx2)

