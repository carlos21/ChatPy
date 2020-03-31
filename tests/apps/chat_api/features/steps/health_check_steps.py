from behave import given, when, then, step

@given(u'app is setup')
def app_is_setup(context):
  pass

@given(u'I send a GET request to "{service}"')
def step_send_request(context, service):
    pass

@then(u'the response content should be "{result}"')
def step_response_content_should_be(context, result):
    pass
