class IntentionalException(Exception):
    """
    we throw this exception so that it's clear in the logs that this is a test
    """

    pass


def raise_exception(request):
    raise IntentionalException(
        "intentional exception to ensure we have no data leaks"
    )
