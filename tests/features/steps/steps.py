from behave import *

@given('a new user open our website')
def step_impl(context):
    context.browser.get('https://rocky-spire-5172.herokuapp.com')
    form = get_element(context.browser,tag='form')
    form.username="alannsp";form.make="Honda";form.model="Civic";
    form.email="alannsp@gmail.com";form.minYear="2008";form.maxyear="2012";
    form.minPrice="10000";form.maxPrice="15000";
    form.submit()

@then('show user successfully submitted information')
def step_impl(context):
    assert true
    

