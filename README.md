# Detecção de Fraudes em Transações Financeiras usando Aprendizado de Máquina

## Autores
- **Kleberson Dos Santos Silva**  
- **Mariângela F.F. Molina**

## Resumo
Este projeto compara três algoritmos de aprendizado de máquina — Árvore de Decisão, Floresta Aleatória e AdaBoost — para detecção de fraudes em transações com cartão de crédito. O estudo avalia o impacto dessas abordagens em termos de acurácia, precisão e recall, considerando desafios como desbalanceamento de classes e eficiência computacional.

## Palavras-chave
- Árvore de Decisão
- Floresta Aleatória
- AdaBoost
- Índice de Gini
- Detecção de Fraude

## Estrutura do Artigo
1. **Introdução**  
   Discussão sobre o uso crescente de aprendizado de máquina na detecção de fraudes em cartões de crédito.
2. **Materiais e Métodos**  
   - Algoritmos: Árvore de Decisão (CART), Floresta Aleatória e AdaBoost.  
   - Dados: 284.807 transações, sendo 0,17% fraudulentas.  
   - Estratégias de implementação e análise comparativa.
3. **Referencial Teórico**  
   Revisão de técnicas avançadas para detecção de fraudes.
4. **Resultados e Discussão**  
   Comparação detalhada do desempenho dos algoritmos em termos de acurácia, precisão e recall.
5. **Conclusão**  
   AdaBoost se destacou como o mais eficaz em cenários complexos, enquanto a Floresta Aleatória apresentou um bom equilíbrio entre desempenho e custo computacional.

## Resultados
| Algoritmo           | Acurácia | Recall | Tempo de Execução |
|---------------------|----------|--------|-------------------|
| Árvore de Decisão   | 99.1%    | 0.71   | 5:29              |
| Floresta Aleatória  | 99.4%    | 0.75   | 15:55             |
| AdaBoost            | 99.6%    | 0.79   | 23:05             |

## Conjunto de Dados
- **Total de transações**: 284.807  
- **Transações fraudulentas**: 492 (0,17%)  
- **Transações legítimas**: 284.315 (99,83%)

O desbalanceamento das classes foi tratado utilizando a biblioteca `StratifiedShuffleSplit`.

## Repositório de Código
O código-fonte usado para a implementação dos algoritmos está disponível no [GitHub](https://github.com/softwarekleberson/DeepLearning_FraudeCartao).

## Referências
- DEVI, D. et al. *A Cost-sensitive weighted Random Forest Technique for Credit Card Fraud Detection*. IEEE Xplore, 2019.  
- KHINE, A.A.; KHIN, H.W. *Credit Card Fraud Detection Using Online Boosting with Extremely Fast Decision Tree*. IEEE Xplore, 2020.  
- LIN, T.H.; JIANG, J.R. *Credit Card Fraud Detection with Autoencoder and Probabilistic Random Forest*. MDPI, 2021.  
- [Mais referências disponíveis no artigo](https://github.com/softwarekleberson/DeepLearning_FraudeCartao).

## Contato
Para mais informações, entre em contato com os autores.

---
