from modules import links_parser


def run():
    links_arr = links_parser.run()
    full_links = []

    for link in links_arr:
        if link[0] == '/':
            link = 'https:' + link
            full_links.append(link)

    return full_links
