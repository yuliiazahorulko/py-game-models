import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, player_data in data.items():

        race_data = player_data.get("race")
        race1 = None
        guild1 = None

        if race_data:
            race1, _ = Race.objects.get_or_create(
                name=race_data["name"],
                description=race_data["description"]
            )

            skills = race_data.get("skill")
            if isinstance(skills, list):
                for skill in skills:
                    Skill.objects.get_or_create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race1
                    )

            guild_data = race_data.get("guild")
            if guild_data:
                guild1, _ = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    description=guild_data["description"]
                )

        Player.objects.get_or_create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race1,
            guild=guild1
        )


if __name__ == "__main__":
    main()
