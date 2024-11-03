# data_loader.py

from anomalib.data import MVTecAD

def load_data():
    # Load only flat surface categories: 'tile', 'leather', 'grid'
    categories = ['tile', 'leather', 'grid']
    datasets = {}
    
    for category in categories:
        dataset = MVTecAD(category=category)
        datasets[category] = dataset
    
    return datasets
