# main.py

from data_loader import load_data
from models import train_and_evaluate_models
from visualization import plot_results

def main():
    # Load the MVTec-AD dataset
    datasets = load_data()  
    
    # Train models and get results
    results = train_and_evaluate_models(datasets)  
    
    # Visualize results
    plot_results(results)  

if __name__ == "__main__":
    main()
