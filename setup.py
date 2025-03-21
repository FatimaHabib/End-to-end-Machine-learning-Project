import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"
PEPO_NAME = "End-to-End-Machine-Learning-Pipeline"
AUTHOR_USER_NAME = "FatimaHabib"
SRC_REPO ="mlproject"
AUTHOR_EMAIL = "habib.fatima.eng@gmail.com"

setuptools.setup(name=SRC_REPO,
                 version=__version__,
                 author=AUTHOR_USER_NAME,
                 author_email=AUTHOR_EMAIL,
                 description="A small python package for NLP app",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url=f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
                 project_urls={
                     "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}/issues",
                     
                 },
                 package_dir={"": "src"},
                 packages=setuptools.find_packages(where="src")
                 
)