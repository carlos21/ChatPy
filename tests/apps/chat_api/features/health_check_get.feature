Feature: API status
  In order to show the server is up and running
  As a health check
  I want to check the API Status

  Scenario: Check the API status
    Given  I sent a GET request to "/health-check"
    Then the response content should be:
    """
      {'status': 'ok'}
    """