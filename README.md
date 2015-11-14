# markdown-it-icon

Emoji icons, Font awesome icons and Ionicons icons for markdown-it.


## Install

`npm install markdown-it-icon --save`


## Usage

```javascript
mdc = mdc.use(require('markdown-it-icon'));
var emojione =require('emojione');
emojione.cacheBustParam = ''; // change this to invalidate emojione icons cache
emojione.imagePathPNG = 'https://cdn.jsdelivr.net/emojione/assets/png/';
mdc.renderer.rules.emoji = function(tokens, idx) {
  var shortname = tokens[idx].markup;
  if(shortname.startsWith('fa-')) { // fontawesome
    return '<i class="fa ' + shortname + '"></i>';
  }
  if(shortname.startsWith('ion-')) { // ionicons
    return '<i class="' + shortname + '"></i>';
  }
  return emojione.shortnameToImage(':' + shortname + ':'); // emojione
};
```


## Syntax

### Emoji icons

`:panda_face:`


### Font awesome icons

`:fa-cog:`


### Ionicons icons

`:ion-social-tux:`


## License

MIT
