# https://github.com/jamalex/notion-py/issues/343
from notion.client import NotionClient
from notion.block import PageBlock
from md2notion.upload import upload

my_token_v2 = "d0adf9d574d1ac180fb677ccfe701bb50f78926e5552b6be532b70cded234fba05d35898e2d13ec14c4db2bb2d007755d19ef1e7f84fad2251e67d350852c1424b5dc4ec328f0b3ec2e6207f2c43"
my_secret = "secret_gOCqwjvOCc5vSY7Cwtzz9NTecTKEx5eD1Z5KI0yGQrn"
url = "https://www.notion.so/ehawk/Engineering-8982234254df4a99bca13654a714ba89"

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in (non-guest) session on Notion.so
# client = NotionClient(token_v2="<token_v2>")
client = NotionClient(token_v2=my_token_v2)

# Replace this URL with the URL of the page you want to edit
page = client.get_block(url)

print("The old title is:", page.title)

# Note: You can use Markdown! We convert on-the-fly to Notion's internal formatted text data structure.
page.title = "Engineering"

with open("TestMarkdown.md", "r", encoding="utf-8") as mdFile:
    newPage = page.children.add_new(PageBlock, title="TestMarkdown Upload")
    upload(mdFile, newPage) #Appends the converted contents of TestMarkdown.md to newPage