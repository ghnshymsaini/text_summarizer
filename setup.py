import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__="0.0.0"

REPO_NAME = "text_summarizer"
AUTHOR_USER_NAME = "ghnshymsaini"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "ghnshymsaini@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ghnshymsaini/text/{REPO_NAME}",
    project_urls={
        "Source Code": "https://github.com/ghnshymsaini/{REPO_NAME}",
        "Issue Tracker": "https://github.com/ghnshymsaini/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"))

