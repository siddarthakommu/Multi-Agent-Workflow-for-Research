from arxiv import Search
from utils.logger import logger

def retrieve_papers(query, max_results=5):
    logger.info(f"Retrieving papers for query: '{query}'")
    search = Search(query=query, max_results=max_results)
    papers = []
    for result in search.results():
        content = f"Title: {result.title}\n\nAbstract: {result.summary}"
        papers.append(content)
    logger.info(f"Retrieved {len(papers)} papers.")
    return papers
