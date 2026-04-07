class JiraIntegration:
    """
    Class to interact with Jira to fetch A/B test hypothesis and goals.
    """

    def __init__(self, jira_client):
        """
        Initializes the JiraIntegration with a Jira client.
        """
        self.jira_client = jira_client

    def fetch_hypothesis_and_goals(self, issue_key):
        """
        Fetches the A/B test hypothesis and goals from a Jira issue.
        
        :param issue_key: The key of the Jira issue to fetch data from.
        :return: A dictionary containing hypothesis and goals.
        """
        issue = self.jira_client.issue(issue_key)
        hypothesis = issue.fields.customfield_12345  # Replace with actual custom field ID
        goals = issue.fields.customfield_67890       # Replace with actual custom field ID
        
        return {"hypothesis": hypothesis, "goals": goals}