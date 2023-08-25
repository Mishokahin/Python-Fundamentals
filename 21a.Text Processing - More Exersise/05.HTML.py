article_title = input()
article_content = input()

print("<h1>" + f"\n{4*' '}{article_title}" + "\n</h1>")
print("<article>" + f"\n{4*' '}{article_content}" + "\n</article>")

while True:
    article_comment = input()
    if article_comment == "end of comments":
        break
    print("<div>" + f"\n{4 * ' '}{article_comment}" + "\n</div>")