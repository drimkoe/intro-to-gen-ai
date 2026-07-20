# Lab 2: Conda

In this version of the lab, you will be using the conda environment in the VM, although these instructions will work for any environment that has Anaconda installed.

## Step 1: Lab directory

Open the `Conda prompt` that is pinned to your task bar. Do not use a regular prompt since it doesn't have Anaconda on its path.

It will default to the `(base)` environment

In this shell, create the `lab2` directory and locate to it.

```bash
(base) C:\Users\micro>mkdir \lab2
(base) C:\Users\micro>cd \lab2
(base) C:\lab2>
```

## Step 2: Conda environment

The setup instructions in the Jupyter notebook seem to run into problems in Windows environments.  Use these instructions instead

Create the lab conda environment

```bash
conda create -n vae python=3.10 -y
conda activate vae
```

First, we need to install `pip`. In the example below, pip is already installed by you will need to install it on your VM environment.

```bash
(transformer) C:\lab1>conda install pip
Channels:
 - defaults
Platform: win-64
Collecting package metadata (repodata.json): done
Solving environment: done

# All requested packages already installed.

```

Now install all the tools you need for your lab.

```bash
conda install -y numpy matplotlib jupyterlab ipykernel
pip install --index-url https://download.pytorch.org/whl/cpu torch torchvision torchaudio
```

Test to ensure that torch is working properly

```bash
python -c "import torch; print(torch.__version__)"
```

If this produces an error, then run this in the environment, and confirm that torch works.

```bash
conda install -y -c conda-forge vs2015_runtime
```



## Step 3: Jupyter Lab



Copy the notebook `VAE.ipynb` to the lab directory
N
ow install thr Jupyter kernel and register the kernel then start Jupyter lab. You should be redirected to the web page.

```bash
python -m ipykernel install --user --name vae --display-name "VAE"
jupyter lab
```

N

