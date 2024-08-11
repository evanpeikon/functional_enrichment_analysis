# create rank file
rank_df = pd.DataFrame({'Gene': skeletal_muscle['names'], 'Score': skeletal_muscle['scores']})
rank_df.set_index('Gene', inplace=True)

# perform GSEA and view results
gsea_results = gp.prerank(rnk=rank_df, gene_sets='KEGG_2016', permutation_num=100, seed=5)
print(gsea_results.res2d)
