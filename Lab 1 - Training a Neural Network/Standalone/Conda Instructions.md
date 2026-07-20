# Lab 1: Conda

In this version of the lab, you will be using the conda environment in the VM, although these instructions will work for any environment that has Anaconda installed.

## Step 1: Lab directory

Open the `Conda prompt` that is pinned to your task bar. Do not use a regular prompt since it doesn't have Anaconda on its path.

It will default to the `(base)` environment

In this shell, create the `lab1` directory and locate to it.

```bash
mkdir \lab1
cd \lab1
```

## Step 2: Conda environment

You will create a lab conda environment called `transformer` where you will install all the tools necessary to train the transformer

First create the environment.

```bash
conda create --name transformer python=3.10 -y
```

Deactivate the `base` environment and activate the `tranformer` environment.

```bash
conda deactivate
conda activate transformer
```

First, we need to install `pip`. In the example below, pip is already installed by you will need to install it on your VM environment.

```bash
conda install pip
```

Now install all the tools you need for your lab.

```bash
pip install torch transformers datasets accelerate tokenizers numpy matplotlib scikit-learn
```

Optional sanity check, list the packages installed in the environment

```bash
pip list
```

## Step 3: Jupyter Lab

Now install Jupyter and register the kernel then start Jupyter lab. You should be redirected to the web page.

```bash
pip install jupyter
python -m ipykernel install --user --name Transformer --display-name "Lab 1"
```

Clone the lab repository and copy the notebook `LLMTuning.ipynb` to the lab directory

```bash
dir
```

Now start the Jupyter lab

```bash
jupyter lab
```

## Step 4: In the lab

One the lab open, open the notebook and select "Lab 1" as the preferred kernel.

<img src="images/lab17.png" />


