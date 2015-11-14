from fabric.api import local

def dist():
    local('browserify index.js -s markdownitIcon > dist/markdown-it-icon.js')
    local('uglifyjs dist/markdown-it-icon.js -c -m > dist/markdown-it-icon.min.js')
