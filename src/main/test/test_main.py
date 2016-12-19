# encoding: utf-8

from django.core.management import BaseCommand
import pytest


@pytest.mark.unit_test
def test_true():
    assert True


@pytest.mark.integration_test
@pytest.mark.django_db
def test_system_check():
    """
    Performs the Django system check.
    """
    base_command = BaseCommand()
    system_check_errors = base_command.check()
    assert not system_check_errors


@pytest.mark.functional_test
def test_home_title(browser):
    """
    Checks title "Home" in the home page.
    """
    browser.visit('localhost:8000')
    title = browser.title
    browser.quit()
    assert title.lower() == 'home'
