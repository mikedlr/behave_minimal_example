from typing import Any
given: Any
when: Any
then: Any

@given(u'that x set to 4')
def step_impl(context):
    context.x = 4


@given(u'I have y set to 7')
def step_impl(context):
    context.y = 7


@when(u'I add those two numbers')
def step_impl(context):
    context.result = context.x + context.y


@then(u'the result should be 11')
def step_impl(context):
    assert context.result == 11
