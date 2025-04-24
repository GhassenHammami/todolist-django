def user_profile(request):
    """
    Adds user profile information to the template context.
    """
    if request.user.is_authenticated:
        try:
            profile = request.user.userprofile
            return {
                'user_profile': profile,
            }
        except:
            return {}
    return {} 