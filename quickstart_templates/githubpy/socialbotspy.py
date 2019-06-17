""" Quickstart script for GithubPy usage """

# imports
from githubpy import GithubPy
from githubpy import smart_run
from socialcommons.file_manager import set_workspace
from githubpy import settings

import random

# set workspace folder at desired location (default is at your home folder)
set_workspace(settings.Settings, path=None)

# get an GithubPy session!
session = GithubPy(use_firefox=True)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_dont_include(["timgrossmann", "uluQulu", "converge"])

    session.set_do_follow(enabled=True, percentage=40, times=1)

    targets = ['timgrossmann', 'uluQulu', 'converge', 'rauchg']
    number = random.randint(3, 5)
    random_targets = targets

    if len(targets) <= number:
        random_targets = targets
    else:
        random_targets = random.sample(targets, number)

    sites = ["instagram", "linkedin", "medium", "facebook", "twitter", "quora", "social media",
            "snapchat", "whatsapp", "slack",
            "tiktok", "periscope", "youtube",
            "gleam", "giveaway", "paid to click", "paid to watch"]
    suffix = ["bot", "automation", "selenium", "api bot",
            "chatbot", "message bot", "dm bot", "like follow bot",
            "automate", "automate AI", "automate ML", "automate deep learning", "automate API"]

    session.search_and_copy_contributors(search_query=random.choice(sites) + " " + random.choice(suffix),
                            dest_organisation="socialbotspy")

    # session.copy_contributors(source_user="realsirjoe",
    #                           source_repo="instagram-scraper",
    #                           dest_organisation="socialbotspy")
    # session.copy_contributors(source_user="instabot-py",
    #                           source_repo="instabot.py",
    #                           dest_organisation="socialbotspy")
    # session.copy_contributors(source_user="social-manager-tools",
    #                           source_repo="socialmanagertools-igbot",
    #                           dest_organisation="socialbotspy")
    # session.copy_contributors(source_user="brunocvcunha",
    #                           source_repo="instagram4j",
    #                           dest_organisation="socialbotspy")
    # session.copy_contributors(source_user="FeezyHendrix",
    #                           source_repo="Insta-mass-account-creator",
    #                           dest_organisation="socialbotspy")
    # session.copy_contributors(source_user="instagrambot",
    #                           source_repo="instabot",
    #                           dest_organisation="socialbotspy")
    # session.copy_contributors(source_user="ytdl-org",
    #                           source_repo="youtube-dl",
    #                           dest_organisation="socialbotspy")
    # session.copy_contributors(source_user="mpawlak2",
    #                           source_repo="instalike-instagram-bot",
    #                           dest_organisation="socialbotspy")
    session.follow_user_followers(random_targets,
                                  amount=random.randint(30, 60),
                                  randomize=True, sleep_delay=600,
                                  interact=True)

    session.follow_user_following(random_targets,
                                  amount=random.randint(30, 60),
                                  randomize=True, sleep_delay=600,
                                  interact=True)

    session.unfollow_users(amount=random.randint(60, 70), skip=170)

