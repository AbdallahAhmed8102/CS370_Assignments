{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "vscode": {
     "languageId": "plaintext"
    }
   },
   "outputs": [],
   "source": [
    "from anomalib.models import EfficientAD\n",
    "\n",
    "# Initialize the model\n",
    "model_efficientad = EfficientAD()\n",
    "\n",
    "# Train the model for each category\n",
    "auroc_efficientad_results = {}\n",
    "for category in categories:\n",
    "    model_efficientad.train(datasets[category].train)  # Train the model\n",
    "    auroc_score = model_efficientad.evaluate(datasets[category].test)  # Evaluate the model\n",
    "    auroc_efficientad_results[category] = AUROC(auroc_score)\n",
    "\n",
    "# Print AUROC scores for EfficientAD\n",
    "for category, score in auroc_efficientad_results.items():\n",
    "    print(f\"EfficientAD AUROC for {category}: {score:.4f}\")\n",
    "\n",
    "# Calculate the average AUROC score\n",
    "average_auroc_efficientad = sum(auroc_efficientad_results.values()) / len(categories)\n",
    "print(f\"Average AUROC for EfficientAD: {average_auroc_efficientad:.4f}\")\n"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
