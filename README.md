# Finetuning for Thinkport GmbH

This repository holds training data to finetune and OpenAI model. It also contains a script to convert the training data to the format that the OpenAI model expects.

## Install

To install the dependencies, run:

    ```python
    pip install -r requirements.txt
    ```

## Usage

### Validation

It is importend to validate your data to prevent wasting money on training.

    ```python
    phyton3 validate.py
    ```

### Training

When you are done with validating your data, you can start training.

    ```python
    python3 finetune.py
    ```
