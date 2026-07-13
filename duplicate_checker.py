from rapidfuzz import fuzz


def check_name_similarity(new_name, existing_users):

    for user in existing_users:

        existing_name = user[0]

        similarity = fuzz.ratio(
            new_name.lower(),
            existing_name.lower()
        )

        if similarity >= 90:

            return True, existing_name, similarity

    return False, None, None