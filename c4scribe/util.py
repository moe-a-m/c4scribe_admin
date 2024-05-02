import os


def md2html(response):
    with open('response.md', 'w+') as f:
        f.write(response.text)

    # Command to execute
    # Using Windows OS command
    print("Converting markdown to html")
    cmd = 'markdown_py -x plantuml_markdown response.md > templates/out.html'
    # Using os.system() method
    os.system(cmd)
    print("End markdown to html")
    return "out.html"