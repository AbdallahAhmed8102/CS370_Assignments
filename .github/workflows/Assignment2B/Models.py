# visualization.py

import matplotlib.pyplot as plt

def plot_results(results):
    categories = list(results.keys())
    patchcore_scores = [results[cat]['PatchCore'] for cat in categories]
    efficientad_scores = [results[cat]['EfficientAD'] for cat in categories]

    plt.figure(figsize=(12, 6))
    x = np.arange(len(categories))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    bars1 = ax.bar(x - width/2, patchcore_scores, width, label='PatchCore', color='blue')
    bars2 = ax.bar(x + width/2, efficientad_scores, width, label='EfficientAD', color='orange')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('AUROC Score')
    ax.set_title('Model Performance on MVTec-AD Dataset')
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()

    # Adding the numerical values on top of the bars
    for bar in bars1 + bars2:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
