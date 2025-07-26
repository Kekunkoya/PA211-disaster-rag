def retrieve_with_fallback(query, vectorstore):
    docs = vectorstore.similarity_search(query, k=4)
    if not docs:
        return ["No results found."], "openai"
    return [d.page_content for d in docs], "openai"