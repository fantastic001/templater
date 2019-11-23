from distutils.core import setup
setup(
  name = 'templater',
  packages = ['templater', 'templater.sources', 'templater.tps'],
  version = '0.1',
  description = 'Code generation tool based oon given templates',
  author = 'Stefan Nožinić',
  author_email = 'stefan@lugons.org',
  url = 'https://github.com/fantastic001/templater', # use the URL to the github repo
  download_url = 'https://github.com/fantastic001/templater/tarball/0.1',
  keywords = ['dev', 'codegen', 'tools'], 
  package_dir = {'templater': 'src/'},
  classifiers = [],
  scripts = ["templater"],
  install_requires=["ArgumentStack", "jinja2"] # dependencies listed here 
)
