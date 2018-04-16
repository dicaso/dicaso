pycassos development
====================

Contributing to the project
---------------------------

Requirements:
- python3 >= 3.6
- virtualenvwrapper
- npm >= 3
- node >= 5
- angular cli
  
Pip packages:

    pip install pycassos[development]


Style guide
-----------
TODO


Original project setup
----------------------

    # doc tree
    mkdir docs && cd docs
    sphinx-quickstart #initiating the documentation
    git add Makefile conf.py index.rst
    make html
    cd ..

    # angular frontend tree
    # => dir for development, dir for build end that will be flask served
    ng new pycassong --style=scss --routing --skip-git
    mkdir -p pycassos/static/song && cd pycassong
    git add README.md e2e karma.conf.js package-lock.json package.json \
      protractor.conf.js src tsconfig.json tslint.json .gitignore \
      .angular-cli.json .editorconfig
    sed -i '' 's+dist+../pycassos/static/song+' .angular-cli.json
    ng build --prod


References
----------
- https://github.com/hawzie197/Flask_Angular4_Skeleton
