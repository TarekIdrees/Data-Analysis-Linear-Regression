# The program is divided into two parts :
* ## Part A : performs analysis on the “gene_table.txt” dataset attached in order to :
      1. Compute the total number of genes and compute the number of different gene biotypes.
      2. Compute the minimum, maximum, average and median number of known isoforms.
      3. Compute, for each chromosome, the number of genes it contains by plotting a bar chart. Also, print the chromosomes with the corresponding number 
         of genes in increasing order.
      4. Computes, for each chromosome, the percentage of genes located on the + strand.
      5. Compute, for each biotype, the average number of transcripts associated to genes
         belonging to the biotype.

* ## Part B : program that uses linear regression with gradient descent to predict the value of UACR based on the FBG of a patient since this value can be used for early detection of kidney disease in diabetic patients.
   **Part B is divided into several parts :**
    *  Read and plot the data.
    *  Separate the data into training and testing. 
    *  Convert from data frames to numpy matrices.
    *  implement the cost function and GradientDescent function. 
    *  Draw the line for FBG (mg/dL) vs UACR (mg/g creatinine)
    *  Draw error graph between iteration and cost.  
