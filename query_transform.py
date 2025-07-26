def enrich_query(user_query, zip_code="17104"):
    return f"{user_query.strip()} in ZIP code {zip_code}. Include local resource info."