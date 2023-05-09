# About Micro Grad Replication

This is a replication version of [karpathy Andrej's](https://github.com/karpathy/micrograd) mircrograd package, which make the learning process into stages to see how the code was gradually improved. Here are the takeouts:

1. The easy way to explain the process of back propagation: a math expression and we do partial derivative on that for each neuron(cell)

2. Build a simple nn using scalers

   1. Introduce value object + basic operations
   2. Give an example of feed forward nn
   3. Visualize the nn the graph
   4. Back propagation implemention
        - In cell back propagation:
            - Show the derivatives of a function
            - Chain rule: dL/dE = (dL / dF) * (dF / dE)
            - Grad accumulation
        - Semi-auto back propagation
        - full back propagation (style1, style2)
        - use pytorch to show the similarity

   5. Build MLP
        - The imprtance of zero grad!!!
        - build neuron, layer, mlp
          - forward
          - loss
          - zero_grad
          - backword
