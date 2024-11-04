def main_context(request):
    user = request.user
    usertype = user.usertype if user.is_authenticated else None

    context = {
        "usertype": usertype,
    }

    return context
