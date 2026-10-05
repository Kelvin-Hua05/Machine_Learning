# Getting Started with Anaconda

## Start using Anaconda

1. Install anaconda

2. activate it

```bash
source ~/anaconda3/bin/activate
#/anaconda3 is the place i installed anaconda

conda init
```

Then your terminal will look like:

```bash
(base) max@223ubuntu:~/workspace/machineLearning$
```

Hint: How to leave anaconda?

Simply type

```bash
conda deactivate
```

## Create an environment for python script

```bash
conda create --name envName python=3.11
```

## see all environment created

```bash
conda env list
```

## switch to a environment

```bash
conda activate envName
```

Then base would turn into envName

## Installing packages

```bash
conda install packageName
```

## Removing packages

```bash
conda remove --name envName packageName
```

## Removing environment

```bash
conda env remove --name envName
```
