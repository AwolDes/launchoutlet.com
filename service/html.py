# Responsible for generating index.html
def gen_html(data):
    index = open("../html/index.html", 'r+')
    
    index.seek(0)
    index.truncate()

    index.write(
    """<html>
    <head>
        <title>Launch Outlet</title>
        <link rel="stylesheet" href="css/custom.css">
        <link href='https://fonts.googleapis.com/css?family=Lato:400,300' rel='stylesheet' type='text/css'>
    </head>
    
    
    <body>
        
        <h1 class="title">Launch Outlet</h1>
        <p class="blurb">The best places for Startups needing good PR for launch.</p>
        <ol class="sites">"""
        )
    
    for i in data:
        index.write("\n\t\t\t<li class=\"site\"><a href=\"" + str(i[0]) +"\" target=\"_blank\">" + str(i[1]) +"</a></li>")

    index.write(
    """\n\t\t</ol>
        
        <script src="js/custom.js"></script>
    </body>
</html>"""
    

        )




