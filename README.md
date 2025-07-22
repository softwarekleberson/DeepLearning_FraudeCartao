# Fraud Detection in Financial Transactions Using Machine Learning

## Authors
- **Kleberson Dos Santos Silva**  
- **Mariângela F.F. Molina**

## Abstract
This project compares three machine learning algorithms — Decision Tree, Random Forest, and AdaBoost — for fraud detection in credit card transactions. The study evaluates the impact of these approaches in terms of accuracy, precision, and recall, considering challenges such as class imbalance and computational efficiency.

## Keywords
- Decision Tree  
- Random Forest  
- AdaBoost  
- Gini Index  
- Fraud Detection

## Article Structure
1. **Introduction**  
   Discussion on the growing use of machine learning in credit card fraud detection.
2. **Materials and Methods**  
   - Algorithms: Decision Tree (CART), Random Forest, and AdaBoost.  
   - Data: 284,807 transactions, with 0.17% fraudulent.  
   - Implementation strategies and comparative analysis.
3. **Theoretical Framework**  
   Review of advanced techniques for fraud detection.
4. **Results and Discussion**  
   Detailed comparison of algorithm performance in terms of accuracy, precision, and recall.
5. **Conclusion**  
   AdaBoost stood out as the most effective in complex scenarios, while Random Forest showed a good balance between performance and computational cost.

## Results

| Algorithm         | Accuracy | Recall | Execution Time |
|------------------|----------|--------|----------------|
| Decision Tree     | 99.1%    | 0.71   | 5:29           |
| Random Forest     | 99.4%    | 0.75   | 15:55          |
| AdaBoost          | 99.6%    | 0.79   | 23:05          |

## Dataset
- **Total transactions**: 284,807  
- **Fraudulent transactions**: 492 (0.17%)  
- **Legitimate transactions**: 284,315 (99.83%)

Class imbalance was handled using the `StratifiedShuffleSplit` library.

## Code Repository
The source code used for implementing the algorithms is available on [GitHub](https://github.com/softwarekleberson/DeepLearning_FraudeCartao).

## References
- DEVI, D. et al. *A Cost-sensitive Weighted Random Forest Technique for Credit Card Fraud Detection*. IEEE Xplore, 2019.  
- KHINE, A.A.; KHIN, H.W. *Credit Card Fraud Detection Using Online Boosting with Extremely Fast Decision Tree*. IEEE Xplore, 2020.  
- LIN, T.H.; JIANG, J.R. *Credit Card Fraud Detection with Autoencoder and Probabilistic Random Forest*. MDPI, 2021.  
- [More references available in the article](https://github.com/softwarekleberson/DeepLearning_FraudeCartao)

## Contact
For more information, please contact the authors.
