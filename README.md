# Fine tuning for Thinkport GmbH

This repository holds training data to finetune and OpenAI model. It also contains a script to convert the training data to the format that the OpenAI model expects.

## Install

To install the dependencies, run:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Validation

It is importend to validate your data to prevent wasting money on training.

    ```bash
    phyton3 validate.py
    ```

### Training

When you are done with validating your data, you can start training.

    ```bash
    python3 finetune.py
    ```

Now visit the OpenAI website to see your training progress. It will take a couple of hours to train. And it wil cost you money. To test the model, visit the [playground](https://platform.openai.com/playground) and select the new model.
