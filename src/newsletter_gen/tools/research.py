from crewai_tools import BaseTool
from exa_py import Exa
import os
from datetime import datetime, timedelta
from typing import List

class SearchAndContents(BaseTool):
    name: str = "Search and Contents Tool"
    description: str = (
        "Searches the web based on a search query for the latest results. Results are only from the last week. Uses the Exa API. This also returns the contents of the search results."
    )

    def _run(self, search_query: str) -> str:

        exa = Exa(api_key=os.getenv("EXA_API_KEY"))

        one_week_ago = datetime.now() - timedelta(days=7)
        date_cutoff = one_week_ago.strftime("%Y-%m-%d")

        search_results = exa.search_and_contents(
            query=search_query,
            use_autoprompt=True,
            start_published_date=date_cutoff,
            text={"include_html_tags": False, "max_characters": 8000},
        )

        return search_results


class FindSimilar(BaseTool):
    name: str = "Find Similar Tool"
    description: str = (
        "Searches for similar articles to a given article using the Exa API. Takes in a URL of the article"
    )

    def _run(self, article_url: str) -> str:

        one_week_ago = datetime.now() - timedelta(days=7)
        date_cutoff = one_week_ago.strftime("%Y-%m-%d")

        exa = Exa(api_key=os.getenv("EXA_API_KEY"))

        search_results = exa.find_similar(
            url=article_url, start_published_date=date_cutoff
        )

        return search_results


class GetContents(BaseTool):
    name: str = "Get Contents Tool"
    description: str = "Gets the contents of a specific article using the Exa API. Takes in the ID of the article in a list, like this: ['https://www.cnbc.com/2024/04/18/my-news-story']."
    
    def _run(self, article_ids: List[str]) -> str:

        exa = Exa(api_key=os.getenv("EXA_API_KEY"))

        contents = exa.get_contents(article_ids)
        return contents
    

# if __name__ == "__main__":
#     get_contents = GetContents()
#     article_ids =  ["https://syncedreview.com/2024/07/30/unlocking-generalist-ai-potential-in-software-development-with-opendevin/", "https://arxiv.org/abs/2408.00989", "https://arxiv.org/abs/2407.21635", "https://arxiv.org/abs/2408.01380", "https://www.businesstoday.in/technology/news/story/elon-musk-on-teslas-optimus-the-billion-robot-army-could-be-largest-source-for-ai-data-440039-2024-08-03?utm_source=rssfeed", "https://x.com/ExtremeNetworks/status/1819085769258017022", "https://arxiv.org/abs/2407.21565"]
#     # article_ids = {["https://syncedreview.com/2024/07/30/unlocking-generalist-ai-potential-in-software-development-with-opendevin/", "https://arxiv.org/abs/2408.00989", "https://www.businesstoday.in/technology/news/story/elon-musk-on-teslas-optimus-the-billion-robot-army-could-be-largest-source-for-ai-data-440039-2024-08-03?utm_source=rssfeed", "https://arxiv.org/abs/2407.21635", "https://arxiv.org/abs/2408.01380", "https://arxiv.org/abs/2407.21565", "https://dev.to/oliver_parker_ai/top-5-platforms-for-building-ai-agents-key-features-use-cases-and-pricing-insights-2dn7"]}
#     contents = get_contents.run(article_ids)
#     print(contents)