from django.contrib.auth.models import User
from account.models import Profile
from beacon.models import Beacon


def get_beacon_profiles(auth_user, user):
    beacon = Beacon.objects.get(user=auth_user)
    profiles = None
    try:
        profiles = beacon.beacon_list.get(user=user)
    except Profile.DoesNotExist:
        pass
    return profiles

def beacon_search(auth_user, username):
    users = [user for user in User.objects.filter(username__startswith=username)]

    beacon_profiles = [get_beacon_profiles(auth_user, user) for user in users if get_beacon_profiles(auth_user, user) is not None]
    return beacon_profiles

if __name__ == '__main__':
    s = beacon_search('davidjoy')
    print(s)
