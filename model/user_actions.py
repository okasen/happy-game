class Response:
    rebellious: bool


def accept():
    return Response(rebellious=False)


def refuse():
    return Response(rebellious=True)
