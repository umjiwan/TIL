import json

def converter(set_post_name_list):
    with open("layout/config.json", "r") as file:
        data = json.load(file)

    username = data["username"]
    branch = data["branch_name"]
    repository = data["repository"]
    
    with open("README.md", "a") as file:
        for set_post_name in set_post_name_list:
            date  = set_post_name[5:10].replace("-", ". ")

            with open(f"post/{set_post_name}", "r") as md_file:
                title = md_file.readline()[2:]

            if before_y != set_post_name[:4]:
                before_y = set_post_name[:4]

                file.write(f"\n## {before_y}<br>\n")

            file.write(f'<a href="https://github.com/{username}/{repository}/blob/{branch}/post/{set_post_name}">{title}</a>\
                            - <i>{date}</i>\
                            <br>\n\
                        ')