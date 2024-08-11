# load data 
filename = 'skeletal_muscle.csv'
data = pd.read_csv(filename)
skeletal_muscle = pd.DataFrame(data)

# calculate mean and standard deviation of the scores
mean_score = skeletal_muscle['scores'].mean()
std_score = skeletal_muscle['scores'].std()

# set the threshold as mean + 1.5 standard deviations
threshold = mean_score + 1.5 * std_score

# filter for genes with scores greater than the threshold and p-value < 0.05
significant_genes = skeletal_muscle[(skeletal_muscle['scores'] > threshold) & (skeletal_muscle['pvals_adj'] < 0.05)]

# extract list of gene names for these significant genes
gene_list = significant_genes['names'].tolist()
