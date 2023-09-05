CN_NAME = {
    "calyx_gold": "拟造花萼（金）",
    "calyx_red": "拟造花萼（赤）",
    "cavern": "侵蚀隧洞",
    "shadow": "凝滞虚影",
    "echo": "历战余响"
}


def name_to_template(name: str):
    from script.utils import template_path
    name = name.upper()
    template = "template_path." + name
    return eval(template)
