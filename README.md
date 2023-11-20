# Finetuning fpr Thinkport

This repository holds training data to finetune and OpenAI model. It also contains a script to convert the training data to the format that the OpenAI model expects.

## Install

To install the dependencies, run:

    ```python
    pip install -r requirements.txt
    ```

## Usage

### Training

```python
python finetune.py --model_name=gpt3 --model_checkpoint=gpt3
```

### Validation

```python
validate.py --model_name=gpt3 --model_checkpoint=gpt3
```

### Convert to OpenAI format

To convert the training data to the format that the OpenAI model expects, run:

```python
python convert.py --model_name=gpt3 --model_checkpoint=gpt3
```
