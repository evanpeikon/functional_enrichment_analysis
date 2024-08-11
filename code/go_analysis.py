# initialize GProfiler and return result in pandas DataFrame format
gp = GProfiler(return_dataframe=True)

# perform GO analysis using the significant gene list
go_results = gp.profile(organism='hsapiens', query=gene_list)

# display the first few results
print(go_results.head())

# plot results
sns.barplot(x='intersection_size', y='name', data=go_results.head(10))
plt.title('Top 10 Enriched GO Terms')
plt.xlabel('Intersection Size')
plt.ylabel('GO Term')
plt.show()
