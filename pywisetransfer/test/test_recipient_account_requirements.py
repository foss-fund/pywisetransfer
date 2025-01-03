"""Test the requirements for a recipient account."""

import pytest
from pywisetransfer.client import Client
from pywisetransfer.model.currency import Currency


def test_requirements_can_be_parsed(sandbox:Client, currency:Currency):
    """Test the requirements for a recipient account.
    
    Here, we validate that all results can be parsed.
    """
    if currency in [Currency.ZMW, Currency.ZWG, Currency.UYW, Currency.STD, Currency.SSP, Currency.CNH]:
        pytest.skip("Not recorded yet.")
    requirements = sandbox.recipient_accounts.get_requirements_for_currency(source=currency, target=currency, source_amount=100)
    assert True

