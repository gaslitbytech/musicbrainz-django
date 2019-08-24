""" Example of python social auth custom pipelines """


def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == "facebook":
        profile = user.get_profile()
        if profile is None:
            raise NotImplementedError("Profile does not exist")
            profile = Profile(user_id=user.id)
        profile.gender = response.get("gender")
        profile.link = response.get("link")
        profile.timezone = response.get("timezone")
        profile.save()
