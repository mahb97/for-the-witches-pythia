"""pythia demo"""

import pythia

pythia.enable()


def average_loss(losses):
    return sum(losses) / len(losses)


def summarize_run(checkpoints):
    losses = [c["val_loss"] for c in checkpoints]
    return {
        "mean_val_loss": average_loss(losses),
        "n_checkpoints": len(checkpoints),
    }


run = []  # forgot to load checkpoints
print(summarize_run(run))
