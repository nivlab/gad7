from scholarly import scholarly
from pandas import DataFrame

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
### Define parameters.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

## Define search queries.
queries = [
    '"gad7" "not at all sure"',
    '"gad-7" "not at all sure"',
    '"generalized anxiety disorder scale" "not at all sure"'
]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
### Query Google scholar.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

## Prealloate space.
search_results = []

## Iterate over queries.
for query in queries:
    
    print('Performing query: %s' %query)
    
    ## Initialize generator object.
    G = scholarly.search_pubs(query, patents=False, year_low=2006)

    ## Iterate over search results.
    for result in G:
        
        ## Append hit.
        try: search_results.append(result.bib)
        except: print(result)
            
## Convert to DataFrame.
search_results = DataFrame(search_results)

## Limit to columns of interest.
cols = ['year','author','title','url','venue','cites']
search_results = search_results[cols]

## Update authors.
search_results['author'] = search_results.author.apply(lambda x: ', '.join(x))

## Drop duplicates.
search_results = search_results.drop_duplicates()

## Save to disk.
search_results.to_csv('search_results.tsv', sep='\t', index=False)