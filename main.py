import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, player_data in data.items():

        race_data = player_data.get("race")
        race_obj = None

        if race_data:
            race_obj, _ = Race.objects.get_or_create(
                name=race_data["name"],
                description=race_data["description"]
            )

            skills = race_data.get("skills", [])
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_obj
                )

        guild_data = player_data.get("guild")
        guild_obj = None

        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
            )

        Player.objects.get_or_create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race_obj,
            guild=guild_obj
        )


if "__name__" == "__main__":
    main()
