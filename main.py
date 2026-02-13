import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    race1 = None
    guild1 = None

    for user in data.keys():
        for info in data[user].keys():
            race = data[user].get("race")
            if race:
                race1 = Race.objects.get_or_create(
                    name=race["name"],
                    description=race["description"]
                )
                skills = race.get("skill")
                if skills:
                    if isinstance(skills, list):
                        for skill in skills:
                            Skill.objects.get_or_create(
                                name=(skill["name"] if skill["name"] else None),
                                bonus=(skill["bonus"] if skill["bonus"] else None),
                                race__name=(info["name"] if info["name"] else None)
                            )
                guild = race.get("guild")
                if guild:
                    guild1 = Guild.objects.get_or_create(
                        name=guild["name"],
                        description=guild["description"]
                    )

            Player.objects.get_or_create(
                nickname=user,
                email=data[user]["email"],
                bio=data[user]["bio"],
                race=(race1 if race1 else None),
                guild=(guild1 if guild1 else None)
            )


if __name__ == "__main__":
    main()
