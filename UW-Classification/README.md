# Deep Learning from University of Washington courses

------

## Environments
* Download and Install ANACONDA(Python 2.7 version) from [here](https://www.anaconda.com/download/)
```
$ bash ~/Downloads/Anaconda2-5.2.0-Linux-x86_64.sh
$ source ~/.bashrc
```

* Install GraphLab Create, and remember to register a [license](https://turi.com/download/academic.html) with a Coursera student
```
$ conda create -n gl-env python=2.7 anaconda=4.0.0
$ source activate gl-env
$ conda update pip
$ pip install --upgrade --no-cache-dir https://get.graphlab.com/GraphLab-Create/2.1/{your registered email address here}/{your product key here}/GraphLab-Create-License.tar.gz
$ conda install ipython-notebook
```

* Install sframe
```
$ pip install -U sframe
```

* Launch jupyter notebook
```
$ jupyter notebook
```

## Reference
* [Anaconda installer for Linux](https://docs.anaconda.com/anaconda/install/linux)
* [GraphLab Create](https://turi.com/download/install-graphlab-create-command-line.html)
* [Machine Learning: Classification](https://www.coursera.org/learn/ml-classification)

